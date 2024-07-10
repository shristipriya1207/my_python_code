# class student:
#     name="karan"


# s1 = student()
# print(s1.name)


#================================

#constructor

'''class student:
    name="karan"  #class attribute
    # def __init__(self):
    #     print("this is default construtor called")
    def __init__(self,age ):
        self.age=age  #instance attribute
        print(self)
        print(" parameterized constructor called")
        print(age)


    
s1 = student(23)
print(s1.name)
print(student.name)
# s2= student()

#if the name of the class attribute and instance attribute has same name then the instance attribute will be called,
#because instance > class
'''

#===============================
#methods
'''class student:
    college_name="manipal"

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def welcome(self):
        print("welcome student")
    def get_marks(self):
        return self.marks

s1= student("shristi",99)
s1.welcome()
print(s1.name)
mark=s1.get_marks()
print("returned marks :",mark)'''

#=================================
#static methods
'''
class student:
    college_name="manipal"

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    @staticmethod      #decorator 
    def staticFunc():
        print("no need to pass self because this is static method in pyhton")    
    def welcome(self):
        print("welcome student")
    def get_marks(self):
        return self.marks

s1= student("shristi",99)
s1.welcome()
print(s1.name)
mark=s1.get_marks()
print("returned marks :",mark)
student.staticFunc()
'''


#==============================
 #del keyword:= used to delete object properties or object itself
'''
class student :
    def __init__(self,name):
        self.name=name

s1=student("shristi")  
# print(s1.name)   
del s1.name
print(s1.name)   

'''
#=============================
#Private(like) attributes & methods
# we uses two unserScore (__) with the attribite name to make it private
'''
class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no=acc_no
        self.__acc_pass=acc_pass   #private member
    def reset_pass(self):
        print(self.__acc_pass) 
        self.__hello();  
    def __hello(self):                #private function
        print("hello everyone !")     

acc1 = Account("1234","asas")
# print(acc1.__acc_pass)   #we cannot access private member
print(acc1.acc_no)  
print(acc1.reset_pass())

# print(acc1.__hello())    #we cannot access private member
'''

#===============================
#inheritance
'''class car:
    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("car is started")

class toyoto (car):
    def __init__(self,name,type):
        self.name=name  
        super().__init__(type)
        super().start()

car1 = toyoto("prius","electirc")
print(car1.start()) 
print(car1.type)                         '''
#===========================
#class method => A class method is bound to the class & receives the class as an implicit first argument
'''
class person:
    name="anonymous"

    @classmethod
    def changeName(cls,name):
        cls.name=name

p1=person()
p1.changeName("Rahul kumar")
print(p1.name)
print(person.name)
'''

#============================
# Polymorphism : operator overloading

#addition of two complex number
'''
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
    # def add(self,obj):   #operator overloading
    #     newReal = self.real + obj.real
    #     newimg = self.img+ obj.img 
    #     return complex(newReal,newimg)
    def __add__(self,obj):   #__add__ => dunder function
       newReal = self.real + obj.real
       newimg = self.img+ obj.img 
       return complex(newReal,newimg)

num1 = complex(1,3 )
num1.showNumber()

num2 = complex(3,5)
num2.showNumber()

# num3 = num1.add(num2)  #operator overloading (for use for dunder function)
num3= num1+ num2    #to call the dunder function
num3.showNumber()     

'''

#=============================================
#random number
'''
import random

target = random.randint(1,100)
while True:
    userchoice = input("guess the number or quit")
    if(userchoice == "quit"):
        break

    userchoice = int(userchoice)
    if (userchoice==target):
        print("Success: correct Guess!!")
        break
    elif(userchoice< target):
        print("Your number was too small. take a bigger guess..")
        
    else:
        print("Your number was too big.take a smaller guess..")
        
print("Game over")   '''

#========================================
#Random password generator

import random 
import string

pass_len = 12
charValues = string.ascii_letters + string.digits + string.punctuation

password=""

for i in range(pass_len):
    password += random.choice(charValues)

print("your password is " , password) 






















