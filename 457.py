class Text:
    def __init__(self, name):
        self.length = 0
        self.doc_list = []
        self.name = name
    def doc_list_create(self):
        with open(self.name, encoding='utf-8') as f:
            self.doc_list = (f.readlines())
            self.length = len(self.doc_list)

    def __lt__(self, other):
        return self.length < other.length

    def write_file(self):
        a = min(fragment1.length, fragment2.length, fragment3.length)
        with open("4.txt", "w") as f:
            if self.length == a:
                f.write(self.name + '\n')
                f.write(str(self.length) + '\n')
                for item in self.doc_list:
                    f.write(item)

fragment1 = Text("1.txt")
fragment1.doc_list_create()

fragment2 = Text("2.txt")
fragment2.doc_list_create()

fragment3 = Text("3.txt")
fragment3.doc_list_create()




# print(a)







# print(fragment1.doc_list)
# print(fragment1.length)
# print(fragment3.name)




# with open('1.txt', encoding='utf-8') as f:
#     list1 = (f.readlines())
#
# with open('2.txt', encoding='utf-8') as f:
#     list2 = (f.readlines())
#
# with open('3.txt', encoding='utf-8') as f:
#     list3 = (f.readlines())
#     # print(len(list3))
# # with open('4.txt', 'w') as f:
# #     f.write()
# a = min(len(list1), len(list2), len(list3))
# b = max(len(list1), len(list2), len(list3))
# if len(list1) == a:
#     print(list1)



#
# # print(list3)