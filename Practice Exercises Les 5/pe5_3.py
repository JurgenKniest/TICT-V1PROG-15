infile = open('kaartnummers.txt', 'r')
regels = infile.read()
infile.close()
losseregels = regels.split('\n')

#wat moet ik hebben?
aantal = 0
grootste_nr = 0
regelnummer = 0
count = 0

#hoe kom ik er aan?

#doorloop de lijst met waarden
for regel in losseregels:
    count = count + 1
    #controleer of de waarde brukerbaar is
    if len(regel) > 0:
        kaart_naam_combinatie = regel.split(', ')
        #vergelijk de waarde met de hoogste waarde
        if eval(kaart_naam_combinatie[0]) > grootste_nr:
            #wanner de waarde hoger is, overschrijf de oude waarde
            grootste_nr = eval(kaart_naam_combinatie[0])
            regelnummer = count

print('Deze file telt {} regels.'.format(count))
print('Het grootste kaartnummer is: {} en dat staat op regel {}'.format(grootste_nr, regelnummer))