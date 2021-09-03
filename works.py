#a=5
#if a>0:
 #   print('hello')
#else:
 #   print('elif')
#+ve or -ve
#num=int(input('enter a number'))
#if num>0:
  # print('positive')
#elif num==0:
   # print('zero')
#else:
   #print('negative')

#atm transfer
#amount=1000
#('enter the withdraw amount')
#w=int(input('enter amount'))
#if w>1000:
  #  print('insuffient amount')
#else:
   # w=1000-w
   # print('balance amount is',w)


#n1=int(input('enter first number'))
#n2=int(input('enter second number'))
#n3=int(input('enter third number'))
#if n1>n2 and n1>n3:
 #  print('the greater numberis:',n1)
#elif n2>n1 and n2>n3:
 #  print('greater number is:',n2)
#elif n3>n1 and n3>n1:
 #   print('greater number is:',n3)
#else:
 #    print('all are same')

#for i in range(2,5):
  #  print(i)

#for i in range(3,10,2):
   #print(i)


#n1=int(input('enter min'))
#n2=int(input('max'))
#for i in range(n1,n2):
 #   print(i)


# a=int(input('enter a number'))
# for i in range(0,11):
#     print(a,'*',i,'=',i*a)



    # for i in range(1,a):
    #    if   i%2==0:
    #        break
    #    else:
    #      print(a)
    # a+=1



# min=int(input('enter min'))
# max=int(input('enter max'))
# for a in range(min,max):
#     if a>1:
#         for i in range(2,a):
#             if a%i==0:
#                 break
#         else:
#                 print(a,end=' ')
def prim(min,max):
    # global s
    s=0
    for a in range(min,max):
     if a>1:
        for i in range(2,a):
            if a%i==0:
                break
        else:
                print(a,end=' ')
                s+=a

         return(s)

prim(1,100)
print()

print('sum',s)
# a='seeni'
# print(a)
# b=""
# for i in a:
#     if i not in b:
#         b=b+i
#     else :
#         print('repeated',i)
#
# print('new string',b)
# def found(l1,n):
#     low=0
#     high=len(l1)-1
#     mid=(low+high)//2
#     fd=False
#     while low<=high and fd==False:
#         if mid==n:
#             fd=True
#         elif n<l1[mid]:
#             high=mid-1
#         else :
#             low=mid+1
#
#     if fd==True:
#         print('found')
#     else:
#         print('not found')




#
# l1=[2,4,5,6,7,1,3]
# l1.sort()
# n=int(input('enter the number'))
# found(l1,n)