import requests

class NewFolder:
    def __init__(self, token: str):
        self.token = token

    def upload(self, path: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        params = {"path": "new_folder"}
        headers = {"Authorization": f"OAuth {self.token}"}
        response = requests.put(url, params=params, headers=headers)
        return f"Папка создана {response.status_code}"

if __name__ == "__main__":
    nf = NewFolder("токен")
    print(nf.upload("new_folder"))
