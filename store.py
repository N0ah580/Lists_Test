# Programmer: Noah
# Description: Store_Test


#Ask for the amount of item wanted to purchase

amount = int(input ("How many items are you purchasing? "))

count = 1
subtotal = 0

#Create a function to ask for and calculate prices
while count <= amount:
    price = float(input ("Enter item 1 price: "))
    subtotal += price
    count += 1

#print combined total and apply tax
print (f"Subtotal: ${subtotal:,.2f}")
tax = subtotal * 0.13
print (f"Tax: ${tax:,.2f}")
total = subtotal + tax
print (f"Total: ${total:,.2f}")

