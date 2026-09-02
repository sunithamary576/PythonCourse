pin="1234"
attempt=1

while attempt<=3:
    input_pin=input(f"Attempt-{attempt}\nEnter your pin: ")
    attempt+=1
    if input_pin==pin:
        print("Successful\n")
        break
    else:
        print("Wrong pin\n")
        if attempt>3:
            print("Account locked")

       
    