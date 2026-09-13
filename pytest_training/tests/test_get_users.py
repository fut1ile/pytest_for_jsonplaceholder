import pytest
from jsonschema import validate, ValidationError
from tests_tools import schemas
from tests_tools import asserts_for_testing

# основной тест Happy Path /users
def test_get_users_full_structure(api_client):
    response = api_client("GET", "/users")
    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list), f"Ожидался список а пришел {type(data).__name__}"

    for user in data:
        asserts_for_testing.assert_user_full_structure(user, user["id"])

# тест на один ресурс
@pytest.mark.parametrize("user_id", [1, 3, 7])
def test_get_single_user_full_structure(api_client, user_id):
    response = api_client("GET", f"/users/{user_id}")
    assert response.status_code == 200
    user = response.json()

    assert isinstance(user, dict), f"Ожидался объект, а пришел {type(user).__name__}"
    assert user["id"] == user_id

    asserts_for_testing.assert_user_full_structure(user, user_id)

# тест schema validation
def test_get_users_schema_validation(api_client):
    response = api_client("GET", "/users")
    assert response.status_code == 200
    data = response.json()

    try:
        validate(instance=data, schema=schemas.USERS_LIST_SCHEMA)
    except ValidationError as e:
        pytest.fail(f"JSON Schema валидация не прошла: {e.message}")

@pytest.mark.parametrize("user_id", [9999, 0, -1])
def test_nonexistent_user_returns_empty_object(api_client, user_id):
    response = api_client("GET", f"/users/{user_id}")
    assert response.status_code == 404
    assert response.json() == {}, f"Ожидался пустой объект, пришло {response.json()}"

