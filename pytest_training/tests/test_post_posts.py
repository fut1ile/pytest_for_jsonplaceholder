from tests_tools import basic_checks
from tests_tools import asserts_for_testing

def test_post_posts_creates(api_client):
    payload = {
        "title": "foo",
        "body": "bar",
        "userId": 1,
    }
    response = api_client("POST", "/posts", json=payload)
    assert response.status_code == 201

    data = response.json()
    assert "id" in data, "В ответе отсутсвует id"
    basic_checks.check_int(data["id"])
    assert data["title"] == payload["title"]
    assert data["body"] == payload["body"]
    assert data["userId"] == payload["userId"]
    asserts_for_testing.assert_posts_full_structure(data)
