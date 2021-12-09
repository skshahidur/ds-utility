import os

import numpy as np

# import pytest
from PIL import Image

from ds_utility.mlflow.sklearn_utils import classification_report_mlflow


# @pytest.fixture()
def test_classification_report_mlflow():
    real = [
        "a",
        "d",
        "a",
        "c",
        "c",
        "a",
        "a",
        "b",
        "d",
        "c",
        "a",
        "a",
        "a",
        "a",
        "d",
    ]
    pred = [
        "a",
        "d",
        "a",
        "a",
        "d",
        "b",
        "c",
        "a",
        "a",
        "b",
        "b",
        "c",
        "b",
        "d",
        "c",
    ]
    path_to_asset = os.path.dirname(os.path.dirname(__file__)) + "/assets"
    expected_image_dir = path_to_asset + "/observed/"
    classification_report_mlflow(real, pred, path=expected_image_dir)

    observed_image_path = path_to_asset + "/expected/classification_report.png"
    assert_images_equal(
        expected_image_dir + "classification_report.png", observed_image_path
    )


def assert_images_equal(image_1: str, image_2: str):
    img1 = Image.open(image_1)
    img2 = Image.open(image_2)

    # Convert to same mode and size for comparison
    img2 = img2.convert(img1.mode)
    img2 = img2.resize(img1.size)

    print(np.asarray(img1).shape)  # noqa
    print(np.asarray(img2).shape)  # noqa

    sum_sq_diff = np.sum(
        (np.asarray(img1).astype("float") - np.asarray(img2).astype("float")) ** 2
    )

    if sum_sq_diff == 0:
        pass
    else:
        assert 1 / np.sqrt(sum_sq_diff) < 0.001
