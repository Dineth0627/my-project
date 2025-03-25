def calculate_discount(original_price, discount_percentage):
    if original_price < 0 or discount_percentage < 0 or discount_percentage > 100:
        return "Invalid input. Ensure price is positive and discount is between 0-100%."
    
    discount_amount = (original_price * discount_percentage) / 100
    final_price = original_price - discount_amount
    
    return discount_amount, final_price

# Example usage
original_price = float(input("Enter the original price: "))
discount_percentage = float(input("Enter the discount percentage: "))

discount, final_price = calculate_discount(original_price, discount_percentage)
print(f"Discount Amount: ${discount:.2f}")
print(f"Final Price: ${final_price:.2f}")
