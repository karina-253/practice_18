def decorator(func):
    """
    A decorator that displays the result of a function,
    having one parameter.

    Args:
        func: A decorated function

    Returns:
        wrapper: Wrapper function
    """

    def wrapper(param):
        result = func(param)
        print(f"{func.__name__}({param}) = {result}")
        return result
    return wrapper


#Example
@decorator
def reverse(s: str) -> str:
    return s[::-1]

print(reverse(input()))
