def count_numbers(interval_1: int , interval_2: int, divisor: int,
                  last_digit: int) -> int:
    """
    Finds the number of natural numbers in the interval [a; b],
    non-multiples of c and ending with the digit d.

    Args:
        interval_1 (int): The beginning of the interval
        interval_2 (int): End of the interval
        divisor (int): Divisor
        last_digit (int): The last digit

    Returns:
        int: The number of matching numbers
    """

    numbers = map(
        lambda target_num: 1 if (target_num % divisor != 0 and
                                 target_num % 10 == last_digit) else 0,
        range(interval_1, interval_2 + 1)
    )

    return sum(numbers)


def main() -> None:
    try:
        interval_1 = int(input("Введите начало интервала: "))
        interval_2 = int(input("Введите конец интервала: "))
        divisor = int(input("Введите делитель: "))
        last_digit = int(input("Введите последнюю цифру: "))

        if interval_1 > interval_2:
            print("Ошибка! Начало интервала должно быть меньше конца")
        elif interval_1 <= 0 or interval_2 <= 0:
            print("Ошибка! Интервал должен быть натуральным числом")
        elif divisor <= 0:
            print("Ошибка! Делитель должен быть натуральным числом")
        elif last_digit < 0 or last_digit > 9:
            print("Ошибка! Последняя цифра должна быть от 0 до 9")
        else:
            print(count_numbers(interval_1, interval_2, divisor, last_digit))

    except ValueError:
        print("Ошибка! Введите целые числа")


if __name__ == "__main__":
    main()
  
