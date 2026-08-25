gender=input("Enter your gender: ")
age=int(input("Enter your age: "))

if gender=="female":
    print("The bus ticket is free for you")
else:
    if age<5:
        print("The bus pass is free for you")
    elif age>=60:
        print("You get a senior citizen discount")
    else:
        print("You need to pay the full price")