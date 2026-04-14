import functools
import json
import xml.etree.ElementTree as ET
from typing import Any
import yaml


def formatting(format_type):
    """
    Decorator for converting the return value of a function to the specified format.

    Args:
        format_type: Format type ('json', 'xml', 'yaml'). If None - JSON

    Returns:
        Decorated function
    """
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)

            output_frmt = format_type.lower() if format_type else 'json'

            if output_frmt == "json":
                return json.dumps(result, ensure_ascii=False, indent=2)
            elif output_frmt == "xml":
                return get_xml(result, "document")
            elif  output_frmt == "yaml":
                return yaml.dump(result, allow_unicode=True, default_flow_style=False)
            else:
                raise ValueError("Неподдерживаемый формат")

        return wrapper
    return decorator


def get_xml(input_data: Any, name: str) -> str:
    """
    Converts a Python object to an XML string.

    Args:
        input_data: Data to convert
        name: Name of the root element

    Returns:
        XML string
    """

    def create_xml(el_name: str, value: Any):
        """
        Recursively creates an XML element from a Python object.

        Args:
            el_name (str): The name of the XML tag for the element to be created
            value (Any): The data to be converted

        Returns:
             xml.etree.ElementTree.Element: The created XML element
              with nested child elements
        """

        elem = ET.Element(el_name)

        if isinstance(value, dict):
            for key, val in value.items():
                sub_el = create_xml(key, val)
                elem.append(sub_el)
        elif isinstance(value, list):
            for item in value:
                item_el = create_xml("item", item)
                elem.append(item_el)
        else:
            elem.text = str(value)

        return elem

    root = create_xml(name, input_data)
    return ET.tostring(root, encoding='unicode', method='xml')

#Examples
@formatting("xml")
def get_book():
    return {
        "book": {
            "name": "Капитанская дочка",
            "author": "Пушкин",
            "year": 1836
        }
    }

@formatting("json")
def get_flowers():
    return {
        "quantity": 19,
        "type": "Лилии",
        "price": 7777,
        "color": "белые"
    }

@formatting("yaml")
def get_restaurant_menu():
    return {
        "ресторан": "Уютное кафе",
        "адрес": "ул.Ленина, 15",
        "телефон": "+7(999)123-45-67",
        "меню": {
            "супы": [
                {"название": "Борщ", "цена": 250, "вес": 300},
                {"название": "Солянка", "цена": 270, "вес": 300},
            ],
            "горячее": [
                {"название": "Паста Карбонара", "цена": 420, "вес": 300},
                {"название": "Рис с овощами", "цена": 320, "вес": 250}
            ],
        }
    }


print("Пример 1: XML")
print(get_book())

print("Пример 2: JSON")
print(get_flowers())

print("Пример 3: YAML")
print(get_restaurant_menu())
