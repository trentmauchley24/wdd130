#Begin gathering input data from user

adjective = input('Please list an adjective: ')
animal = input('Please list an animal: ')
verb0 = input('Please list a verb: ')
exclamation = input('Please list an exclamation: ')
verb1 = input('Please list a verb: ')
verb2 = input('Please list a verb: ')
emotion = input('Please list an emotion: ')
action = input('Please put an action: ')
#Begin applying the user input to the Madlib.
print('')
print('Your story is:')
print('')
print(f'The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb0} down the hallway. \"{exclamation.capitalize()}!\" I yelled. But all I could think to do was to {verb1} over and over. Miraculously, that caused it to stop, but not before it tried to {verb2} right in front of my family. That caused me to feel so...so {emotion.upper()}! I couldn\'t stop thinking about it until later when I {action} to finish the day. Man what a day.')
print("")
#Tried out an if...else statement to get some practice in and get some more user input.
#Please let me know your thoughts.
user_fun = input('On a scale of one to five how was the Madlib? ')
if int(user_fun) >= 3:
    print('We are so glad you had fun! Thank you for your time.')
    exit
else:
    print('Sorry to hear that. We hope you fun next time. Thank you!')
    exit

