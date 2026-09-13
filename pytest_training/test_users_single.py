import pytest
import requests
import basic_checks

REQUIRED_RESPONSE_FIELDS = ["id", "name", "email", "address", "phone"]
REQUIRED_ADDRESS_FIELDS = ["street", "city", "geo"]

@pytest.mark.parametrize("user_id", [1, 2, 5, 10])
def test_get_single_user(api_client, user_id):
    response = api_client("GET", f"/users/{user_id}")
    assert response.status_code == 200

    user = response.json()

    # базовые проверки
    assert isinstance(user, dict), f"Ожидался объект, а пришел {type(user).__name__}"
    assert user["id"] == user_id

    for field in REQUIRED_RESPONSE_FIELDS:
        assert field in user, f"У юзера {user_id} отсутствует поле '{field}'"

    # тип и диапазон id
    assert isinstance(user["id"], int)
    assert user["id"] >= 1
    # проверки name/email
    basic_checks.check_name(user)
    basic_checks.check_email(user)
    # проверка вложенного address
    address = user["address"]
    for field in REQUIRED_ADDRESS_FIELDS:
        assert field in address, f"У юзера {user_id} в address нет поля '{field}'"

@pytest.mark.parametrize("user_id", [999, 1000, -1, 0])
def test_get_nonexistent_user_returns_404(api_client, user_id):
    response = api_client("GET", f"/users/{user_id}")
    assert response.status_code == 404