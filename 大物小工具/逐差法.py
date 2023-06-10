counts = 0
list1 = []
list2 = []
temp = eval(input('输入系数'))
while counts != temp:
   x,y = eval(input(''))
   num = y -x
   list1.append(num)
   counts += 1
   print(num)
def sum_list(*args):  # 计算列表元素求和
   def process(i):
      if i == 1:
         return args[0]
      else:
         return process(i - 1) + args[i - 1]

   return process
Temp = len(list1)
a = sum_list(*list1)
pj = a(Temp)/5
print('平均值是{}'.format(pj))
for i in list1:
   list2.append((i-pj)**2)
Sc = (sum(list2)/(temp-1))**(1/2)
print('标准差是{}'.format(Sc))
s = 3*Sc
print('{},{}'.format(pj-s,pj+s))