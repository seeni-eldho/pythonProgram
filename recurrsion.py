# # def fact(x):
# #     if x==1:
# #         return 1
# #     else:
# #         return x*fact(x-1)
# # print('factorial',fact(3))
# #
def rfib(i):
    if i==0:
        return i
    elif i==1:
        return i
    else:
        return rfib(i-1)+rfib(i-2)

for i in range(10):
    print(rfib(i))