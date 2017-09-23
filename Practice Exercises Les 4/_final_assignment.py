def standaardprijs(afstandKM):
    if afstandKM > 50:
        prijs = round(15 + 0.60*afstandKM,2)                                            #Als de afstand groter is dan 50 km zal je een startprijs hebben van 15 euro en 60 cent per kilometer betalen.
    else:
        prijs = round(0.80*afstandKM,2)                                                 #Als de afstand kleiner is dan 50 km zal de persoon 80 cent per kilometer betalen.
    if afstandKM < 0:
        prijs = int(0)                                                                  #Als de afstand kleiner dan 0 is, zal de persoon niks hoeven te betalen.
    return prijs

def ritprijs(leeftijd, weekendrit, afstandKM):
    prijs1 = standaardprijs(afstandKM)
    if weekendrit == True:
        if leeftijd <12 or leeftijd >=65:
            totaleprijs = round((prijs1/100)*65, 2)                                          #Als de persoon jonger is dan 12 en 65 of ouder is zal deze persoon 35% korting krijgen hier.
        else:
            totaleprijs = round((prijs1/ 100) * 60, 2)                                       #Als de persoon tussen 12 en 65 is zal deze persoon hier 40% korting krijgen.
    else:
        if leeftijd <12 or leeftijd >=65:                                               #Als de persoon jonger is dan 12 en 65 of ouder is zal deze persoon 30% korting krijgen hier.
            totaleprijs = round((prijs1/100)*70, 2)
        else:
            totaleprijs = (prijs1)                                                           #Als de persoon tussen 12 en 65 is zal deze persoon de volle prijs moeten betalen.
    return totaleprijs


resultaat1 = ritprijs(11, True, 40)
resultaat2 = ritprijs(12, True, 40)
resultaat3 = ritprijs(64, True, 40)
resultaat4 = ritprijs(65, True, 40)

resultaat5 = ritprijs(11, False, 40)
resultaat6 = ritprijs(12, False, 40)
resultaat7 = ritprijs(64, False, 40)
resultaat8 = ritprijs(65, False, 40)

resultaat9 = ritprijs(11, True, 60)
resultaat10= ritprijs(12, True, 60)
resultaat11= ritprijs(64, True, 60)
resultaat12= ritprijs(65, True, 60)

resultaat13= ritprijs(11, False, 60)
resultaat14= ritprijs(12, False, 60)
resultaat15= ritprijs(64, False, 60)
resultaat16= ritprijs(65, False, 60)

resultaat17= ritprijs(11, True, -50)
resultaat18= ritprijs(12, True, -50)
resultaat19= ritprijs(64, True, -50)
resultaat20= ritprijs(65, True, -50)

resultaat21= ritprijs(11, False, -50)
resultaat22= ritprijs(12, False, -50)
resultaat23= ritprijs(64, False, -50)
resultaat24= ritprijs(65, False, -50)

print('Jouw ritprijs is €',str(resultaat1), 'euro!')
print('Jouw ritprijs is €',str(resultaat2), 'euro!')
print('Jouw ritprijs is €',str(resultaat3), 'euro!')
print('Jouw ritprijs is €',str(resultaat4), 'euro!')
print(' ')
print('Jouw ritprijs is €',str(resultaat5), 'euro!')
print('Jouw ritprijs is €',str(resultaat6), 'euro!')
print('Jouw ritprijs is €',str(resultaat7), 'euro!')
print('Jouw ritprijs is €',str(resultaat8), 'euro!')
print(' ')
print('Jouw ritprijs is €',str(resultaat9), 'euro!')
print('Jouw ritprijs is €',str(resultaat10), 'euro!')
print('Jouw ritprijs is €',str(resultaat11), 'euro!')
print('Jouw ritprijs is €',str(resultaat12), 'euro!')
print(' ')
print('Jouw ritprijs is €',str(resultaat13), 'euro!')
print('Jouw ritprijs is €',str(resultaat14), 'euro!')
print('Jouw ritprijs is €',str(resultaat15), 'euro!')
print('Jouw ritprijs is €',str(resultaat16), 'euro!')
print(' ')
print('Jouw ritprijs is €',str(resultaat17), 'euro!')
print('Jouw ritprijs is €',str(resultaat18), 'euro!')
print('Jouw ritprijs is €',str(resultaat19), 'euro!')
print('Jouw ritprijs is €',str(resultaat20), 'euro!')
print(' ')
print('Jouw ritprijs is €',str(resultaat21), 'euro!')
print('Jouw ritprijs is €',str(resultaat22), 'euro!')
print('Jouw ritprijs is €',str(resultaat23), 'euro!')
print('Jouw ritprijs is €',str(resultaat24), 'euro!')