# employees=[
#     {"e_id":1000,"e_name":"ram","salary":25000,"department":"testing","exp":1},
#     {"e_id":1001,"e_name":"ravi","salary":22000,"department":"ba","exp":1},
#     {"e_id":1002,"e_name":"raj","salary":20000,"department":"mrkt","exp":1},
#     {"e_id":1003,"e_name":"nikil","salary":26000,"department":"developer","exp":1},
#     {"e_id":1004,"e_name":"nivi","salary":28000,"department":"developer","exp":2},
#
# ]
# for employee in employees:
#     if ( employee['department']=='developer'):
#        print(employee['e_name'])
#        print(employee['e_name'].upper())
# e_names=list(map(lambda employee:employee['e_name'].upper(),employees))
# print(e_names)

# sum=0
# for employee in employees:
#     sum+=employee['salary']
# print(sum)

# for employee in employees:
#     if ( employee['department']=='developer'):
#        print(employee['e_name'])
#        print(employee['e_name'].upper())

#lst=[1,2,3,4]
# square=list(map(lambda num:num**2,lst))
# print(square)
#

# cube=list(map(lambda num:num**3,lst))
# print(cube)
# from functools import reduce
#
# sum=reduce(lambda num,num1:num+num1,lst)
# print(sum)

#lst=[2,4,6]

# lst1=[]
#sum=sum(lst)
# for i in lst:
#     lst1.append(sum -i)
# print(lst1)
#op=[sum-num for num in lst]
#print(op)
#lst=[2,4,6]
# n=len(lst)
# sum=6
# print(getPairsCount(lst,n,sum))


# lst=[1,2,3,4]
# low=0
# upp=len(lst)-1
# pair=6
# pairs=[]
# while(low<upp):
#     sum=lst[low]+lst[upp]
#     if(sum==pair):
#         pairs.append((lst[low],lst[upp]))
#         low+=1
#     elif(sum>pair):
#         upp-=1
#     elif(sum<pair):
#         low+=1
# print(pairs)


lst=[10,11,12,20,23,30]
lst1=[10,11,22,44,23,30]
z=[]
for i in lst:
   if i in lst1:
       z.append(i)
print(z,end=' ')


