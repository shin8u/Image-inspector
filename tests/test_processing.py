from image_inspector.processing import *
import numpy as np
import pytest

def test_blur():
    img = np.zeros((5,5,1),dtype=np.uint8)
    img[2][2] = 255

    result = blur(img, (3,3))

    assert result[2][2] == 64

def test_blur_invalid_kernel():
    img = np.zeros((5,5,1),dtype=np.uint8)
    img[2][2] = 255
    with pytest.raises(ValueError):
        blur(img, (0,0))

def test_threshold():
    img = np.array([
        [10, 40],
        [80, 100]
        ], dtype=np.uint8)

    result = threshold(img, 80)

    assert result[1][1] == 255
    assert result[1][0] == 0
    assert sum(result[0]) + sum(result[1]) == 255

def test_threshold_invalid_value():
    img = np.array([
        [10, 40],
        [70, 100]
        ], dtype=np.uint8)

    with pytest.raises(ValueError):
        threshold(img, -1)