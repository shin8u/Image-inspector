import cv2
import numpy as np

def to_hsv(img):
        if img.ndim == 2:
                img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
        return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def to_grayscale(img):
        if img.ndim == 3:
                return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return img

def blur(img, kernel_size):
        
        if kernel_size[0] % 2 == 0 or kernel_size[0] != kernel_size[1] or kernel_size[0] < 0:
                raise ValueError("Неправильный размер ядра.")

        return cv2.GaussianBlur(img, ksize=kernel_size, sigmaX=0)

def threshold(img, threshold_value):
        if threshold_value < 0 or threshold_value > 255:
                raise ValueError("Недопустимое значение порога.")
        grey_img = img
        if img.ndim != 2:
                grey_img = to_grayscale(grey_img)

        _, thresh = cv2.threshold(grey_img, threshold_value, 255, cv2.THRESH_BINARY)

        return thresh
        

