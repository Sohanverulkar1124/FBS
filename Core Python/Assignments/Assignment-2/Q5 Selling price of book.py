cost_p = int (input('Enter the book cost price :'))
discount = int (input('Enter the discount % :'))

discount_p = cost_p * discount / 100 
selling_p = cost_p - discount_p

print(f'Discount price :',selling_p)