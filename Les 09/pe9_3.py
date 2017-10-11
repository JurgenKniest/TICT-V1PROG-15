import csv

with open ('gamers.csv', 'r') as myCSVFile:
    reader = csv.reader(myCSVFile, delimiter=';')
    hoogstescore = 0
    for row in reader:
        score = int(row[2])
        if score > hoogstescore:
            hoogstescore = score
            hoogste_naam = row[0]
            hoogste_datum = row[1]
print("De hoogstescore is: {}. Op {} behaald door: {}.".format(hoogstescore, hoogste_datum, hoogste_naam))