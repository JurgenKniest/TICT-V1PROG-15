import csv

with open('inloggers.csv', 'w',newline='')as myCSVFile:
    writer = csv.writer(myCSVFile, delimiter=';')
    while True:
        naam = input("Wat is je achternaam?: ")
        if naam == 'einde':
            break
        voorl = input("Wat is/zijn je voorletter(s)?: ")
        gbdatum = input("Wat is je geboortenaam?: ")
        email = input("Wat is je email?: ")
        writer.writerow((voorl,naam,gbdatum,email))