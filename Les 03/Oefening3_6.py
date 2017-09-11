getallenrij = [2, 4, 6, 8, 10, 9, 7]
zoekgetal = eval(input('Welk getal?: '))
gevonden = False

for getal in getallenrij:
    if getal == zoekgetal:
         gevonden = True
if gevonden == True:
    print('Het zoekgetal zit in de lijst.')
else:
    print('Zit er niet in, jammer joh.')
