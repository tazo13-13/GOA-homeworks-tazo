# 5 დავალება
i = 1
while i <= 10:
    print(i)
    i = i + 1


# 6 დავალება
a = 10
while a >= 1:
    print(a)
    a = a - 1


# 7 დავალება
name = input("enter your name: ")

vowels = "aeiou"
count = 0

for i in name:
    if i in vowels:
        count += 1
print("in your name are" ,count, "vowels")