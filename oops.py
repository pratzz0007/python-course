# # #class

class employee:
    name = "harry"
    language= "py" 
    slary =120000
harry = employee()
print(harry.name , harry.language)     

#self_parameter

class employee:
    name = "harry"
    language = "py"  #this is a class attribute
    slary =120000
    mood = "happy"
    def getinfo(self ):
        print(self.mood)
        print(f"thelanguageis {self.language} and the salary is {self.slary}")
    @staticmethod
    def greet():
        print("good morning")

harry = employee()
harry.language =  "javascript" #this is an instance attribute,
harry.name = "pratik"
print(harry.name)
harry.getinfo() 
harry.greet()

# #CONSTRUCTOR


class employee:
    name = "harry"
    language = "py"  #this is a class attribute
    slary =120000
    def __init__(self): # dunder method which is automatically called
         
         print("employee object is created")
    mood = "happy"
    def getinfo(self ):
        print(self.mood)
        print(f"thelanguageis {self.language} and the salary is {self.slary}")
    @staticmethod
    def greet():
        print("good morning")

harry = employee()
harry.name = "pratik"
print(harry.name , harry.slary)

 

#constructor 2
class employee:
    name = "harry"
    language = "py"  #this is a class attribute
    slary =120000
    def __init__(self , name , slary , language): # dunder method which is automatically called
         self.name = name
         self.slary = slary
         self.language = language
         print("employee object is created")
    mood = "happy"
    def getinfo(self ):
        print(self.mood)
        print(f"thelanguageis {self.language} and the salary is {self.slary}")
    @staticmethod
    def greet():
        print("good morning")

harry = employee("pratik", 150000, "js")
harry.name = "pratik"
print(harry.name , harry.slary , harry.language)

 