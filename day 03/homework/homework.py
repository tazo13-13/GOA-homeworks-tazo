# 1 დავალება
a = 5
b = "3"

sum = a + int(b)
print(sum)


# 2 დავალება
print (int("5"))
print(int("12"))

print(str(5))
print(str(12))

print(float(1))
print(float(11))

print(bool("tazo"))
print(bool(0))


# 3 დავალება
x = float(input("enter number: "))
y = float(input("enter number 2: "))


# 4 დავალება
a = int(input("enter first number: "))
b = int(input("enter second number: "))

if a % 2 == 0 and b % 2 == 0:
    print("both number are even. their sum is:", a + b) 
else:
    print("The given numbers are not even so they will not be summed")


# 5 დავალება
name = input("Your name is:")
surname = input("Your surname is:")
age = input("Your age is:")
city = input("You live in:")
country = input("The country you live in is:")

print("Your name is:", name)
print("your surname is:", surname)
print("your age is:", age)
print("your city is", city)
print("your country is", country)


# 6 დავალება
print(5 == 5)
print(6 >= 9)
print(9 <= 8)
print(10 < 11)
print(11 > 10)
print(11 != 10)


# 7 დავალება
x = int(input("enter number: "))
y = int(input("enter number 2: "))
print(x - y)
print(x + y)
print(x / y)
print(x * y)


# 8 დავალება
my_name = "tazo"
your_name = input("enter your name: ")

if my_name == your_name:
    print('We have the same name')
else:
    print('Our names do not match')


# 9 დავალება
# კონკადინაცია არის სტრინგების ერთმანეთზე მიმატება

print('45' + "45")
# გამოიტანს 4545 რადგან სტრინგია


# 10 დავალება
x = int(input("enter number: "))

if x % 2 == 0:
    print('The number is even')
else:
    print("your number is odd")