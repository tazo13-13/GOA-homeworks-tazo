# 8 დავალება
password = "12345678"

guess = input("enter password: ")

while guess != password:
    print("wrong password")
    
guess = input("enter password: ")
print("password is correct")