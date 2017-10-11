import csv
with open('artikel.csv','r') as myCSVFile:
    reader = csv.DictReader(myCSVFile, delimiter=';')
    duurste_artikel = 0
    duurste_naam = ''
    kleinste_voorraad = 1000
    kleinste_artikelnummer= ''
    totaalVoorraad= 0
    for row in reader:
        prijs = float(row['Prijs'])
        if prijs > duurste_artikel:
            duurste_artikel = prijs
            duurste_naam = row['Naam']
        voorraad = int(row['Voorraad'])
        if voorraad < kleinste_voorraad:
            kleinste_voorraad = voorraad
            kleinste_artikelnummer = row['Artikelnummer']
        totaalVoorraad += int(voorraad)
    print("Het duurste artikel is {} en die kost {} Euro.".format(duurste_naam,duurste_artikel))
    print("Er zijn slechts {} exemplaren in voorraad van het product met nummer {}.".format(kleinste_voorraad, kleinste_artikelnummer))
    print("In totaal hebben wij {} producten in ons magazijn liggen".format(totaalVoorraad))