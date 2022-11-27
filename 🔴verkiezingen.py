lijst = []
maxlengtelijst = []

while maxlengtelijst != 0:
    item = input('Wat is de naam van de partij?: ')
    lijst.append(item)
    if item =='Uitslag!':
        break

print('De winaar is: ', (lijst))