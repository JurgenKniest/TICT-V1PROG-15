invoer = "5-9-7-1-7-8-3-2-4-8-7-9"
losseinvoer = invoer.split('-')
losseinvoer.sort()
maxgetal = max(losseinvoer)
mingetal = min(losseinvoer)
lengetal = len(losseinvoer)
lijst1 = []

for x in losseinvoer:
    x = int(x)
    lijst1.append(x)

sumgetal = sum(lijst1)
average = sumgetal/lengetal

print('Gesorteerde lijst van ints: {}'.format(lijst1))
print('Grootste getal: {} en Kleinste getal: {}'.format(maxgetal, mingetal))
print('Aantal getallen: {} en Som van de getallen: {}'.format(lengetal, sumgetal))
print('Gemiddelde: {}'.format(average))

