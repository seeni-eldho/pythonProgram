#lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# a=[]
# for i in lst:
#     if i not in a:
#         a.append(i)
# print(a)
# a=[]
# a=[i for i in lst if i not in a.append(i) ]
# print(a)

#
# def add(a,b):
#     print('addition=',a+b)
# def sub (a, b):
#     print('subtraction=', a - b)
# def mul(a, b):
#     print('multiplication=', a * b)
# def div(a, b):
#     print('division=', a / b)
# def floor(a, b):
#     print('floor division=', a // b)
# def exp(a,b):
#     print('exponent=', a ** b)
#
# choice=int(input('enter the choice'))
# if  (choice>0 and choice<7):
#  n1=int(input('enter the first number'))
#  n2=int(input('enter the second number'))
#  if choice==1:
#     add(n1,n2)
#  if choice==2:
#     sub(n1,n2)
#  if choice==3:
#     mul(n1,n2)
#  if choice==4:
#     div(n1,n2)
#  if choice==5:
#     floor(n1,n2)
#  if choice==6:
#     exp(n1,n2)
# else:
#  print('invalid')
# str=input('enter the string')
# str1=""
# for i in str:
#     if i not in 'aeiou':
#      str1+=i
# print(str1)
# l1=[3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,34,289,49,12,63,976]
# l1.sort()
# print('second largest element',l1[-2])
#append
# l1=[1,2,3,4]
# l2=[4,5,6]
# l1.extend(l2)
# def prim(a,b):
#     s=0
#     for i in range(a,b):
#        # fl=0
#         for j in range(2,i):
#           if (i%j)==0:
#               break
#         else:
#            print(i)
#            s=s+i
#     return s
#
#
# print(prim(1,50))


#
# a=[1,2,3,45,6,7,33,11,77,9,0,5]
# b=[3,77,0,5,33,6,22,5,90,32,56,78,98,54,67,11,34,88]
# for i in a:
#     for j in b:
#         if i==j:
#             print(i)

# a=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# b={}
# b.union(a)
# b=[i for i in a for jwhile i==j print i]



# # a=int(i

# for i in range(1,100):
#     if i%5==0:
#         print(i)
a=[i for i in range(101) if(i%5==0) ]
print(a)
# for i in range(1,5):
#   for l in range(i):
#     k=1
#     for j in range(l):
#         print(k,end='')
#     print()
#     k+=1

# def prime(a,b):
#  global s
#  s=0
#  for i in range(a,b):
#    for j in range(2,i):
#      if i%j==0:
#       break
#    else:
#        print(i,end=' ')
#        s+=i
#  return(s)
#
# prime(1,50)
# print('sum',s)
# l=0
# for l in range(1,5):
#  if (l%2!=0):
#     for i in range(5):
#      for j in range(i):
#         print(l,end=' ')
#
#      print()
#  else :
#         for i in range(4,0,-1):
#             for j in range(i):
#                 print(l, end=' ')
#
#             print()
# ls=[1,2,3,4,4,3,6,8,7,0]
# print(list(set(ls)))
