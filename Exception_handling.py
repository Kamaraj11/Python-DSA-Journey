from re import findall

print("welcome to zomato")

try:
    number_of_items = int(input("How many itmes? "))
    total_price = 200 * number_of_items
    average_price = total_price / number_of_items
    print("Average price per items", average_price)
except Exception:
    print("you cannot put zero ")







