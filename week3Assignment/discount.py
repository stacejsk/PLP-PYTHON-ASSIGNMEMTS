def calculate_discount(price, discount_percent):
    if discount_percent>= 20:
        discounted_price = price- (discount_percent/100 * price)
        return discounted_price
    else:
        return price
    
original_price = int(input("What is the original price :"))
discount = int(input("What is the discount price :"))

final_price= calculate_discount(original_price, discount)

if final_price == original_price:
    print("No discount for", final_price)
else :
    print("Your discounted price is :", final_price)