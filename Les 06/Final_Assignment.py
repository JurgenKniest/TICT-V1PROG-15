def nieuwe_kluis():
    kluisnummers = []
    for i in range(1, 13):
        kluisnummers.append(i)

    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()


    for kluis in kluizendata:
        gegevensvan1kluis = kluis.split(';')
        stringnummer = gegevensvan1kluis[0]
        nummer = int(stringnummer)
        kluisnummers.remove(nummer)

    if len(kluisnummers) > 0:
        nieuwkluisnummer = kluisnummers[0];
        print('Je kluisnummer is {}'.format(nieuwkluisnummer))
        code = input('Voer een code in: ')
        outfile = open('kluizen.txt', 'a')
        outfile.write('{};{}\n'.format(nieuwkluisnummer, code))
        outfile.close()
    else:
        print('Er is geen kluis meer beschikbaar')

def kluis_teruggeven():
    infile = open('kluizen.txt', 'r')
    kluizendata = infile.readlines()
    infile.close()
    stringnummer = input('Wat is het nummer van je kluis: ')
    code = input('Wat is de code van je kluis: ')
    nieuwekluizendata = []

    for kluis in kluizendata:
        datavan1kluis = kluis.split(';')
        stringkluisnummer = datavan1kluis[0]
        kluiscode = datavan1kluis[1].strip()
        gegevenscorrect = (stringkluisnummer == stringnummer) and (kluiscode == code)
        if not gegevenscorrect:
            nieuwekluizendata.append(stringkluisnummer + ';' + kluiscode)

    outfile = open('kluizen.txt', 'w')
    for i in range(0, len(nieuwekluizendata)):
        outfile.write(nieuwekluizendata[i] + '\n')
    outfile.close()