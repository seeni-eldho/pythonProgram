#1
# class vechile:
#     def details(self):
#         n1=input("enter the vechile number")
#         n2=input("enter the owner name")
#         self.n1=n1
#         self.n2=n2
#         print("vechile number is ",n1)
#         print("owner name is ",n2)
# class bus(vechile):
#     def detail(self):
#      n3=input("enter the address")
#      self.n3=n3
#      print("address",n3)
# a=bus()
# a.details()
# a.detail()
#13

# evod=lambda a: "even" if a%2==0 else "odd"
# print(evod(5))
# #11

# import re
# rule="^[A-Z][a-z]+"
# sr=input("enter the string")
# matcher=re.fullmatch(rule,sr)
# if matcher is not None:
#     print('valid')
# else:
#     print('not valid')

# class book:
#     def display(self,bookname):
#      self.bookname=bookname
#      print("BOOK NAME",bookname)
# class book1(book):
#     def display(self,author):
#      self.author=author
#      print("AUTHOR IS",author)
# bk=book1()
# bk.display("SARA JOSEPH")
#

# import re
# f=open('phone','r')
# f1=open('phone1','w')
# for i in f:
#  l=i.rstrip("\n")
#  # print(l)
#  rule="[+][9][1][0-9]{10}"
#  matcher=re.fullmatch(rule,l)
#  if matcher is not None:
#      f1.write(i)


# n1=int(input('enter the first'))
# n2=int(input('enter the second'))
# try:
#     div=n1/n2
#     print(div)
# except Exception as e:
#     print(e.args)
# finally:
#     print('done')

# class demo:
#     def __init__(self,name,address):
#         self.name=name
#         self.address=address
#     def __str__(self):
#         s=self.name
#         return s
# obj=demo("luminar","thrissur")
# print(obj)



# class lib:
#     def __init__(self,book_name,author,pages):
#         self.library='luminar'
#         self.book_name=book_name
#         self.author=author
#         self.pages=pages
#     def printval(self):
#         print(self.li
#
# import re
# rule="^[a][\d]*[b]$"
# string=input("enter the string")
# matcher=re.fullmatch(rule,string)
# if matcher is not None:
#     print('valid')
# else:
#     print('not valid')
#
#
