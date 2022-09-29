from tkinter.messagebox import YES


first_name = input('What is your first name? ')
last_name = input('What is your last name? ')
# output = "Your name is, {1} {0}".format(first_name.capitalize(), last_name.capitalize())
output = f'Hello, {first_name.capitalize()} {last_name.capitalize()}'
print(output)

