list = input('a')
list = list.casefold()
for i in list:
    each = 0
    if list.count(i) > each:
        each = list.count(i)
        name = i
    else:
        continue
print("次数最多的是{0},次数是{1}".format(name,each))

