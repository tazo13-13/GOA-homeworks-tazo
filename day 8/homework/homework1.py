# 2)
# ფუნქცია არის ჩაშენებული პროგრამა რომელიც ასრულებს კონკრეტულ მოქმედებას მისი გამოძახება შეგვიძლია მუდმივად


# 3)
name = ["tazo", "lasha", "soso", "luka", "gio", "levani", "gia", "saba"]
print(name[:8])
# ინდექსის რაოდენობის გასაგებად ვიყენებთ len ფუნქციას
print(len(name))


# 4)
index = int(input("Enter index: "))
text = input("Enter name: ")

names = ["example_name", "example_name_2", "example_name_3", "example_name_4"]

names.insert(index, text)

print(names)


# 5)
name2 = input("enter your name: ")
print(name2.title())


# 6)
# function — ცალკე შექმნილი კოდია, რომელსაც ვწერთ ჩვენ და ვიძახებთ მის სახელს.
# method — არის ფუნქცია, მაგრამ მიბმულია კონკრეტულ ობიექტზე (მაგ. string, list).


# 7)
name3 = '    N I N O     '
print(name3.strip())


# 8)
def greet(name):
    print("Hello", name)

greet("tazo")