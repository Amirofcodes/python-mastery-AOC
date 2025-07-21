# Variable = A container for a value (string, integer, float, boolean) A variable behaves as if it was the value it contains.

# strings

```bash
first_name = "Bro"
food = "pizza"
email = "Bro123@fake.com"
print(f"Hello {first_name}")
print(f"You like {food}")
print(f"Your email is: {email}")
```

# integers

```bash
age = 25
quality = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")
```

# float

```bash
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is ${price}")
print(f"Your gpa is: {gpa}")
print(f"'You ran{distance}km")
```

# boolean

```bash
is_student = True # or False

print(f"Are you a student?: {is_student}")

if is_student:
print(“You are a student")
else:
print(“You are NOT a student")
```

# Typecasting = the process of converting a variable from one data type to another str(), int(), float(), bool()

# input() = A function that prompts the user to enter data. Returns the entered data as a string

```bash
name = input("What is your name?: ")
age = input("How old are you?: ")
age = int (age)
age = age + 1

print(f"Hello {name}!")
print ("HAPPY BIRTHDAY!")
print(f”You will be {age} years old next year")
```

# Exercise 1 Rectangle Area Calc

```bash
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length \* width
print(f"The area is: {area}cm²")
```

# Exercise 2 Shopping Cart Program

```bash
item = input("What item would you like to buy?: ")
price = float(input("What is the price?: "))
quantity = int(input("How many would you like?: "))
total = price \* quantity

print(f"You have bought {quantity} x {item}/s")
print(f"Your total is: €{total)")
```
