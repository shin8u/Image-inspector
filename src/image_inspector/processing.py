import cv2

def to_hsv(img):
    if img.ndim == 2:
            img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def to_grayscale(img):
      if img.ndim == 3:
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
      return img