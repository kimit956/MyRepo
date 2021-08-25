def is_num(shopping_cart):
    try:
        x = float(input("Enter the price of your item: $"))
    except ValueError:
        x = float(input("\nThat is not a number.\n"))
    shopping_cart.append(x)


shopping_cart = []
response = "Y"
total = 0

while response != "N":
    is_num(shopping_cart)
    try:
        response = input("Add more items to your cart? y/n: ")
    except ValueError:
        response = input("\nPlease enter a 'Y' for yes or a 'N' for no: ")
    response = response.capitalize()
if len(shopping_cart) < 23:
    total = sum(shopping_cart) * 0.85
elif len(shopping_cart) > 24:
    total = sum(shopping_cart) * 0.75
else:
    total = sum(shopping_cart)
tax = total * 1.08
print("The total is:","${0:.2f}".format(tax))