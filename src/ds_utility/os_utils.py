import os
import shutil
from typing import NoReturn

import structlog

from ds_utility.typing_utils import PathType

logger = structlog.get_logger()


def os_rm(path: PathType) -> NoReturn:
    """Delete a file or directory given a relative / absolute path.

    Ref: https://stackoverflow.com/a/41789397

    Arguments:
        path: Path as string or pathlib PosixPath
    """
    if os.path.isfile(path) or os.path.islink(path):
        os.remove(path)
    elif os.path.isdir(path):
        shutil.rmtree(path)


def os_mkdir_p(path: PathType, overwrite=False) -> NoReturn:
    """Create a directory with a provided path (relative / absolute)."""
    try:
        os.makedirs(path, exist_ok=overwrite)
    except OSError:
        logger.warning(
            "Directory already exists. Use overwrite=True to overwrite.", path=path
        )


def os_cp(path: PathType, dst: PathType, overwrite=False) -> NoReturn:
    """Copy a file to a destination or to a folder.

    Ref: https://stackoverflow.com/a/13814557

    Arguments:
        path: Path as string or pathlib PosixPath for source
        dst: Path as string or pathlib PosixPath for destination
        overwrite: Whether to overwrite the final directory.
    """
    if not os.path.exists(dst):
        os.makedirs(dst)
    if os.path.isfile(path):
        shutil.copy2(path, dst)
    elif os.path.isdir(path):
        for item in os.listdir(path):
            s = os.path.join(path, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=overwrite)
            else:
                if (
                    not os.path.exists(d)
                    or os.stat(s).st_mtime - os.stat(d).st_mtime > 1
                ):
                    shutil.copy2(s, d)
