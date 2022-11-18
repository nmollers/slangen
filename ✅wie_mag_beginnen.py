import random
spelers = []
speleraantal = int(input('Hoeveel spelers zijn der?: '))

for i in range (0, speleraantal):
    spelernaam = input('Voer de naam van de speler in: ')
    spelers.append(spelernaam)

random.shuffle(spelers)
print(spelers[0] + ' mag beginnen met het spel!')