# 2)
# list არის კოლექცია მონაცემთა სტრუქტურა სადაც შეგვიძლია ყველანაირი მონაცემის შენახვა
names = ["tazo", "lasha", "luka", "beqa", "levani"]
for i in names:
    print("my name is", i)


# 3)
animals = ["dog", "cat", "cow", "pig", "lion", "tiger"]
print(animals[4][2])


# 4)
item = ['lambo', 'BMW', 'Mercedes', 'Honda', 'phone', 'computer']
print(item[1:5])


# 5)
real_password = 'Nino1234!'
attemps = 3

user_attempts = 0

while attemps > user_attempts: 
    remaining = attemps - user_attempts
    user_input = input(f'Guess the password again You have {remaining}, Attemp(s) left To Guess the password: ')
    user_attempts += 1

    if user_input == real_password:
        print('Congrats you have guessed the correct password!')
        break
    else:
        print('Wrong please try again later!')
else:
    print('You have reached the maximum number of attempts')


# 6)
# ფუნქცია ეს არის კოდი რომელსაც სახელს არქმევ და შემდეგ რამდენჯერაც გინდა იყენებ  ფუბქცია-(def)


# 7)
a = ["d","p","w","q","a","f","t","u","o","a","b","m"]
print(a[7], a[9])


# 8)
# append ამატებს ელემენტებს list ში
list = []
list.append(input("enter name: "))
list.append(input("enter last name: "))
list.append(input("enter age: "))
list.append(input("enter nikname: "))
list.append(input("enter adres: "))
print(list)


# 10)
# მასივში შეგვიძლია ყველანაირი ტიპის მონაცემის შენახვა