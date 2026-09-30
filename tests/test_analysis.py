import numpy as np

from image_inspector.analysis import *


def test_img_info():
    img = np.zeros((100, 200, 3), dtype=np.uint8)

    result = img_info(img)

    assert result["width"] == 200
    assert result["height"] == 100
    assert result["channels"] == 3
    assert result["dtype"] == "uint8"

def test_calculate_brightness_black():
    img = np.zeros((100,200,3), dtype=np.uint8)
    result = calculate_brightness(img)

    assert result == 0

def test_calculate_brightness_known_value():
    img = np.array([
    [[10, 20, 30], [40, 50, 60]],
    [[70, 80, 90], [100, 50, 20]]
    ], dtype=np.uint8)

    result = calculate_brightness(img)

    assert result == 70
