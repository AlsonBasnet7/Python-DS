name1=str(input("Enter the first product name"))
name2=str(input("Enter the second  product name"))
name3=str(input("Enter the third prodcut name"))
item1=float(input('Enter the price of first item'))
item2=float(input("Enter the price of second item"))
item3=float(input("Enter the price of third item"))
total_cost=item1+item2+item3
print("The total cost of three items is ",total_cost)
tax_amout=(13/100)*total_cost
print("The taxed amount is",tax_amout)
final_total=total_cost+tax_amout
print("The dinal total is",final_total)
nameraprice={name1:item1,name2:item2,name3:item3}
print(nameraprice)
print(f"{total_cost} is the sub total cost. {tax_amout} is the tax amount.{final_total} is the final total")