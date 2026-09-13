import re

NAME_WORD = r"[A-Za-z]+(?:[-'][A-Za-z]+)*\.?"
NAME_PATTERN = rf"{NAME_WORD}(?: {NAME_WORD})+"
EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}"

# валидность имени
def check_name(data):
    name = data.get("name")
    assert isinstance(name, str), f"name должен быть строкой, а не {type(name).__name__}"
    assert name.strip() != "", "name не должен быть пустым"
    assert name == name.strip(), f"name='{name}' содержит пробелы по краям"
    assert re.fullmatch(NAME_PATTERN, name), f"name='{name}' не похоже на имя человека"

# валидность email
def check_email(data):
    email = data.get("email")

    assert isinstance (email, str), f"email должен быть строкой, а не {type(email).__name__}"
    assert re.fullmatch(EMAIL_PATTERN, email), \
        f"email='{email}' не похож на корректный email"

# вспомогательные проверки типов
def check_string(value, field_name, user_id):
    assert isinstance(value, str), (
        f"У юзера {user_id} поле '{field_name}' должно быть str, "
        f"а пришло {type(value).__name__}"
    )

def check_int(value, field_name, user_id):
    assert isinstance(value, int), (
        f"У юзера {user_id} поле '{field_name}' должно быть int, "
        f"а пришло {type(value).__name__}"
    )

def check_float_or_string_latlng(value, field_name, user_id):
    assert isinstance(value, (str, float, int)), (
        f"У юзера {user_id} поле '{field_name}' должно быть str/float/int, "
        f"а пришло {type(value).__name__}"
    )