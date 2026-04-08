import json

def sort_list(information: list) -> list:
    """
    Sorts a list of lists in non-increasing numerical order.

    Args:
        information: A list where each element is [string, number]

    Returns:
        A sorted list
    """
    return sorted(information, key=lambda pair: pair[1], reverse=True)


def main() -> None:
    try:
        json_input = input("Введите список списков в JSON формате: ")
        json_inf = json.loads(json_input)

        for index, item in enumerate(json_inf):
            if not isinstance(item, list) or len(item) != 2:
                print("Ошибка! Элемент должен быть [строка, число]")
                return
            if not isinstance(item[0], str):
                print("Ошибка! Первый элемент должен быть строкой")
                return
            if not isinstance(item[1], (int, float)):
                print("Ошибка! Второй элемент должен быть числом")
                return

        print(sort_list(json_inf))

    except Exception:
        print("Ошибка ввода")


if __name__ == "__main__":
    main()
