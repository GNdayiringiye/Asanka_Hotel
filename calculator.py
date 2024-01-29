print('input')\

price = input('Charge for food:')
Tip = (float(price)*18/100)
Sales_Tax = (float(price)*7/100)


print('output')
print('Tip = :' , Tip)
print('Sales Tax = :' , Sales_Tax)
print('Grand Total = ', float(price) + Tip + Sales_Tax)
