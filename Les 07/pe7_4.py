#infile = open('ticker_symbols.txt', 'r')
#openbestand = infile.read()
#splitbestand = openbestand.split('\n')
dictionary = {}

def ticker(filename):
    infile = open(filename, 'r')
    openbestand = infile.readlines()
    for bedrijf in openbestand:
        bedrijf1 = bedrijf.rstrip('\n').split(':')
        dictionary[bedrijf1[0]] = bedrijf1[1]
    return dictionary

def tickername(bedrijf):
    ticker('ticker_symbols.txt')
    print(dictionary[bedrijf])
    print(bedrijf)

bedrijf = input('Bedrijf of afkorting: ')
tickername(bedrijf)
