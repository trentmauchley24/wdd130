first_name = input('What is your first name? ')
last_name = input('What is your last name?')
# output = 'My name is {1}, {0} {1}. '.format(first_name.capitalize(), last_name.capitalize())
output = f'My name is {last_name.capitalize()}, {first_name.capitalize()} {last_name.capitalize()}'
print(output)