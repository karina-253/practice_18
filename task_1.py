def count_chars(target_str: str, position_1: int , position_2: int) -> int:
    """
    Counts the number of uppercase characters
    in the specified range of a string.

    Args:
        target_str (str): Source string for analysis
        position_1 (int): Initial position (numbering from 1)
        position_2 (int): Final position
    Returns:
        int: The number of uppercase characters in the specified range
    """

    chars_upper = filter(
        lambda char: char.isupper(),
        target_str[position_1 - 1:position_2]
    )

    return len(list(chars_upper))


def main():
    try:
        input_str = input("Введите строку: ")
        start = int(input("Начальная позиция: "))
        end = int(input("Конечная позиция: "))

        if start < 1 or end < 1:
            print("Ошибка! Индексы должны быть положительными числами")
        elif start > end:
            print("Ошибка! Начальная позиция должна быть меньше конечной")
        else:
            print(count_chars(input_str, start, end))

    except ValueError:
        print("Ошибка! Введите целые числа")


if __name__ == "__main__":
    main()
