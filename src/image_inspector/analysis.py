import cv2
import numpy as np
from . import processing


def img_info(img):
    result = {}
    result['width'] = img.shape[1]
    result['height'] = img.shape[0]
    if img.ndim == 3:
        result['channels'] = img.shape[2]
    result['dtype'] = str(img.dtype)

    return result

def calculate_brightness_hsv(img):
    img_hsv = processing.to_hsv(img)

    value = img_hsv[:,:,2]

    return float(np.mean(value))

def calculate_channel_means(img):
    
    match img.ndim:
        case 2:
            return {"brightness": calculate_brightness_hsv(img)}
        case 3:
            means = img.mean(axis=(0,1))
            return {
                "B": float(means[0]),
                "G": float(means[1]),
                "R": float(means[2])
                }

def calculate_brightness_histogram_hsv(img):
    hsv_img = processing.to_hsv(img)
    hist = [0] * 256
    for i in hsv_img[:,:,2]:
        for j in i:
            hist[j] += 1

    return hist

def calculate_brightness_grayscale(img):
    img_gray = processing.to_grayscale(img)

    return float(np.mean(img_gray))

def calculate_brightness_histogram_grayscale(img):
    img_gray = processing.to_grayscale(img)
    hist = [0] * 256
    for i in img_gray:
        for j in i:
            hist[j] += 1

    return hist