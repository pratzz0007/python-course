name = input("enter a student name : ")
roll_no = int (input(" enter a student roll no : "))
math = int (input("enter maths marks : "))
science = int (input("enter science marks : "))
english = int (input (" enter marks of english subject:" ))
total = math + science + english 
average = total /3
print("\n----student report----")
print("name : " , name)
print("roll no : " , roll_no)
print("total marks" , total)
print("average marks" , average)
if average >=90:
    print("grade : A")
elif average >=75:    
    print("grade : B")
elif average >=60:
    print("grade : C")
else:
    print("grade : D")     