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

def test_calculate_channel_means_black():
    img = np.zeros((100,200,3), dtype=np.uint8)
    result = calculate_channel_means(img)

    assert result['B'] == 0
    assert result['G'] == 0
    assert result['R'] == 0


def test_calculate_channel_means_known_value():
    img = np.array([
    [[10, 20, 30], [40, 50, 60]],
    [[70, 80, 90], [100, 50, 20]]
    ], dtype=np.uint8)

    result = calculate_channel_means(img)

    assert result["B"] == 55
    assert result["G"] == 50
    assert result["R"] == 50

def test_calculate_channel_means_grayscale():
    img = np.array([
    [10, 40],
    [70, 100]
    ], dtype=np.uint8)

    result = calculate_channel_means(img)

    assert result["brightness"] == 55

def test_calculate_brightness_histogram():
    img = np.array([
        [[10, 20, 30], [40, 50, 60]],
        [[70, 80, 90], [100, 50, 20]]
        ], dtype=np.uint8)

    result = calculate_brightness_histogram(img)

    assert result[30] == 1
    assert result[60] == 1
    assert result[90] == 1
    assert result[100] == 1
    assert sum(result) == 4

