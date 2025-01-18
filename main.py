firstNum = int(input("First num: "))
secondNum = int(input("Second num: "))

print("a+b", firstNum+secondNum, "\na-b", firstNum-secondNum, "\na*b", firstNum*secondNum, "\na/b", firstNum/secondNum)

name = str(input("Ur name: "))
color = str(input("Ur favorite color: "))

print("Ur name is", name, "and ur favorite color is", color)

yearOfBirth = int(input("Ur birth: "))
ageYear = int(input("Did you have a birthday this year? Choose 1 if yes or 2 if no: "))

if (ageYear == 1):
    age = 2025 - yearOfBirth
elif (ageYear == 2):
    age = 2025 - 1 - yearOfBirth
else:
    print("Sorry! We have some troubles(((")
print(age)