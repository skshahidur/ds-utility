import os
from pathlib import Path

from ds_utility.os_utils import os_cp, os_mkdir_p, os_rm


def test_os_rm_cp_mkdir():
    current_path = Path(__file__).parent
    os_mkdir_p(current_path / "sample/abc")
    assert "sample" in os.listdir(current_path)
    assert "abc" in os.listdir(current_path / "sample/")
    os_cp(current_path / "sample/abc", current_path / "sample/cba")
    assert "cba" in os.listdir(current_path / "sample/")
    # assert [f in os.listdir(current_path / "sample") for f in ["abc", "cba"]]
    os_rm(current_path / "sample/abc")
    assert "abc" not in os.listdir(current_path / "sample/")
    os_rm(current_path / "sample/cba")
    assert "cba" not in os.listdir(current_path / "sample/")
    os_rm(current_path / "sample/")
    assert "sample" not in os.listdir(current_path)


test_os_rm_cp_mkdir()
