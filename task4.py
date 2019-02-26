# -*- coding: UTF-8 -*-


def letterCounter(sentence) -> dict:
    """Количество каждой буквы в предложении.

     На вход принимаем строку.
     Считаем количество каждого символа и сохраняем в  словарь.
     :type sentence: str
      """
    statistic = {}
    for i in sentence:
        if i in statistic:
            statistic[i] += 1
        else:
            statistic[i] = 1
    return statistic
