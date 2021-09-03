# def revert_val(func):
#     def wrapper(no1,no2):
#         if no1<no2:
#             (no1,no2)=(no2,no1)
#             return func(no1,no2)
#         else:
#             return func(no1,no2)
#     return wrapper
# # @revert_val
# def div(num1,num2):
#     return num1/num2
# print(div(2,10))
# def admin(func):
#     def wrapper(a,b):
#         if a!="admin":
#             raise Exception('NOT ALLOWED')
#         else:
#             return func(a,b)
#     return wrapper

# @admin
# def changepin(user,pin):
#     my=pin
#     return my
# print(changepin('admi',1000))

# def vaccine(func):
#     def wrapper(a,b):
#         if b<18:
#             raise Exception('not elligible')
#         else:
#             return func(a,b)
#     return wrapper
#
# @vaccine
# def person(name,age):
#       return name+' is elligible'
# print(person('admi',17))