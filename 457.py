class Fragment:
    def __init__(self, name):
        self.length = 0
        self.doc_list = []
        self.name = name

    def doc_list_create(self):
        with open(self.name, encoding='utf-8') as f:
            self.doc_list = (f.readlines())
            self.length = len(self.doc_list)

def write_file(Fragment):
    with open("4.txt", "a") as f:
        f.write(Fragment.name + '\n')
        f.write(str(Fragment.length) + '\n')
        for item in Fragment.doc_list:
            f.write(item)
        f.write('\n')
        f.write('\n')

fragment1 = Fragment("1.txt")
fragment1.doc_list_create()

fragment2 = Fragment("2.txt")
fragment2.doc_list_create()

fragment3 = Fragment("3.txt")
fragment3.doc_list_create()

a = min(fragment1.length, fragment2.length, fragment3.length)
b = max(fragment1.length, fragment2.length, fragment3.length)
dict_file = {fragment1 : fragment1.length, fragment2 : fragment2.length, fragment3 : fragment3.length}
for key, value in dict_file.items():
    if value == a:
        write_file(key)
    elif a < value < b:
        write_file(key)
    elif value == b:
        write_file(key)