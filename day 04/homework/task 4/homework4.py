# 5 დავალება
# Sequencing- ყველაფერი თამიმდევრობით ხდება მაგ:
print("A")
print("tazo")
print("13")

# Selection- არჩევს ერთ-ერთ გზას პირობის მიხედვით მაგ:
age = 15
if age >= 18:
    print("srulwlovani xar")
else:
    print("ar xar srulwlovani")

#  Iteration- იმეორებს მოქმედებას რამდენჯერმე
for i in range(5):
    print("Tazo13")


# 6 დავალება
# for loop - ეს არის ციკლი, რომელიც გამოიყენება მაშინ როდესაც ზუსტად ვიცით რამდენჯერ გვინდა ბრძანების შესრულება
# for ცვლადი  in ობიექტი:
# მაგალითად:
for i in range(1,14):
    print("name", i)

pairs = [(1,"a"), (2, "b"), (3, "c")]
for number, letter in pairs:
        print(number, letter)


# 7 დავალება
# while loop-ეს არის ციკლი როდესაც რაღაც კოდი მეორდება იქამე სანამ პირობა ჭეშმარიტი არ იქნება
# მაგალითად:
x = 10
while x >= 5:
    print(x)
    x = x - 1
# for loop და while loop განსხვავებაა ის რომ for loop_ში წინსწარ ვიცით რამდენჯერ მეორდება კოდი while loop_ში კი არვიცით


# 8 დავალება
user_number = int(input('Enter the number: '))
factorial = 1

for i in range(factorial, user_number + 1):
    factorial = factorial * i
print(factorial)