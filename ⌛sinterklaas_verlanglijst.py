lijst = []
maxlengtelijst = []

while maxlengtelijst != 0:
    item = input('Wat wil je op je verlanglijst zetten?: ')
    lijst.append(item)
    if item =='Klaar!':
        break

print ('Dit is je verlanglijst voor sinterklaas:')
print(sorted(lijst, key=str.casefold))