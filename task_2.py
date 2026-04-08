def sum_numbers(interval_1: int , interval_2: int,
                divisor_1: int, divisor_2: int) -> int:
    """
    Finds the sum of natural numbers in the interval [a; b],
    multiples of  c and d.

    Args:
        interval_1 (int): The beginning of the interval
        interval_2 (int): End of the interval
        divisor_1 (int): The first divisor
        divisor_2 (int): The second divisor

    Returns:
        int: The sum of the multiples of c and d
    """

    numbers = filter(
        lambda target_number: target_number % divisor_1 == 0 and
        target_number % divisor_2 == 0, range(interval_1, interval_2 + 1)
    )

    return sum(numbers)


def main():
    try:
        integral_1 = int(input("Введите начало интервала: "))
        integral_2 = int(input("Введите конец интервала: "))
        divisor_1 = int(input("Введите 1й делитель: "))
        divisor_2 = int(input("Введите 2й делитель: "))

        if integral_1 > integral_2:
            print("Ошибка! Начало интервала должно быть меньше конца")
        elif divisor_1 <= 0 or divisor_2 <= 0:
            print("Ошибка! Делители должны быть натуральными числами")
        else:
            print(sum_numbers(integral_1, integral_2, divisor_1, divisor_2))

    except ValueError:
        print("Ошибка! Введите целые числа")


if __name__ == "__main__":
    main()
  
