# 2)
corect_password = "secret"
attempts = 0

while attempts < 3:
    user_input = input("Enter password: ")

    if user_input == corect_password:
        print("Access granted")
        break
    else:
        attempts += 1
        print("Incorrect password! attempts used", attempts)

        if attempts == 3:
            print("You have reached the maximum number of attempts")


# 3)
print(True and False and 5 > 9 and 90 * 30 > 1089 or False and 'Nino' != '' or False or True and 56 * 2 > 90)
# გამოიტანს True რადგან ჯერ and მოქმედებ კეთდება შემდეგ or


# 4)
# მასივი ანუ list სია, კოლექცია მაგალითად [1, 2, 3] ან [ა, ბ ,ს] ყველანაირი მონაცემის ტიპის შენახვა შეგვიძლია


# 5)
ოჯახი = "თაზო ტერტერაშვილი, ლაშა ტერტერაშვილი, ლაზარე ტერტერაშვილი, იოანე ტერტერაშვილი, სოსო ტერტერაშვილი, თეო გოდერძიშვილი"
for i in ოჯახი:
    print(i)


# 6)
numbers = [4, 5, 6, 7, 8, 9]
total = 0

for i in numbers:
    total += i

print("sum: ", total)



# 7)
# indexing თუ სია გვაქვს კონკრეტულ ელემენტს ამოვიღებთ ინდექსის გამოყენებით ასევე ეს string ზეც მუშაობს


# 8)
# indexing ამის საშუალებით ჩვენ ელემენტზე წვდომა გვაქვს, ანუ მიუთითებს ადგილს სიაში, შეგვიძლია მისი სიიდან გამოტანა მოქმედების შესრულება და ასევე ჩანაცვლება


# 9)
# 1
num = [10, 20, 30]
print(num[0])


# 2
letters = ['a', 'b', 'c', 'd']
print(letters[-1])


# 3
numbers = [1, 2, 3]

numbers[1] = 77
print(numbers)


# 4
animals = ['cat', 'pig', 'wolf']
print(animals[2][2])


# 5
nums = [1, 2, 3]
nums.append(4)
print(nums)