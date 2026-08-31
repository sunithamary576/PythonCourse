Bill=250
coupon1=249
coupon2=500
if Bill>=coupon1 and Bill<=400:
    print(f"Total amount to pay: {int(Bill/1.5)}")
    print(f"Add items upto Rs 500 to get half price")
elif Bill>=coupon2 and Bill<=1000:
    print(f"Total amount to pay: {int(Bill/2)}")
else:
    print(f"Total amount to pay: {Bill}")