class Text:
    def __init__(self, name):
        self.length = 0
        self.doc_list = []
        self.name = name

    def doc_list_create(self):
        with open(self.name, encoding='utf-8') as f:
            self.doc_list = (f.readlines())
            self.length = len(self.doc_list)

    def write_file(self):
        with open("4.txt", "w") as f:
            f.write(self.name + '\n')
            f.write(str(self.length) + '\n')
            for item in self.doc_list:
                f.write(item)

    def search(self):
        a = min(fragment1.length, fragment2.length, fragment3.length)
        b = max(fragment1.length, fragment2.length, fragment3.length)
        list_file = [fragment1.length, fragment2.length, fragment3.length]
        for self.length in list_file:
            if self.length == a:
                self.write_file()
            if a < self.length < b:
                self.write_file()
            if self.length == b:
                self.write_file()

fragment1 = Text("1.txt")
fragment1.doc_list_create()

fragment2 = Text("2.txt")
fragment2.doc_list_create()

fragment3 = Text("3.txt")
fragment3.doc_list_create()