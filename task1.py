# -*- coding: UTF-8 -*-


def arrayModificator(arr, transformer) -> list:
    """Результат выполнения принятой функции.

    На вход принимаем массив и функцию.
    Применяем принятую функцию ко всем элементам массива.
    :type transformer: function
    :type arr: list
    """
    return list(map(transformer, arr))
