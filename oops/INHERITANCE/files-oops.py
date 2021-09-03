# count={}
# f=open('f1','r')
# for i in f:
#     w=i.split(' ')
#     print(w)
#     print()
#     for i in w:
#         if i not in count:
#             count.update({i:1})
#         else:
#             val=int(count[i])
#             val+=1
#             count.update({i:val})
# print(count)
count=0
f=open('student','r')
for i in f:
    w=i.split(' , ')
    print(w)
    print()
#     for i in w:
#         if i not in count:
#             count.update({i:1})
#         else:
#             val=int(count[i])
#             val+=1
#             count.update({i:val})
# print(count)
