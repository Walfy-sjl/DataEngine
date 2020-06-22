
# name = input("What's your name?")
# sum = 100+100
# print ('hello,%s' %name)
# print ('sum = %d' %sum)

score = 75
if score >= 90:
    print('Excellent')
else:
    if score < 60:
        print('Fail')
    else:
        print('Good Job')

sum = 0
for nn in range(10):
    sum = sum + nn

print(sum)

lists = ['a','b','c']
lists.append('d')
print(lists)
print(len(lists))
lists.insert(0,'mm')
lists.pop()
lists.insert(2,'asdads')
print(lists)

tuples = ('A',"B","C")
print(tuples[0])

dictt = {"name":"zhangsan","age":56,"gender":"male"}
dictt['mobile'] = 17621922419
print(dictt)
dictt.pop('mobile')
print("mobile" in dictt)
print(dictt.get('name'))
'''
dict.get(key, default=None)
key -- 字典中要查找的键。
default -- 如果指定键的值不存在时，返回该默认值。
'''

print(dictt.get('age',99))
print(dictt.get('eeee',99))

s = set(['a','b','c'])
s.add('d')
s.add(135)
print(s)
s.remove('c')
print(s)

'''
# 导入一个模块
import model_name
# 导入多个模块
import module_name1,module_name2
# 导入包中指定模块 
from package_name import moudule_name
# 导入包中所有模块 
from package_name import *
'''

str1 = input()
str2 = input()

print("the first string is:"+str1)
print("the second string is:"+str2)



