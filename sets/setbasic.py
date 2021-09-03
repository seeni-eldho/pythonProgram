# a={1,2,3,4}
# print(a)
# print(type(a))

# a=set()
# a.add(1)
# a.add('true')
# print(a)
# print(type(a))
#doesnot keep oder if we write in mixed number result will be in asecning order
#hetrogeneous float int result will be in int
#doesnot support duplicate elements 123342
#result will be 1234
b={1,'hello',5,6,7.5,False}
print(b)

# for i in b:
#     print(i)
# a=set{1,2,3,4}
#
# n=int(input('enter limit'))
# for i in range(n):
#     b=int(input('enter the value'))
#     a.add(b)
#     c.add(a*a)
# print(a)
# print('sq',b)
# s={1,2,3,4}
# s.remove(2)
# s.clear()
# del s
# print(s)


#1.not keeping order
#2.not support duplicate elements
#3.hetrogeneous
#4.mutable
#5.nesting not possible
# a={1,{3,2}}
# print(a)

# a={1,2,3,4,5,6,7,8,9,88,45,67}
# b=set()
# c=set()
# for i in a:
#     if i%2==0:
#         b.add(i)
#     else:
#         c.add(i)
# print(b,c)
# print(c)

# a={1,2,3,4}
# b=set()
# for i in a:
#   b.add(i*i)
# print(b)
# c=set()
# a={1,2,3,4,5,6}
# b={2,3,4,8,9}
# for i in a:
#     if i in b:
#        c.add(i)
# print(c)
# a={1,2,3,4,5,66}
# b={4,5,6,7,8}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# print(b.difference(a))
a={13,5,6,8,2,7,8,9,11}
np=set()
p=set()
for i in a:
    if i > 1:
     for j in range(2,i):
        if(i%j)==0:
            np.add(i)
            break
        p.add(i)
print(np)
print(p)



