# -*- coding: UTF-8 -*-


def squaresList(n) -> list:
    """Список квадратов нечетных чисел.

    На вход принимаем заданное число. Заполняем пустой массив:
    проверяем на нечетность и возводим в квадрат.
    """
    squares = []
    for i in range(1, n + 1):
        if i % 2 != 0:
            squares.append(i * i)
    return squares
