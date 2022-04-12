print ("Welcome to total price calculator")

item = 0;
cart = []

print ("Enter item's price or 0/less to get results")

while True:
  item = float(input("Enter price/0:- "))
  
  if item > 0:
    cart.append(item)
  else:
    break

print ("The total price = ${:,.2f}".format(sum(cart)))
print ("Bye")
