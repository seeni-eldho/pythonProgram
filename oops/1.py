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
#
# class A:
#     def printa(self):
#         print('a')
# class B(A):
#     def printb(self):
#         print('b')
# class C(B)   :
#     def printc(self):
#         print('c')
# a=A()
# a.printa()
# b=B()
# b.printb()
# c=C()
# c.printc()

# class Child:
#     def printa(self):
#         print('SEENI')
# class Student(Child):
#     def printb(self):
#         print('21')
# class Parent(Student)   :
#     def printc(self):
#         print('LUMINAR')
# a=Child()
# a.printa()
# b=Student()
# b.printb()
# c=Parent()
# c.printc


#
# class Person:
#         def valuea(self,name):
#           self.name=name
#           print(self.name)
#
#
# class Child(Person):
#             def valueb(self,  name):
#                 self.name = name
#                 print(self.name)
#                 print(self.name)
# #
#
# class Parent(Person):
#     def valuec(self,  name):
#         self.name = name
#         print(self.name)
#
# #
# class Student(Child):
#         def valued(self,  name):
#             self.name = name
#             print(self.name)
#
#
#
#
# a=Person()
# a.valuea('seeni')
# b=Child()
# b.valueb('sincy')
# c=Parent()
# c.valuec('sibi')
# d=Student()
# d.valued('eldho')
#class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def printval(self):
#         print('name',self.name)
#         print('age',self.age)
#
# class student(person):
#     def __init__(self,rollno,mark,name,age):
#         super().__init__(name,age)
#         self.rollno=rollno
#         self.mark=mark
#     def print(self):
#         print(self.rollno)
#         print(self.mark)
#         print(self.name)
#         print(self.age)
# cr=student(2,34,'seeni',22)
# cr.printval()

# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#
#     def printval(self):
#         print('name',self.name)
#         print('age',self.age)
#
# class student(person):
#     def __init__(self,rollno,mark,name,age):
#         super().__init__(name,age)
#         self.rollno=rollno
#         self.mark=mark
#     def print(self):
#         print(self.rollno,self.mark,self.name)
# cr=student(2,34,'seeni',22)
# cr.print()

# class vechicle:
#     def __init__(self,model,regno,color):
#         self.model=model
#         self.regno=regno
#         self.color=color
#     def print(self):
#         print(self.model,self.regno,self.color)
#     def __str__(self):
#         return self.model
#
# vh=vechicle('i10','123ed','black')
# vh.print()
# print(vh)


# class student:
#     def __init__(self,name,rollno,department,college):
#         self.name=name
#         self.rollno=rollno
#         self.department=department
#         self.college=college
#     def print(self):
#         print(self.name,self.rollno,self.department,self.college)
#     def __str__(self):
#         return self.name+str(self.rollno)
#
# vh=student('seeni',23,'computer','vimala')
# vh.print()

#print(vh)


class parent:
    def __init__(self,name,address):
        self.name=name
        self.address=address
    def display(self):
        print(self.age,self.address)

class teacher(parent):
    def __init__(self,name,age,address,id):
        super().__init__(age,address)
        self.name=name
        self.id=id
    def printval(self):
        print(self.name,self.address,self.id,self.address)

    def __str__(self):
        return self.name+str(self.id)

st=teacher('seeni',123,22,'asfs')
st.printval()
print(st)
#polymorphism(manyforms)
#overloadind...same method name diff num of parameters

# class parent:
#     def dis(self,name):
#         self.name=name
#         print(self.name)
#
# class teacher(parent):
#        def dis(self,name1,addr):
#         self.name1=name1
#         self.addr=addr
#         print(self.name1,self.addr)

# per=teacher()
# per.dis('seeni',2)
## #overriding...same method name and same num of argumenrts
# class opp:
#     def dis(self,n1):
#         self.n1=n1
#         print(self.n1)
#     def dis(self,n2,n3):
#         self.n2=n2
#         self.n3=n3
#         print(self.n2+self.n3)
#
#
# per=opp()
# per.dis(6,7)

#child class method overrides parent class method
# class parent:
#     def dis(self,name,add):
#         self.name=name
#         self.add=add
#
# class teacher(parent):
#     def dis(self, name, add):
#         self.name = name
#         self.add = add
#         print(self.name)
#         print(self.add)
#
#
# per = teacher()
# per.dis('seeni', 1)
#
# class parent:
#     def dis(self,name):
#         self.name=name
#         print(self.name)
#
#     def dis(self,name1,addr):
#         self.name1=name1
#         self.addr=addr
#         print(self.name1,self.addr)
#
# per=parent()
# per.dis('seeni')
#
#
#
#
#
#
#
#















































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































