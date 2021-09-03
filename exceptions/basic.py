# n1=int(input('enter the first'))
# n2=int(input('enter the second'))
# try:
#     div=n1/n2
#     print(div)
# except:
#     print('exception occured')
a=[1,2,3,4,5]
n=int(input('enter the index to print'))
try:
    print(a[n])
except:
    print('out of range')
finally:
    print('inside finally')

# a = [1, 2, 3, 4, 5]
# n = int(input('enter the index to print'))
# try:
#     print(a[n])
# except Exception  as e:
#     print(e.args)
# finally:
#     print('inside finally')
# n1=int(input('enter the first'))
# n2=int(input('enter the second'))
# try:
#     div=n1/n2
#     print(div)
# except Exception as e:
#     print(e.args)
# finally:
#     print('done')
# a=int(input('enter the first'))
# b=int(input('enter the second'))
# if b>a:
#     raise Exception('n02 is great ')
# else:
#     print(a/b)

# a = int(input('input  enter age'))
# if a < 18:
#     raise Exception('not eligible')
# else:
#     print('eligible')
#try block and finally always works
#but except does not always work

