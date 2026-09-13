import pytest
import basic_checks

REQUIRED_RESPONSE_FIELDS = ["id", "name", "email", "address", "phone"]
REQUIRED_ADDRESS_FIELDS = ["street", "city", "geo"]

def test_get_users(api_client):

    response = api_client("GET", "/users")
    assert response.status_code == 200
    data = response.json()

    # проверка на список юзеров
    assert isinstance(data, list), f"Ожидался список, а пришел {type(data).__name__}"
    assert len(data) == 10
    # проверка уникальности id
    ids = [user["id"] for user in data]
    assert len(set(ids)) == len(ids), f"Обнаружены дубли id: всего {len(ids)} юзеров, уникальных только {len(set(ids))}"

    # проверка структуры каждого юзера
    for user in data:
        # проверки наличия обязательных полей 
        for field in REQUIRED_RESPONSE_FIELDS:
            assert field in user, f"У юзера {user['id']} отсутствуют поле '{field}'"
        # проверки id
        assert isinstance(user["id"], int), f"id должен быть числом, а не {type(user['id']).__name__}"
        assert user["id"] >= 1, f"id={user['id']} должен быть >= 1"
        # проверки email 
        basic_checks.check_email(user)
        # проверки name
        basic_checks.check_name(user)
        # проверка вложенной структуры address
        address = user["address"]
        for field in REQUIRED_ADDRESS_FIELDS:
            assert field in address, f"У юзера {user['id']} в address нет поля '{field}'"
            
