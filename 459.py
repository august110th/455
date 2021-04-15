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
        with open("to_upload.txt", "rb") as f:
            response = requests.put(result, files={"file": f})
        return f"Файл загружен на яндекс диск! Код: {response.status_code}"

if __name__ == "__main__":
  uploader = YaUploader("токен")
  print(uploader.upload("to_upload.txt"))