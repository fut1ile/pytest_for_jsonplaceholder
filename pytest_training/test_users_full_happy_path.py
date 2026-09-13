import pytest
import basic_checks
from jsonschema import validate, ValidationError
import schemas

# полное тестирование Happy Path 
ADDRESS_FIELDS = ["street", "suite", "city", "zipcode", "geo"]
USER_TOP_LEVEL_FIELDS = ["id","name","username","email","phone","website","address","company"]
GEO_FIELDS = ["lat", "lng"]
COMPANY_FIELDS = ["name", "catchPhrase", "bs"]

def assert_user_full_structure(user, user_id):
    # проверка верхних полей
        for field in USER_TOP_LEVEL_FIELDS:
            assert field in user, f"У юзера {user_id} отсутствует поле '{field}'"
    
        # проверка id
        basic_checks.check_int(user["id"], "id", user_id)    
        assert user["id"] >= 1
    
        # проверки name, username, email, phone, website
        basic_checks.check_string(user["name"], "name", user_id)
        basic_checks.check_string(user["username"], "username", user_id)
        basic_checks.check_string(user["email"], "email", user_id)
        basic_checks.check_string(user["phone"], "phone", user_id)
        basic_checks.check_string(user["website"], "website", user_id)
    
        # валидация name/emails
        basic_checks.check_name(user)
        basic_checks.check_email(user)
    
        # проверки address
        address = user["address"]
        assert isinstance(address, dict), (
            f"У юзера {user_id} 'address' должен быть объектом, "
            f"а пришел {type(address).__name__}"
        )
    
        for field in ADDRESS_FIELDS:
            assert field in address, f"У юзера {user_id} в address нет поля '{field}'"
            basic_checks.check_string(address["street"], "address.street", user_id)
            basic_checks.check_string(address["suite"], "address.suite", user_id)
            basic_checks.check_string(address["city"], "address.city", user_id)
            basic_checks.check_string(address["zipcode"], "address.zipcode", user_id)
    
        # проверки geo
        geo = address["geo"]
        assert isinstance(geo, dict), (
            f"У юзера {user_id} 'address.geo' должен быть объектом, "
            f"а пришел {type(geo).__name__}"
        )
    
        for field in GEO_FIELDS:
            assert field in geo, f"У юзера {user_id} в address.geo нет поля '{field}'"
    
        basic_checks.check_float_or_string_latlng(geo["lat"], "address.geo.lat", user_id)
        basic_checks.check_float_or_string_latlng(geo["lng"], "address.geo.lng", user_id)
    
        # проверки company 
        company = user["company"]
        assert isinstance(company, dict), (
            f"У юзера {user_id} 'company' должен быть объектом, "
            f"а пришел {type(company).__name__}"
        )
    
        for field in COMPANY_FIELDS:
            assert field in company, f"У юзера {user_id} в company нет поля '{field}'"
    
        basic_checks.check_string(company["name"], "company.name", user_id)
        basic_checks.check_string(company["catchPhrase"], "company.catchPhrase", user_id)
        basic_checks.check_string(company["bs"], "company.bs", user_id)

# основной тест на список пользователей /users
@pytest.mark.parametrize("user_id", [1, 2, 5, 10])
def test_get_users_full_structure(api_client, user_id):
    response = api_client("GET", "/users")
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list), f"Ожидался список а пришел {type(data).__name__}"
    assert len(data) == 10

    user = next(u for u in data if u["id"] == user_id)
    assert_user_full_structure(user, user_id)

# тест на один ресурс
@pytest.mark.parametrize("user_id", [1, 3, 7])
def test_get_single_user_full_structure(api_client, user_id):
    response = api_client("GET", f"/users/{user_id}")
    assert response.status_code == 200
    user = response.json()

    assert isinstance(user, dict), f"Ожидался объект, а пришел {type(user).__name__}"
    assert user["id"] == user_id

    assert_user_full_structure(user, user_id)

def test_get_users_schema_validation(api_client):
    response = api_client("GET", "/users")
    assert response.status_code == 200
    data = response.json()

    try:
        validate(instance=data, schema=schemas.USERS_LIST_SCHEMA)
    except ValidationError as e:
        pytest.fail(f"JSON Schema валидация не прошла: {e.message}")

    