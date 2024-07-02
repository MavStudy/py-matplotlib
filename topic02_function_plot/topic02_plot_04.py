# Matplotlib - Функция plot для построения и оформления двумерных графиков
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def main():
    matplotlib.use('TkAgg')

    #  мы можем рисовать графики с разными шагами по оси абсцисс,
    #  например, так:
    y = np.arange(0, 5, 1)  # [0, 1, 2, 3, 4]
    x = np.array([a*a for a in y])  # [0, 1, 4, 9, 16]
    plt.plot(x, y)
    plt.show()

    # Вот так гибко и интуитивно понятно обрабатывает
    # функция plot() входные данные.


if __name__ == '__main__':
    main()
