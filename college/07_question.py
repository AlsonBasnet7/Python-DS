names = []
prices = []
quantities = []

while True:
    name = input("Enter item name: ")
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))

    names.append(name)
    prices.append(price)
    quantities.append(qty)

    more = input("Add more? (yes/no): ")
    if more == "no":
        break

subtotal = 0

for i in range(len(names)):
    total = prices[i] * quantities[i]
    subtotal = subtotal + total

vat = subtotal * 0.13
final_total = subtotal + vat

print("Subtotal:", subtotal)
print("VAT:", vat)
print("Final Total:", final_total)