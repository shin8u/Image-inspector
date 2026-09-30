from . import analysis
from . import inout

path = input('Введите путь к изображению.')

img = inout.load_image(path)
print(analysis.calculate_brightness_histogram(img))