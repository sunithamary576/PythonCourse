seat=3

while seat>0:
    print(f"There are {seat} seats available")
    booking=input("Do u wanna book a seat?(yes/no): ").lower()
    if booking=="yes":
        seat-=1
        print("Seat booked!")
    else:
        print("No booking made.")
        break
    if seat==0:
        print("All seats are booked!")
