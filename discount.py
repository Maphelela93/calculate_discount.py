  # discount function

# global variation
price = float(input("Enter the price:"))
discount_percent = int(input("Enter the percentage:"))

# function define
def calculate_discount ("price, discount_percent")
   # local variable
   #new_price
   if discount_percent >= 20:
    discount_percent = discount_percent / 100
    dicount = discount_percent * price
    new_price = price = discount
    print(f"The discount is{discount_percent}, and new price is R{new_price}, thanks for shoping wwith us.")
   else:
    print(f"The percentage {discount_percentage}% is too low, the {price} is the original. thanks for shopping with us.")

calculate_discount(price, discount_percent)
