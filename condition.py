order_amount=1000
days="sat"
membership="no"
if (order_amount>=1000 and days in['sat','sun']) or membership=="gold":
    print("20 percent discount")
else:
    print("No discount")


