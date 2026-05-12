product = "Laptop"
price = 666.99
quantity = 10

total =price * quantity
print("Invoice Details")
print("-" * 20)
print(f"Item: {product}")
print(f"Unit Price: ${price:.2f}")
print(f"Quantity: {quantity}")
print(f"Total: ${total:.2f}")   

#output:
#Invoice Details
#--------------------
#Item: Laptop
#Unit Price: $666.99
#Quantity: 10
#Total: $6669.90
    