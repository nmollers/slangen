spelerscore = []
speleraantal = int(input('Hoeveel spelers zijn der?: '))

for i in range (0, speleraantal):
    speler = (input('Hoeveel punten heeft deze speler?: '))
    spelerscore.append(speler)

print(sorted(spelerscore, reverse=True))