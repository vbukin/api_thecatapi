import pytest
from service.client import Client
from endpoints.votes import Votes


@pytest.fixture
def get_id():
    with open('utils/votes.txt', 'r') as file:
        return int(file.read())


@pytest.fixture
def input_value():
   input = 39
   return input