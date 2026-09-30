import numpy as np

from image_inspector.analysis import img_info


def test_img_info():
    img = np.zeros((100, 200, 3), dtype=np.uint8)

    result = img_info(img)

    assert result["width"] == 200
    assert result["height"] == 100
    assert result["channels"] == 3
    assert result["dtype"] == "uint8"