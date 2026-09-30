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

def calculate_brightness(img):
    img_hsv = processing.to_hsv(img)
    
    value = img_hsv[:,:,2]

    return value.sum()/value.size

def calculate_channel_means(img):
    
    match img.ndim:
        case 2:
            return {"B": calculate_brightness(img)}
        case 3:
            means = img.mean(axis=(0,1))
            return {
                "B": float(means[0]),
                "G": float(means[1]),
                "R": float(means[2])
                }

def calculate_brightness_histogram(img):
    hsv_img = processing.to_hsv(img)
    hist = [0] * 256
    for i in hsv_img[:,:,2]:
        for j in i:
            hist[j] += 1

    return hist