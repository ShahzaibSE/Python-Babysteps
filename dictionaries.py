customer7890 = {"firstname": "Shahzaib", "lastname":"Noor", "age": "25", "zip": "74600"}
del customer7890["zip"]
print(f"Customer Info: {customer7890}")
#
firstname_customer = customer7890.get("firstname")
print(firstname_customer)
customer7890.update({"country" : "Pakistan"})
print("Updated customer Info")
print(customer7890)