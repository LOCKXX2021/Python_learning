import easygui
box_string = easygui.enterbox('')
type_box = box_string.split('\n')
type_box.remove('类型')
type1_box = []
type2_box = []
counts = 1
for i in type_box:
    if i == "铅钡":
        type1_box.append(counts)
    else:
        type2_box.append(counts)
    counts += 1
box_string = easygui.enterbox('')
type_box = box_string.split('\n')
type_box.remove('表面风化')
un_box = []
counts = 1
for i in type_box:
    if i == "无风化":
        un_box.append(counts)
    counts += 1
type1_unbox = [i for i in type1_box if i in un_box]
type1_fengbox = [i for i in type1_box if i not in un_box]
type2_unbox = [i for i in type2_box if i in un_box]
type2_fengbox = [i for i in type2_box if i not in un_box]
print(type1_unbox)
print(type1_fengbox)
print(type2_unbox)
print(type2_fengbox)

