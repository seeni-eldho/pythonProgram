# que=[]
# front=0
# rear=0
# size = int(input('enter the size'))
# n=1
# def qin():
#     global front,size,que,rear
#     if rear<size:
#         n1=int(input('enter the number'))
#         que.insert(rear,n1)
#         rear+=1
#     else:
#         print('queue is full')
#         for i in range(front,rear):
#             print(que[i])
# def qout():
#     global front,que,rear
#     if rear==front:
#         print('queue is empty')
#     else:
#         front+=1
#         for i in range(front,rear):
#             print(que[i])
#
#
#
# while(n==1):
#     choice=int(input('enter the choice'))
#     if (choice==1):
#       qin()
#     elif( choice==2):
#      qout()
#     n=int(input('1 to continue'))
# def prim():
# for i in range(1,50):
#     if (i>1):
#         for j in range(2,i):
#             if i%j==0:
#              break
#         else:
#           print(i,end=' ')


# min=int(input('enter min'))
# max=int(input('enter max'))
# for a in range(min,max):
#     if a>1:
#         for i in range(2,a):
#             if a%i==0:
#                 break
#         else:
#                 print(a,end=' ')
k=1
for i in range(4):
    if (1%2!=0):
      for j in range (4):
       for l in range(j):
        print(k,end=' ')
       print()
      k+=1
