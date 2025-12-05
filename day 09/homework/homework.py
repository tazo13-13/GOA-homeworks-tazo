# 2)
# default parameters არის ის როდესაც ფუნქცია მუშაობს არგუმენტის გარეშე მაგ: def greet(name = "tazo") -- print("hello name") 
# return ფუნქციაში აბრუნებს მნიშვნელობას მაგ: def add(a, b): -- return a + b  -- x = add(13, 2) -- print(x)


# 3)
def which_is_greater(c, b):
    if c > b:
        print("message - The first number is greater than the second number")
    elif c < b:
        print("The second number is greater than the first number")
    else:
        print("they are equal to each other")
        
which_is_greater(13, 13)


# 4)
def num(a):
    total = 0
    for i in a:
        total += i
    print(total)
    return total
num([2, 3, 4, 5, 6, 7, 8, 9, 10])


# 5)
def count_vowels(t):
    count1 = 0
    for k in t:
        if k in "aeiou":
            count1 += 1
    return count1
print(count_vowels("tazo"))


# 6)
def is_palindrome(v):
        if v == v[::-1]:
            print('This text is palindrome')
        else:
            print('This text is not a palindrome')
            
is_palindrome(input("enter name: "))


# 7)
def is_uppercase(z):
    if z == z.upper():
        print("True")
    else:
        print("False")

is_uppercase(input("enter name upper: "))


# 8)
# sring methods: 
namee = "tazo"
print(namee.upper())

name1 = "lasha"
print(name1.lower())

name2 = "soso"
print(name2.capitalize())

name3 = "hidroelectrosadguri"
print(name3.count("o"))


# list methods:
colors = ["red", "blue", "green"]
colors.append("pink")
print(colors)

colors1 = ["red", "blue"]
colors1.insert(1, "pink")
print(colors1)

colors2 = ["red", "blue"]
colors2.remove("red")
print(colors2)

numss = [1, 2, 3, 4, 7, 2, 10]
numss.sort()
print(numss)

nums2 = [1, 2, 3, 4, 4, 4, 7, 2, 77, 77, 10]
nume3 = set(nums2)
print(nume3)

# 9)