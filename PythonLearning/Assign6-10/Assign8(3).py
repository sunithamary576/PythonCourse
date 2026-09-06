age=int(input("Enter your age: "))

if age<18:
    print("You get a student membership")
elif age>=60:
    print("You get a senior citizen memebership")
else:
    print("You get a regular membership")