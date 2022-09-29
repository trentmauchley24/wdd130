print('Please enter the following information:')
print('')
#It is now ready to receive user input.
first = input('First name: ')
last = input('Last name: ')
email = input('Email address: ')
phone = input('Phone number: ')
title = input('Job title: ')
id = input('ID number: ')
hair = input('Hair color: ')
eye = input('Eye color:')
start_date = input('Start date of employment (mm/dd/yyyy): ')
training = input('Have you completed the advanced training (y/n)? ')
adv_training = training.capitalize()

hair_color = hair.capitalize()[0:3] #Setting parameters for characters entered in for hair and eye color.
eye_color = eye.capitalize()[0:3]

print('')
print('The ID card is: ')
#fun little thing is that I used a multiplier to give the amount of dots for the printed ID card.
print('-'*75)
#Prints the information that was requested from the employee.
print(f'{last.upper()}, {first.capitalize()}')
print(title.title())
print(f'ID: {id}' )
print(f"{email.lower()}")
print(phone)
#Prints the additional information that was asked.
#For the additional information I used a fomat for spacing that gives 25 spaces in between the information
#given.
#I gave another example of the spacing format that can be used.
print(f"{'Hair color:'+ hair_color:<25}{'Eye color: ' + eye_color}")
#print(f"{'Hair color:'+ hair_color:25}{'Eye color: ' + eye_color}")
print(f"{'Start date: '+ start_date:<25}{'Trained: ' + adv_training}")
#print(f"{'Start date: '+ start_date:25}{'Trained: ' + adv_training}")
print('-'*75) 