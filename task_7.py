import json
from typing import Any


def to_json(func):
    """
    A decorator that converts the value returned
    by the function to JSON format.

    Args:
        func: A decorated function

    Returns:
        wrapper: Wrapper function
    """

    def wrapper(*args: Any, **kwargs: Any) -> str:
        result = (func(*args, **kwargs))
        return json.dumps(result, ensure_ascii=False)
    return wrapper

#Examples
@to_json
def convert_text(text: str) -> str:
    return text


@to_json
def convert_dict() -> dict:
    return {"name": "Лиза", "age": 18, "weight": 50}


@to_json
def convert_tuple() -> tuple:
    return (5, 9, 25)

print(convert_text('i love friday'))
print(convert_dict())
print(convert_tuple())
