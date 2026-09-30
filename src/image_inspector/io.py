import cv2

def load_image(path):
    img = cv2.imread(path)

    if img is None:
        raise ValueError(f"Не удалось открыть изображение по пути {path}.")

    return img

def save_image(img, path):
    result = cv2.imwrite(path, img)

    if not result:
        raise ValueError("Не удалось сохранить изображение.")