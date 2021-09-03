# # #SINGLE INHERITANCE
# class Person: #BASE CLASS/PARENT CLASS/SUPER CLASS
#     def walk(self):
#         print('walking')
# class student(Person): #DERIVED CLASS/SUB CLASS/CHILD CLASS
#     def exam(self):
#         print('exam')
# pe=student()
# pe.exam()
# pe.walk()

# class person():
#     def details(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,self.age)
# class employee(person):
#     def epl(self,id,salary):
#        self.id=id
#        self.salary=salary
#        print(self.id,self.salary)
# a=employee()
# a.details('seeni',33)
# a.epl(1,20000)
#multiple inheritance
# class Person:
#     def details(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,self.age)
# class Child:
#     def details1(self,school,classe):
#         self.school=school
#         self.classe=classe
#         print(self.school,self.classe)
# class student(Person,Child):
#     def display(self,mark):
#         self.mark=mark
#         print(self.mark)
#
# a=student()
# a.details('seeni',33)
# a.details1('luminar',5)
# a.display(55)
#
# class Person:
#     def details(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,self.age)
# class Parent:
#     def details1(self,pname,adress):
#         self.pname=pname
#         self.adress=adress
#         print(self.pname,self.adress)
# class employee(Person,Parent):
#     def display(self,company,salary):
#         self.company=company
#         self.salary=salary
#         print(self.company,self.salary)
# a=employee()
# a.details('seeni',33)
# a.details1('eldho',34)
# a.display('luminar',22222)

class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Parent:
    def details1(self,pname,adress):
        self.pname=pname
        self.adress=adress
        print(self.pname,self.adress)
class Teacher(Person,Parent):
    def display(self,school,salary):
        self.school=school
        self.salary=salary
        print(self.school,self.salary)
a=Teacher()
a.details('seeni',33)
a.details1('eldho',34)
a.display('luminar',22222)

