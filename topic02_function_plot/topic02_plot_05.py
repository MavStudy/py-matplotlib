# Matplotlib - Функция plot для построения и оформления двумерных графиков
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def main():
    matplotlib.use('TkAgg')

    # Давайте сразу на график наложим сетку, чтобы он выглядел более
    # информативно. Для этого достаточно прописать строчку:
    plt.grid()

    y = np.arange(0, 5, 1)  # [0, 1, 2, 3, 4]
    x = np.array([a*a for a in y])  # [0, 1, 4, 9, 16]
    y2 = [0, 1, 2, 3]
    x2 = [i+1 for i in y2]

    plt.plot(x, y, x2, y2)
    plt.show()

    # Причем, оба графика отображаются совершенно независимо. В частности, они
    # здесь имеют разное число точек. Никаких проблем не возникает.


if __name__ == '__main__':
    main()
