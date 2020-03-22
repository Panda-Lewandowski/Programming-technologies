import random

class Product:
    def __init__(self, name, amount, cost):
        self._name = name 
        self._amount = amount
        self._cost = cost

    def get_total_cost(self):
        return self._amount * self._cost

    def __str__(self):
        return f"{self._name} ({self._amount} шт. по {self._cost} руб.)"


if __name__ == "__main__":
    n = int(input("Введите общее количество наименований в магазине: "))
    warehouse = []
    total_cost = 0

    for i in range(n):
        p = Product("Товар " + str(i + 1), 
                                random.randint(1, 10), 
                                random.randint(10, 100))
        total_cost += p.get_total_cost()
        warehouse.append(p)
        print(p)

    print(f"Суммарная стоимость всех товаров: {total_cost} руб.")
    print("Массив объектов: ", warehouse)

    