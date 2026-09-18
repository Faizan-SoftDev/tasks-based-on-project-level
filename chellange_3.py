# 🚀🗂️ Challenge 1: The High-Precision Pricing Engine (Decimal)Problem: Your e-commerce store needs to calculate the final price of items in a shopping cart. If you use standard float data types, binary rounding errors will happen (e.g., 10.15 + 20.30 might equal 30.450000000000003), causing financial mismatches.Your Task: Write a function calculate_order_total(items: list[dict], tax_rate: str) -> str that loops through a list of items, calculates the subtotal, adds tax, and returns the final total as a string rounded to exactly two decimal places.Input Format:pythonitems = [
#     {"name": "Laptop Sleeve", "price": "25.99", "qty": 2},
#     {"name": "Wireless Mouse", "price": "12.50", "qty": 1}
# ]
# tax_rate = "0.08"  # 8% sales tax
# Use code with caution.🛒 
from decimal import Decimal, ROUND_HALF_UP

def calculate_order_total(items: list[dict], tax_rate: str) -> str:
    # 1. Initialize subtotal as a Decimal zero
    subtotal = Decimal("0.00")
    
    # 2. Safely compute item totals without converting to float
    for item in items:
        price = Decimal(item["price"])
        qty = Decimal(str(item["qty"]))  # Convert int to str for safety
        subtotal += price * qty
        
    # 3. Convert tax rate to Decimal and compute total
    tax_multiplier = Decimal(tax_rate)
    total = subtotal * (Decimal("1.00") + tax_multiplier)
    
    # 4. Quantize to exactly 2 decimal places using standard accounting rounding
    final_total = total.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    
    return str(final_total)    

# --- Test Case ---
pythonitems = [
    {"name": "Laptop Sleeve", "price": "25.99", "qty": 2},    
    {"name": "Wireless Mouse", "price": "12.50", "qty": 1}
]

print(calculate_order_total(pythonitems, tax_rate="0.08"))  # Output: "69.64"