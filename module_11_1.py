import requests
import numpy as np
from PIL import Image

url = 'https://mediasole.ru/'
response = requests.get(url)
print(response)
r1 = requests.post(url, data={'key': 'value'})
print(r1)
r2 = requests.head(url)
print(r2)

a = np.array([1, 2, 35, 7, 54])
delta = np.ones(5, dtype=int)
print(a + delta)
print(a * a)
print(a.sum())

image_path = 'C:/Python/pythonProject4/ёлка.jpg'
image = Image.open(image_path)
new_size = (1000, 600)
resized_image = image.resize(new_size)  # Изменен размер
data = image.getdata()
new_data = []
for item in data:
    if isinstance(item, tuple) and len(item) >= 3:
        new_data.append((item[0], 0, 0))
    else:
        new_data.append(item)
filtered_image = Image.new(image.mode, image.size)
filtered_image.putdata(new_data)
filtered_image.save(image_path)  # Изменен цвет на красный
output_path = 'C:/Python/pythonProject4/output_image.png'
resized_image.save(output_path, format='PNG')  # Сохранение в другом формате
