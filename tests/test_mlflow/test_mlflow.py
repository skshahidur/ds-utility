import os

import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as ssim

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
    observed_image_dir = path_to_asset + "/observed/"
    classification_report_mlflow(real, pred, path=observed_image_dir)

    expected_image_path = path_to_asset + "/expected/classification_report.png"
    assert_images_equal(
        observed_image_dir + "classification_report.png", expected_image_path
    )


def assert_images_equal(image_1: str, image_2: str):

    img1 = np.asfarray(Image.open(image_1).convert("L"))
    img2 = np.asfarray(Image.open(image_2).convert("L"))
    similiarity = ssim(
        img1,
        img2,
        multichannel=True,
        gaussian_weights=True,
        sigma=1.5,
        use_sample_covariance=False,
        data_range=255,
    )
    assert similiarity > 0.9
