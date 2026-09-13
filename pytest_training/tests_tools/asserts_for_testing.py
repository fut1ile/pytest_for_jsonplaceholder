from . import basic_checks

# валидация Happy Path для GET/users
def assert_user_full_structure(user, user_id):
    ADDRESS_FIELDS = ["street", "suite", "city", "zipcode", "geo"]
    USER_TOP_LEVEL_FIELDS = ["id","name","username","email","phone","website","address","company"]
    GEO_FIELDS = ["lat", "lng"]
    COMPANY_FIELDS = ["name", "catchPhrase", "bs"]
    # проверка верхних полей
    for field in USER_TOP_LEVEL_FIELDS:
        assert field in user, f"У юзера {user_id} отсутствует поле '{field}'"

    # проверка id
    basic_checks.check_int(user["id"], "id", context=f"user_id={user_id}")
    assert user["id"] >= 1

    # проверки name, username, email, phone, website
    basic_checks.check_string(user["name"], "name", context=f"user_id={user_id}")
    basic_checks.check_string(user["username"], "username", context=f"user_id={user_id}")
    basic_checks.check_string(user["email"], "email", context=f"user_id={user_id}")
    basic_checks.check_string(user["phone"], "phone", context=f"user_id={user_id}")
    basic_checks.check_string(user["website"], "website", context=f"user_id={user_id}")

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
    basic_checks.check_string(address["street"], "address.street", context=f"user_id={user_id}")
    basic_checks.check_string(address["suite"], "address.suite", context=f"user_id={user_id}")
    basic_checks.check_string(address["city"], "address.city", context=f"user_id={user_id}")
    basic_checks.check_string(address["zipcode"], "address.zipcode", context=f"user_id={user_id}")

    # проверки geo
    geo = address["geo"]
    assert isinstance(geo, dict), (
        f"У юзера {user_id} 'address.geo' должен быть объектом, "
        f"а пришел {type(geo).__name__}"
    )

    for field in GEO_FIELDS:
        assert field in geo, f"У юзера {user_id} в address.geo нет поля '{field}'"

    basic_checks.check_float_or_string_latlng(geo["lat"], "address.geo.lat", context=f"user_id={user_id}")
    basic_checks.check_float_or_string_latlng(geo["lng"], "address.geo.lng", context=f"user_id={user_id}")

    # проверки company
    company = user["company"]
    assert isinstance(company, dict), (
        f"У юзера {user_id} 'company' должен быть объектом, "
        f"а пришел {type(company).__name__}"
    )

    for field in COMPANY_FIELDS:
        assert field in company, f"У юзера {user_id} в company нет поля '{field}'"

    basic_checks.check_string(company["name"], "company.name", context=f"user_id={user_id}")
    basic_checks.check_string(company["catchPhrase"], "company.catchPhrase", context=f"user_id={user_id}")
    basic_checks.check_string(company["bs"], "company.bs", context=f"user_id={user_id}")

# валидация Happy Path для GET/posts
def assert_posts_full_structure(data):
    POSTS_FIELDS = ["userId", "id", "title", "body"]
    for el in data:
        post_id = el["id"]
        for field in POSTS_FIELDS:
            assert field in el, f"У id {post_id} отсутствует поле '{field}'"

        basic_checks.check_int(el["userId"], "userId", context=f"id={post_id}")
        basic_checks.check_int(el["id"], "id", context=f"id={post_id}")
        basic_checks.check_string(el["title"], "title", context=f"id={post_id}")
        basic_checks.check_string(el["body"], "body", context=f"id={post_id}")