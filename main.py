import matplotlib.pyplot as plt
from PIL import Image


def show_meme(image_path):
    # Открываем изображение с помощью PIL
    img = Image.open(image_path)

    # Создаем фигуру для отображения
    plt.figure(figsize=(8, 8))

    # Показываем изображение
    plt.imshow(img)
    plt.axis('off')  # Отключаем оси
    plt.show()


if __name__ == '__main__':
    show_meme('C:/Users/YVozhdaeva/Desktop/memes/mem.jpg')


