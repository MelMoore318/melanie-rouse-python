name = "Melanie"
age = 42
height = 5.9
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

your_name = input("What is your name? ")
birth_year = int(input("What year were you born "))
age = 2026 - birth_year
print(f"Hi, {your_name}! You are approximately {age} years old")

number1 = float(input("Enter a number: "))
number2 = float(input("Enter a second number: "))

result = number1 * number2
print(f"The product of {number1} and {number2} is {result}. ")

item_name = "Cat food"
price = 21.99
quantity = 3

total = price * quantity

print("=================================")
print("           Receipt               ")
print("=================================")
print(f"Item: {item_name} ")
print(f"Price: {price:.2f} ")
print(f"Quantity: {quantity} ")
print("---------------------------------")
print(f"Total: ${total:.2f} ")

name = input("Enter your full name: ")
hometown = input("Enter your hometown: ")
favorite_hobby = input("Enter your favorite hobby: ")
fun_fact = input("Enter a fun fact: ")
birth_year = int(input("Enter your birth year: "))

age = 2026 - birth_year

print("==================================")
print(f"     Profile: {name}             ")
print("==================================")
print(f"Name:           {name}")
print(f"Hometown:       {hometown}")
print(f"Favorite hobby: {favorite_hobby}")
print(f"Fun fact:       {fun_fact}")
print(f"Age:            {age}")
print("==================================")

