# list1=[1,2,3,4,1,2,7,8]
# print(list1)
#1.keeping order
#2.support duplicate elements
#3.heterogeneous
#4.nesting possible
#5.list is mutable
# list2=[1,'hello',8.2,True]
# print(list2)
# l1=[]
# l1.append(8)
# l1.append('hello')
# print(l1)
# a=int(input('enter the limit'))
# l1=[]
# for i in range(a):
#     b=input('enter the number')
#     l1.append(b)
# print(l1)
# l1=[1,2,[3,4,[5,6]]]
# print(l1)

# list=[1,2,3]
# list.append(6)
# list.remove(3)
# list.clear()
# del list
# print(list)
# a=[1,2,3,4]
# b=[]
# for i in a:
#    b.append(i*i)
# print(b)
# a = [1, 2, 3, 4, 5, 6]
# def list(a):
#  b=int(input('enter the element'))
#  if b in a:
#     print('not')
#  else:
#    print('found')

##list(a)
# a=[1,2,3,4,5]
# def sum
# s=0
# for i in a:
#   s=s+i
# print('sum',s)
# l1=[1,2,3,4]
# print(l1[-1])
# b=[]
# a=[5,8,3,7]
# while  a:
#   min =a[0]
#   for j in a:
#     if j< min:
#        min =j
#   b.append(min)
#   a.remove(min)
#
# print(b)
# print(a)

# l1=[1,2,3,1[1:3])
# print(l1[-4:-1])
# print(l1[:4])
# print(l1[3:])
# print(l1[:])
# print(l1[4,5,6,7]
# print(l::-1])
# a=[1,2,31,3,4,5,4,31]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
#     else:
#         print(i)



# a.sort()
# print(a)
# print(a[0])
# print(a[-1])
# a=[1,2,3,4]
# b=[]
# for i in a:
#     b.append(i*5)
# print(b)
# a=[1,2,3,4]
# b=[i*5 for i in a]
# print(b)

# for i in a:
#   #if i%2==0:
#     b.append(while i%2==0)
#   else:
#       c.append(i)
# #c.append(for i in a if(i%2!=0))
# print('even',b)
# print('odd',c)
# a=[1,2,3,4,5]
# b=[i for i in a if i%2==0]
# print('even',b)
# c=[i for i in a if i%2!=0]
# print('odd',c)

# even=[i for i in range(100,200) if i%2==0]
# print('even',even)
# a=[11,2,1,8,4,5]
# max=0
# min=a[0]
# for i in a:
#      if i>max:
#        max = i
#      if i<min:
#          min=i
# print(max)
# print(min)
# a=[1,2,3,4,55,100]
# s=1
# for i in a:
#     s=s*i
# # print(s)

# num=int(input("eneter your number"))
# lst.sort()
#
# low=0
# upper=len(lst)-1
#
# mid=(low+upper)//2
#
# if(num>lst[mid]):
#     low=mid+1
#     found()
# elif(num<lst[mid]):
#     upper=mid-1
#     found()
# else:
#     print("element found")
#
# def found():
#     flag=0
#     for i in range(low,upper):
#         if (num == i):
#             flag = 1
#             break
#         else:
#             pass
#     if (flag > 0):
#         print("number found")
#     else:
# #         print("number not found")
# lst=[2,10,4,5,1,15,7,9]
#
#     num = int(input("enter your number"))
#     lst.sort()
#     print(lst)
#     low=0
#     upper=len(lst)-1
#     mid=(low+upper)//2
#     if (num>lst[mid]):
#         low=mid+1
#     elif (num<lst[mid]):
#         upper=mid-1
#
#     # else:
#     #     print("element found")
#
#     flag=0
#     for i in range(low,upper):
#             if (num == i):
#                 flag = 1
#                 break
#             else:
#                 pass
#     if (flag > 0):
#             print("number found")
#     else:
#             print("number not found")
# found()
def bin(l1,key):
    low=0
    high=len(l1)-1
    found=False
    while low<=high and found==False :
        mid=(low+high)//2
        if key==l1[mid]:
            found=True
        elif key>l1[mid]:
            low=mid+1
        else:
            high=mid-1
    if found==True:
        print('found')
    else :
        print('not found')

l1=[23,56,3,7,9]
l1.sort()
print(l1)
key=int(input('number'))
bin(l1,key)
#to add number to a list use extend
# a=[1,3,'wer',7]
# c=[]
# b=[1,2,6,7]
# a.extend(b)
#
# print(a)











a='seeni'
print(a)
b=''
b+=a
#for i in a:
    b


