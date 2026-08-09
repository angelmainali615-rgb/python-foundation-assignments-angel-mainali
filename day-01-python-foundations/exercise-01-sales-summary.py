product_name = "Wireless Mouse"
unit_price = 1500
quantity_sold = 12
discount_percentage = 0.10

# Calculate gross sales
gross_sales = unit_price * quantity_sold

# Calculate discount amount
discount_amount = gross_sales * discount_percentage

# Calculate final sales
final_sales = gross_sales - discount_amount

# Display the result
print(f"Product: {product_name}")
print(f"Gross sales: NPR {gross_sales:.2f}")
print(f"Discount: NPR {discount_amount:.2f}")
print(f"Final sales: NPR {final_sales:.2f}")