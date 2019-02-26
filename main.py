from task1 import arrayModificator
from task2 import squaresList
from task3 import maxNumber
from task4 import letterCounter

# Task 1
print('TASK 1\n')

b = [1, 2, 3]  # type: list


def incOne(param):
    """Увеличиваем элемент на 1."""
    return param + 1


print('sourse array: ', b)
print('result array with incOne: ', arrayModificator(b, incOne))

print('\n===============\n')
# end task 1

# Task 2
print('TASK 2\n')

n = 15  # type: int

print('number: ', n)
print('result array of squaring odd numbers: ', squaresList(n))

print('\n===============\n')
# end task 2

# Task 3
print('TASK 3\n')

elements = [-1, -10, -5, -1000, -2000, 10]

print('elements: ', elements)
print('max element: ', maxNumber(*elements))

print('\n===============\n')
# end task 3

# Task 4
print('TASK 4\n')

exampleSentence = "Привет! Это тестовое задание."  # type: str

print('sentense: ', exampleSentence)
print('statistic: ', letterCounter(exampleSentence))

print('\n===============\n')
# end task 4
