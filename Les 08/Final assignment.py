def inlezen_beginstation(stations):
    beginstation=input("Geef beginstation: ")
    while beginstation not in stations:
        beginstation = input("Niet goed, geef een ander beginstation: ")
    return beginstation

def inlezen_eindstation(stations, beginstation):
    eindstation = input("Geef eindstation: ")
    while eindstation not in stations:
        eindstation = input("Niet goed, geef een ander eindstation: ")
    while stations.index(eindstation) <= stations.index(beginstation):
        eindstation = input("Geef nieuw eindstation: ")
    return eindstation

def omroepen_reis(stations, beginstation, eindstation):
    nummerB = stations.index(beginstation)+1
    nummerE = stations.index(eindstation)+1
    print("Het beginstation {} is het {}e station in het traject".format(beginstation, nummerB))
    print("Het eindstation {} is het {}e station in het traject".format(eindstation, nummerE))
    afstand = nummerE - nummerB
    print("De afstand bedraagt {} station(s).".format(afstand))
    prijs = 5*afstand
    print("De prijs van de kaartjes is {} euro.".format(prijs))
    print("Jij stapt in de trein in: {}".format(beginstation))
    for i in range(nummerB, nummerE -1):
        print("-",stations[i])
    print("Jij stapt uit in: {}".format(eindstation))

stations = ['Schagen', 'Heerhugowaard',..., 'Sittard', 'Maastricht']
beginstation = inlezen_beginstation(stations)
eindstation = inlezen_eindstation(stations, beginstation)
omroepen_reis(stations, beginstation, eindstation)
