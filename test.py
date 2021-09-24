import unittest
from yandex import NewFolder


class FolderCreate(unittest.TestCase):
    def test_folder_create(self):
        self.assertEqual(NewFolder.folder_create(NewFolder, "new_folder"), 'Папка создана 201')


if __name__ == '__main__':
    unittest.main()
