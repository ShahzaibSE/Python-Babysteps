customer7890 = {"firstname": "Shahzaib", "lastname":"Noor", "age": "25", "zipCode": "74600"}
del customer7890["zipCode"]
print(f"Customer Info: {customer7890}")
#
firstname_customer = customer7890.get("firstname")
print(firstname_customer)
customer7890.update({"country" : "Pakistan"})
print("Updated customer Info")
print(customer7890)
print()
#
for key in customer7890: #with values you only get keys.
    print(f"Customer keys: {key}")
print()
# Iterating over dictionaries values.
for val in customer7890.values(): #with values you only get keys.
    print(f"Customer Info: {val}")
# Just loop through keys.
print()
for key in customer7890.keys():
    print(f"Customer keys: {key}")  
#Printing both keys and values.
print()
for key, val in customer7890.items():
    print(f"Customer keys: {key} & Customer value: {val}")       
#
# 
customer_29876 = {
 "first name": "David",
 "last name": "Elliott",
 "address": "4803 Wellesley St.",
 "discounts": ["standard", "volume", "loyalty"],
}    
#
discount_amount = 0
#
if "brother-in-law" in customer_29876["discounts"]:
  discount_amount = .30
elif "loyalty" in customer_29876["discounts"]:
  discount_amount = .15
elif "volume" in customer_29876["discounts"]:
  discount_amount = .10
elif "standard" in customer_29876["discounts"]:
  discount_amount = .05