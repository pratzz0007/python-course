# class bankaccount:
#     def __init__(self, account_number, balance=0):
#             self.account_number = account_number
#             #__balance is a private variable, it can only be accessed within the class
#             self.__balance = balance
#     def deposit(self, amount):
#             if amount > 0:
#                 self.__balance += amount
#                 print(f"Deposited {amount}. New balance: {self.__balance}")
#             else:
#                 print("Deposit amount must be positive.")
#     def show_balance(self):
#             print(f"Account Number: {self.account_number}, Balance: {self.__balance}")



#encapsulation 2
class Student:
    def __init__(self, name, admission_number, cgpa):
        self.name = name
        self.admission_number = admission_number
        self.__cgpa = cgpa

    def get_cgpa(self):
        return self.__cgpa

    def set_cgpa(self, new_cgpa):
        if 0 <= new_cgpa <= 10:
            self.__cgpa = new_cgpa
        else:
            print("Invalid CGPA. It must be between 0 and 10.")

pratik = Student("Pratik", "12345", 8.5)

print(pratik.get_cgpa())

pratik.set_cgpa(9.0)

print(pratik.get_cgpa())