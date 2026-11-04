"""
Reflection:
1. In Exercise 3 you saw the difference between .get() and bracket notation. When in real work would you use each one, and what's your rule of thumb for choosing?
   - Use bracket notation when you expect the key to be present and want your program to fail fast if data is missing, which helps catch bugs early during development. Use .get() when a key might be optional or missing and you have a sensible default value or want to handle missing keys gracefully without crashing your script. Rule of thumb: use brackets for required fields, and .get() for optional fields or configuration lookups.

2. Exercise 8 asked you to build a summary dictionary with a loop. What does this pattern remind you of from Excel, and why might the Python version be more useful for large datasets?
   - This pattern reminds me of a Pivot Table or a SUMIF/COUNTIF function in Excel. The Python version is much more useful for large datasets because it is not limited by Excel's row constraints, can easily scale to millions of rows, automates data cleaning and transformation pipelines effortlessly, and can integrate directly with databases or APIs without manual file exports.
"""

# EXERCISE 1 · Beginner: One customer
print("=== EXERCISE 1 ===")
customer = {
    "name": "Alice Smith",
    "email": "alice@example.com",
    "tier": "gold",
    "ytd_spend": 1250.50,
}

print(customer["name"])
print(customer["email"])
print(customer["tier"])
print(customer["ytd_spend"])
print("Full dict:", customer)
print()


# EXERCISE 2 · Beginner: Update and add
print("=== EXERCISE 2 ===")
customer["phone"] = "555-0199"
print("After adding phone:", customer)

customer["tier"] = "platinum"
print("After updating tier to platinum:", customer)

del customer["email"]
print("After deleting email:", customer)
print()


# EXERCISE 3 · Beginner: Safe lookup
print("=== EXERCISE 3 ===")
# Use .get() to look up the deleted email field with a default value
email_result = customer.get("email", "no email on file")
print(f".get() result for email: {email_result}")

try:
  print(customer["email"])
except KeyError:
  print("KeyError caught: 'email' key no longer exists in the dictionary.")
print()


# EXERCISE 4 · Beginner: Iterate
print("=== EXERCISE 4 ===")
for key, value in customer.items():
  print(f"{key}: {value}")

print()


# EXERCISE 5 · Intermediate: Lookup table
print("=== EXERCISE 5 ===")
tier_discounts = {"bronze": 0, "silver": 0.05, "gold": 0.10, "platinum": 0.15}

current_tier = customer["tier"]
discount_rate = tier_discounts.get(current_tier, 0)
purchase_amount = 200
final_price = purchase_amount * (1 - discount_rate)

print(
    f"Tier: {current_tier} · Discount Rate: {discount_rate * 100}% ·"
    f" Final Price: ${final_price:.2f}"
)
print()


# EXERCISE 6 · Intermediate: List of dicts
print("=== EXERCISE 6 ===")
customers_list = [
    {"name": "Alice", "tier": "platinum", "ytd_spend": 3000},
    {"name": "Bob", "tier": "silver", "ytd_spend": 450},
    {"name": "Charlie", "tier": "bronze", "ytd_spend": 120},
]

purchase_amount_6 = 300
for c in customers_list:
  rate = tier_discounts.get(c["tier"], 0)
  discount_amount = purchase_amount_6 * rate
  print(
      f"Name: {c['name']} · Tier: {c['tier']} · Discount Amount:"
      f" ${discount_amount:.2f}"
  )
print()


# EXERCISE 7 · Intermediate: Nested catalog
print("=== EXERCISE 7 ===")
catalog = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product_name, info in catalog.items():
  if info["stock"] < 20:
    print(f"LOW STOCK ALERT: {product_name} has only {info['stock']} items left!")
print()


# EXERCISE 8 · Advanced: Sales by region
print("=== EXERCISE 8 ===")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200},
]

sales_summary = {}
for tx in transactions:
  region = tx["region"]
  amount = tx["amount"]
  sales_summary[region] = sales_summary.get(region, 0) + amount

# Print final summary sorted by region name
for region in sorted(sales_summary.keys()):
  print(f"{region}: {sales_summary[region]}")