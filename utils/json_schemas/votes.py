votes_json_schema = schema = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "user_id": {"type": "string"},
        "image_id": {"type": "string"},
        "sub_id": {"type": ["string", "null"]},
        "created_at": {"type": "string"},
        "value": {"type": "integer"},
        "country_code": {"type": ["string", "null"]},
        "image": {
            "type": "object",
            "properties": {
                "id": {"type": "string"},
                "url": {"type": "string"}
            },
            "required": ["id", "url"]
        }
    },
    "required": ["id", "user_id", "image_id", "created_at", "value", "image"]
}