import os
import random
import jsonschema
from faker import Faker

from service.client import Client
from endpoints.votes import Votes
from config.definitions import ROOT_DIR
from utils.json_schemas.votes import votes_json_schema


def test_get_all():
    client = Client()
    votes = Votes(client)
    result = votes.get()
    result_json = result.json()
    assert result.status_code == 200
    assert type(result_json) is list
    assert len(result_json) > 0


def test_get_one():
    client = Client()
    votes = Votes(client)

    result = votes.get()
    result_json = result.json()

    result = votes.get(random.choice(result_json)['id'])
    result_json = result.json()
    print(result_json)

    jsonschema.validate(result_json, votes_json_schema)
    assert result.status_code == 200
    assert type(result_json) is dict
    assert len(result.json()) != 0
    assert type(result_json['id']) is int


def test_post():
    client = Client()
    votes = Votes(client)

    fake = Faker('en_GB')
    body = {"image_id": fake.pystr(),
            "sub_id":  fake.pystr(),
            "value": fake.random_int(min=1, max=20)
            }

    result = votes.post(body)
    result_json = result.json()
    vote_id = result_json['id']
    assert result.status_code == 201
    assert type(result_json) is dict
    assert result_json['message'] == 'SUCCESS'
    assert vote_id is not None
    with open(os.path.join(ROOT_DIR, 'utils', 'votes.txt'), 'w') as file:
        file.write(str(vote_id))


def test_check_posted(get_id):
    client = Client()
    votes = Votes(client)

    result = votes.get(get_id)
    result_json = result.json()

    assert result.status_code == 200
    assert type(result_json) is dict
    assert result_json['id'] == get_id


def test_delete_posted(get_id):
    client = Client()
    votes = Votes(client)

    result = votes.delete(get_id)
    result_json = result.json()
    assert result.status_code == 200
    assert type(result_json) is dict
    assert result_json['message'] == 'SUCCESS'


def test_check_deleted(get_id):
    client = Client()
    votes = Votes(client)

    result = votes.get(get_id)
    # fail here because response contains string 'NOT_FOUND', but we expected dict {"message": "NOT_FOUND"}
    result_json = result.json()
    assert result.status_code == 404
    assert type(result_json) is dict
    assert result_json['message'] == 'SUCCESS'
    assert result_json['status'] == 404
