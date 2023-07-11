import requests


class Client:
    def __init__(self):
        self.protocol = 'https://'
        self.host = 'api.thecatapi.com'
        self.version = '/v1'
        self.key = 'x-api-key'
        self.value = 'DEMO-API-KEY'
        self.url = self.protocol + self.host + self.version

    def get(self, path, payload=None):
        my_headers = self.get_headers()
        return requests.get(url=f"{self.url}{path}",
                            params=payload,
                            headers=my_headers,
                            verify=False
                            )

    def post(self, path, body=None):
        my_headers = self.get_headers()
        print(f"{self.url}{path}")
        return requests.post(url=f"{self.url}{path}",
                             headers=my_headers,
                             json=body,
                             verify=False
                             )

    def delete(self, path):
        my_headers = self.get_headers()
        return requests.delete(url=f"{self.url}{path}",
                             headers=my_headers,
                             verify=False
                             )

    def get_headers(self):
        return {self.key: self.value}
