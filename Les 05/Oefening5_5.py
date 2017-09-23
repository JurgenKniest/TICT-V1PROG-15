infile = open('Voorbeeld5_5.txt', 'r')
inhoud = infile.read()
infile.close()
print(inhoud)

infile = open('Voorbeeld5_5.txt', 'r')
inhoud1 = infile.read()
infile.close()
inhoud2 = inhoud1.split()
print(inhoud2)

infile = open('Voorbeeld5_5.txt', 'r')
inhoud3 = infile.readlines()
infile.close()
print(inhoud3)

