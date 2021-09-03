# #class
# class person:
#     def walk(self):
#         print('person is walking')
#     def read(self):
#         print('person is reading')
#
# #object1
# pe1=person()
# pe1.walk()
# pe1.read()
#
# #object1
# pe2=person()
# pe2.walk()
# pe2.read()

# class book:
#     def authour(self):
#         print('auther is akkittam')
#     def year(self):
#         print('published in 2019')
#
# #object1
# pe1=book()
# pe1.authour()
# pe1.year()
#
# #object1
# pe2=book()
# pe2.authour()
# pe2.year()

# class person:
#     def value(self,name,age):
#         self.name=name
#         self.age=age
#     def printval(self):
#         print('name',self.name)
#         print('age:',self.age)
# pe=person()
# pe.value('anu',22)
# pe.printval()
# class employee:
#     def value(self,id,name,salary,age,company,department):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         self.company=company
#         self.id=id
#         self.department=department
#     def printval(self):
#         print('id:', self.id, end=' ')
#         print(',name:',self.name,end=' ')
#         print(',age:',self.age,end=' ')
#         print(',company:',self.company,end=' ')
#         print(',department:',self.department,end=' ')
#         print(',salary:', self.salary, end=' ')
# pe=employee()
# pe.value(1,'anu',22000,22,'luminar','finanace')
# pe.printval()
# class Add:
#     def inputval(self):
#        n1=int(input('first number'))
#        n2=int(input('second number'))
#        self.n1=n1
#        self.n2=n2
#     def result(self):
#        print('sum is',self.n1+self.n2)
# a=Add()
# a.inputval()
# a.result()
#TYPES OF VARIABLES
#1.INSTANCE VARIABLE..RELATED TO METHODS..ACCESS USING SELF
#2.STATIC VARIABLE..RELATES TO CLASS..ACCESS USING CLASS NAME
# class Stud:
#     school='luminar'
#     def value(self,rollno,name):
#         self.name=name
#         self.rollno=rollno
#     def printval(self):
#         print('id:', self.rollno, end=' ')
#         print(',name:',self.name,end=' ')
#         print(',school:',Stud.school,end=' ')
#
# pe=Stud()
# pe.value(1,'anu')
# pe.printval()

# class Emp:
#     company='luminar'
#     def value(self,id,name):
#         self.name=name
#         self.id=id
#     def printval(self):
#         print('id:', self.id, end=' ')
#         print(',name:',self.name,end=' ')
#         print(',company:',Emp.company,end=' ')
#
# pe=Emp()
# pe.value(1,'anu')77
# pe.printval()

# class Bank:
#     def customer(self,name,accountno):
#         self.name=name
#         self.minbalance=5000
#         self.balance=self.minbalance
#         self.accountno=accountno
#     def deposit(self,amt):
#         self.amt=amt
#         self.balance+=self.amt
#         print('credit',self.amt)
#     def withraw(self,amut):
#         self.amut=amut
#         if self.amut>self.balance:
#             print('defficency')
#         else:
#             self.balance-=self.amut
#             print('final balance is',self.balance)
#
# c1=Bank()
# c1.customer('seeni',1)
# c1.deposit(2000)
# c1.withraw(1000)

# class Person:
#   def __init__(self,name,age,address):
#     self.name=name
#     self.age=age
#     self.address=address
#
#   def display(self):
#       print(self.name,self.age,self.address)
# obj=Person("seeni",33,"luminar")
# obj.display()
# class Calculator:
#     def __init__(self,n1,n2):
#         self.n1=n1
#         self.n2=n2
#     def sum(self):
#         print('sum=',self.n1+self.n2)
#     def sub(self):
#         print('sub',self.n1-self.n2)
#     def div(self):
#         print('div',self.n1/self.n2)
#     def mul(self):
#         print('mul',self.n1*self.n2)
# c1=Calculator(6,3)
# ch=int(input('enter choice'))
# if ch==1:
#     c1.sum()
# elif (ch==2):
#     c1.sub()
# elif (ch==3):
#     c1.div()
# elif (ch==4):
#     c1.mul()
#



class Teacher:
        college='luminar'
        def __init__(self,name,id,subject,department):
            self.name=name
            self.id=id
            self.subject=subject
            self.department=department
        def display(self):
            print('name:',self.name,'id:',self.id,'college:',Teacher.college,'department:',self.department)

t1=Teacher('seeni',1,'computer','computerscience')
t1.display()