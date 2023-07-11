from service.client import Client


class Votes:
    def __init__(self, client: Client):
        self.path = '/votes'
        self.client = client

    def get(self, vote_id=None):
        if vote_id:
            return self.client.get(f'{self.path}/{vote_id}')
        return self.client.get(self.path)

    def post(self, body):
        return self.client.post(self.path, body)

    def delete(self, vote_id):
        return self.client.delete(f'{self.path}/{vote_id}')
