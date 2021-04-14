import requests
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {"Authorization": f"OAuth {self.token}"}
        params = {"path": disk_file_path, "overwrite": "True"}
        response = requests.get(upload_url, params=params, headers=headers, timeout = 5)
        print(response.json())
        return response.json()

    def upload_file_to_disk(self, disk_file_path, filename):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open("to_upload.txt", "rb"))
        response.raise_for_status()
        if response.status_code == 201:
            print("Succes")

#
if __name__ == '__main__':
    uploader = YaUploader('2303acdcd34a428db8778a708d56a056')
    result = uploader.upload_file_to_disk("upload/to_upload.txt", "to_upload.txt")
# print(result)