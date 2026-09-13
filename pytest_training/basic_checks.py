import re

NAME_WORD = r"[A-Za-z]+(?:[-'][A-Za-z]+)*\.?"
NAME_PATTERN = rf"{NAME_WORD}(?: {NAME_WORD})+"
EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"

def check_name(data):
    name = data.get("name")
    assert isinstance(name, str), f"name должен быть строкой, а не {type(name).__name__}"
    assert name.strip() != "", "name не должен быть пустым"
    assert name == name.strip(), f"name='{name}' содержит пробелы по краям"
    assert re.fullmatch(NAME_PATTERN, name), f"name='{name}' не похоже на имя человека"

def check_email(data):
    email = data.get("email")

    assert isinstance (email, str), f"email должен быть строкой, а не {type(email).__name__}"
    assert re.fullmatch(EMAIL_PATTERN, email), \
        f"email='{email}' не похож на корректный email"