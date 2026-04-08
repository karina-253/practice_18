import math
from functools import reduce


def composition_numbers(interval_1: int , interval_2: int, divisor: int) -> int:
    """
    Finds the product of natural numbers in the interval [a; b]
    that are perfect squares and multiples of c.

    Args:
        interval_1 (int): Start of the interval
        interval_2 (int): End of the interval
        divisor (int): Divisor

    Returns:
        int: Product of suitable numbers
    """
    numbers = filter(
        lambda target_num: math.isqrt(target_num) ** 2 == target_num
                           and target_num % divisor == 0,
        range(interval_1, interval_2 + 1)
                     )

    result = reduce(lambda target_num, next_num: target_num * next_num, numbers, 1)

    return result


def main() -> None:
    try:
        interval_1 = int(input("Введите начало интервала: "))
        interval_2 = int(input("Введите конец интервала: "))
        divisor = int(input("Введите делитель: "))

        if interval_1 > interval_2:
            print("Ошибка! Начало интервала должно быть меньше конца")
        elif interval_1 <= 0 or interval_2 <= 0:
            print("Ошибка! Интервал должен быть натуральным числом")
        elif divisor <= 0:
            print("Ошибка! Делитель должен быть натуральным числом")
        else:
            print(composition_numbers(interval_1, interval_2, divisor))

    except ValueError:
        print("Ошибка! Введите целые числа")


if __name__ == "__main__":
    main()
  
