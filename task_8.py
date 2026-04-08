import functools
from datetime import datetime
from typing import Any


def get_logs(log_file: str):
    """
    A decorator that receives a log file with exceptional situations
    that occurred during the execution of a function, including the date,
    time, and type of the exceptional situation.

    log file (str):  the path to the file for recording logs
    """

    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                return function(*args, **kwargs)
            except Exception as e:
                time_exception = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                type_exception = type(e).__name__

                log_message = (
                    f"[{time_exception}] "
                    f"Exception type: {type_exception} ; "
                    f"Function: {function.__name__} ; "
                    f"Error_message: {e}\n"
                )

                with open(log_file, 'a', encoding='utf-8') as f:
                    f.write(log_message)

                raise
        return wrapper
    return decorator


@get_logs("errors.log")
def get_value(key: dict, value: str) -> Any:
    return key[value]


def main() -> None:
    user = {"name": "Valentina", "age": 43}

    print("Успешный вызов")
    print(f"Результат: {get_value(user, "name")}")

    print("Вызов с ошибкой")
    try:
        get_value(user, "job")
    except KeyError:
        print("Исключение было перехвачено и записано в лог-файл")


if __name__ == "__main__":
    main()
