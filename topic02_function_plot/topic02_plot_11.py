# Matplotlib - Функция plot для построения и оформления двумерных графиков
# Изменение цвета линий графиков.
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def main():
    matplotlib.use('TkAgg')

    plt.grid()

    y = np.arange(0, 5, 1)  # [0, 1, 2, 3, 4]
    x = np.array([a*a for a in y])  # [0, 1, 4, 9, 16]
    y2 = [0, 1, 2, 3]
    x2 = [i+1 for i in y2]

    # Помимо типа линий у графиков, конечно же, можно менять и их цвет.
    # В самом простом варианте достаточно после стиля указать один из символов
    # предопределенных цветов:
    #
    # <p align=center>{'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w'}
    #
    # Цвет можно понять по английскому названию указанной первой буквы.
    # Например,
    #
    # b = blue, r = red, g = green, c = cyan, w = white, и т.д.

    # Давайте изменим цвет у наших графиков, указав символы g и m:
    # lines = plt.plot(x, y, '--g', x2, y2, ':m')
    #
    # Можно использовать именованный параметр color (или просто букву c)
    # для более точной настройки цвета:
    lines = plt.plot(x, y, '--g', x2, y2, ':m', color='r')
    print(lines)
    plt.show()

    # В данном случае оба графика будут отображены красным. Преимущество этого
    # параметра в возможности указания цвета не только предопределенными
    # символами, но, например, в шестнадцатиричной записи:
    lines = plt.plot(x, y, '--g', x2, y2, ':m', color='#0000CC')
    print(lines)
    plt.show()

    # Или в виде кортежей формата:
    lines = plt.plot(x, y, '--g', x2, y2, ':m', color=(0, 0, 0))
    print(lines)
    plt.show()

    lines = plt.plot(x, y, '--g', x2, y2, ':m', color=(0, 0, 0, 0.5))
    print(lines)
    plt.show()


if __name__ == '__main__':
    main()
# Варианты типа линий
# -----------------------------------------------------------------------------
#  Обозначение типа | Описание
#  линии            |
# -----------------------------------------------------------------------------
#  '-'              | Непрерывная линия (используется по умолчанию)
# -----------------------------------------------------------------------------
#  '--'             | Штриховая линия
# -----------------------------------------------------------------------------
#  '-.'             | Штрихпунктирная линия
# -----------------------------------------------------------------------------
#  ':'              | Пунктирная линия
# -----------------------------------------------------------------------------
#  'None' или ''    | Без рисования линии
# -----------------------------------------------------------------------------
