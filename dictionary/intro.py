# dict={'name':'seeni','age':35,'class':'python'}
# print(dict)
# print(type(dict))
# print(dict['name'])
# dict['age']=8
# print(dict)
# dict['school']='seventhday'
# print(dict)
# dict.update({'name':'eldho'})
# print(dict)
# del dict['name']
# print(dict)
# del dict
# print(dict)

# dict={1:2,3:4,5:6}
# a=int(input('enter the key'))
# if a in dict:
#     print('found')
# else:
#     print('not found')
# dict={'name':'seeni','class':7,'school':'senenth'}
# a=input('enter the string')
# if a in dict:
#     print('found')
# else:
#     print('not found')
# a='hello world'
# b=a.split(' ')
# print(b)
# keys are unique,values duplication allowed
# keys same type
# mutable
# nesting possible
# nesting possible
# d={1:'hello',2:{1,2,3,4}}
# print(d)
#a={'hello hai hello  hi hai hai '}


# count={}
# b=input('enter')
# words=b.split(' ')
# print(words)
# for i in words:
#     if i not in count:
#         count.update({i:1})
#     else:
#       val=int(count[i])
#       val+=1
#       count.update({i:val})
# print(count)

l1=[(1,'seeni',20,25000),(2,'sibi',30,10000),(3,'sincy',40,40000)]
print(l1)
for i in l1:
    if i[-1]>=15000:
      print(i)
