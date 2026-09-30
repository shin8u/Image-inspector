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

def test_detect_edges():
    img = np.array([
        [0, 0, 0, 0, 0],
        [0, 255, 255, 255, 0],
        [0, 255, 255, 255, 0],
        [0, 255, 255, 255, 0],
        [0, 0, 0, 0, 0]
        ], dtype=np.uint8)

    result = detect_edges(img, 100, 200)

    flag_zeros_max = 0
    flag_is_max = 0

    for i in result:
        for j in i:
            if j != 0 and j != 255:
                flag_zeros_max = 1
            if j == 255:
                flag_is_max = 1
 
    assert result.ndim == 2
    assert flag_zeros_max == 0
    assert flag_is_max == 1

def test_detect_edges_valid_value():
    img = np.array([
            [0, 0, 0, 0, 0],
            [0, 255, 255, 255, 0],
            [0, 255, 255, 255, 0],
            [0, 255, 255, 255, 0],
            [0, 0, 0, 0, 0]
            ], dtype=np.uint8)
    with pytest.raises(ValueError):
        detect_edges(img, 100, 100)
