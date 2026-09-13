from tests_tools import asserts_for_testing

def test_get_posts_full_structure(api_client):
    response = api_client("GET", "/posts")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list), f"Ожидался список а пришел {type(data).__name__}"
    asserts_for_testing.assert_posts_full_structure(data)
