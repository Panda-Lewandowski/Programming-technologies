import random
from datetime import datetime


def binary_search(l, value, low=0, high=-1):
    if not l or not (value >= l[0] and value <= l[-1]):
        raise ValueError("Элемент находится вне списка!")

    if high == -1: 
        high = len(l) - 1

    if low >= high:
        if l[low] == value: 
            return low
        else: 
            raise ValueError("Элемент не найден!")

    mid = (low + high) // 2

    if l[mid] > value: 
        return binary_search(l, value, low, mid - 1)
    elif l[mid] < value: 
        return binary_search(l, value, mid + 1, high)
    else: 
        return mid


if __name__ == '__main__':
    random.seed(datetime.now())

    n = int(input('Введите размерность списка: '))
    lst = [random.randint(700, 800) for _ in range(n)]
    lst.sort()
    
    print(f"Сгенерированный список: {lst}")
    to_find = random.choice(lst)
    print(f"Элемент, который должен быть найден: {to_find}")
    result = binary_search(lst, to_find)
    print(f"Позиция, на которой элемент найден: {result}")
    print(f"Проверка позиции: {lst[result]}")

