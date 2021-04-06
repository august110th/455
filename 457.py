with open('1.txt', encoding='utf-8') as f:
    list1 = (f.readlines())

with open('2.txt', encoding='utf-8') as f:
    list2 = (f.readlines())

with open('3.txt', encoding='utf-8') as f:
    list3 = (f.readlines())
    line_count = 0
    print(len(list3))
with open('4.txt', 'w') as f:
    f.write('2')

# print(list3)