def overeenkomst(bruin,groen):
    overeen = bruin.intersection(groen)
    for station in overeen:
        print('{} zit in beide trajecten'.format(station))
    print('\n')
    return overeen


def verschil(bruin,groen):
    verschillendStation = bruin.difference(groen)
    for station in verschillendStation:
        print('{} zit alleen in het bruine traject'.format(station))
    print('\n')
    return verschillendStation


def printen(bruin,groen):
    bruinEnGroen = groen.difference(bruin)
    overeenkomst(bruin, groen)
    verschil(bruin, groen)
    for station in bruinEnGroen:
        print('{} zit alleen in het groene traject'.format(station))


bruin = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', "Helmond 't hout", 'Helmond', 'Helmond Brouwhuis', 'Deurne'}
groen = {'Boxtel', 'Best', 'Beukenlaan', 'Eindhoven', 'Geldrop', 'Heeze', 'Weert'}
printen(bruin,groen)