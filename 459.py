import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {"path": file_path, "overwrite": "True"}
        headers = {"Authorization": f"OAuth {self.token}"}
        response = requests.get(url, params=params, headers=headers)
        result = response.json()["href"]
