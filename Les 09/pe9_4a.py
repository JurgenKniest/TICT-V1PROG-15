import csv

with open('artikel.csv', 'w', newline='') as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    writer.writerow(('Artikelnummer','Artikelcode','Naam','Voorraad','Prijs'))
    while True:
        artikelnummer = input("Wat is het artikelnummer? ")
        if artikelnummer == 'stop':
            break
        artikelcode = input("Wat is de artikelcode? ")
        naam = input("Wat is de artikelnaam? ")
        voorraad = input("Wat is de voorraad? ")
        prijs = input("Wat is de prijs? ")
        writer.writerow((artikelnummer, artikelcode, naam, voorraad, prijs))
