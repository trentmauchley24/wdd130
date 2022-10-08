import time
price_per_child = float(input('What is the price of the child\'s meal? '))
price_per_adult = float(input('what is the price of an adult\'s meal? '))
children_number = int(input('How many children are there? '))
adult_number = int(input('How many adults are there? '))
sales_tax_percent = float(input('What is the sales tax rate?'))

subtotal_of_children = price_per_child*children_number
subtotal_of_adults = price_per_adult*adult_number
subtotal_group = subtotal_of_adults+subtotal_of_children
print('\nSubtotal: $%.2f'%subtotal_group)
sales_tax_converted= sales_tax_percent/100
sales_tax=subtotal_group*sales_tax_converted
print('Sales Tax: $%.2f'%sales_tax)
total=sales_tax+subtotal_group
print('Total: $%.2f'%total)
tip=float(input('How much of a tip would you like to leave (20%, 15%, 10%, 0%, or custom?) '))
tip_total=((tip/100)*total)+total
print(f'Your total with a tip is ${tip_total:.2f} ')
payment=float(input('\nWhat is the payment amount? '))
if payment<tip_total:
    change=abs(payment-tip_total)
    print(f'Insufficient funds. Remaining balance needed to be paid: ${change:.2f}\n')
else:
    change=payment-tip_total
    print('Change: $%.2f\n'%change)
signature=input('Signature(Print Name): ')
rating=int(input('Give us a rating of 1-5. 5 being fantastic and 1 being horrible: '))
if rating >= 3:
    print('We are glad you loved it. Please come again.')
else:
        print('We are sorry you didn\'t like it please leave a review letting us know what we could do better.')
review=input('Review:')
print('Submitting review. This may take a moment.')
i=0
while i<=99:
   i+=5
   time.sleep(.5)
   print(f'%{i}')
print('Review has been submitted for review. Thank you!')





