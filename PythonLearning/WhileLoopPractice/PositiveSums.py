total=0
while True:
    user=int(input("Enter a number: "))
    if user>=0:
        total+=user
    elif user<0:
        break
print(f"Sum of positive elements: {total}")