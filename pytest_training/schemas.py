USER_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "required": [
        "id",
        "name",
        "username",
        "email",
        "phone",
        "website",
        "address",
        "company",
    ],
    "properties": {
        "id": {"type": "integer", "minimum": 1},
        "name": {"type": "string", "minLength": 1},
        "username": {"type": "string", "minLength": 1},
        "email": {"type": "string", "minLength": 1},
        "phone": {"type": "string", "minLength": 1},
        "website": {"type": "string", "minLength": 1},
        "address": {
            "type": "object",
            "required": ["street", "suite", "city", "zipcode", "geo"],
            "properties": {
                "street": {"type": "string"},
                "suite": {"type": "string"},
                "city": {"type": "string"},
                "zipcode": {"type": "string"},
                "geo": {
                    "type": "object",
                    "required": ["lat", "lng"],
                    "properties": {
                        "lat": {"type": ["string", "number"]},
                        "lng": {"type": ["string", "number"]},
                    },
                },
            },
        },
        "company": {
            "type": "object",
            "required": ["name", "catchPhrase", "bs"],
            "properties": {
                "name": {"type": "string"},
                "catchPhrase": {"type": "string"},
                "bs": {"type": "string"},
            },
        },
    },
    "additionalProperties": False,
}


USERS_LIST_SCHEMA = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "array",
    "items": USER_SCHEMA,
}