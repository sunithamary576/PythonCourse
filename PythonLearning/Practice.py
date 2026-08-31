Bill=600
coupon1=249
coupon2=500
if Bill>=coupon1 and Bill<=400:
    print(f"Total amount to pay: {int(Bill/2)}")
elif Bill>=coupon2 and Bill<=1000:
    print(f"Total amount to pay: {int(Bill/1.5)}")
else:
    print(f"Total amount to pay: {Bill}")
