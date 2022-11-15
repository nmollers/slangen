operation = input('''
Maak een keuze voor je som:
+ voor plus
- voor min
* voor keer
/ voor gedeeld door
= voor getypt cijfer
''')

number_1 = int(input('uw eerste cijfer: '))
number_2 = int(input('uw tweede cijfer: '))

# + som
if operation == '+':
    print('{} + {} = '.format(number_1, number_2))
    print(number_1 + number_2)

# - som
elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

# * som
elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

# / som
elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

# = som
elif operation == '=':
    print(number_1)

# bij een fout antwoord
else:
    print('je hebt geen juiste keuze gemaakt, herstart de rekenmachine opnieuw.')
