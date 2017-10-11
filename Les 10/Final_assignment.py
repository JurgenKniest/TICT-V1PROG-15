import xmltodict

def processXML(filename):
    with open(filename) as myXMLFile:
        filestring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary

stationsdict = processXML('FA.xml')
stations = stationsdict['Stations']['Station']

print("\nDit zijn de codes en types van de 4 stations: ")
for station in stations:
    print('{:4} - {}'.format(station['Code'], station['Type']))

print("\nDit zijn alle stations met een of meer synoniemen: ")
for station in stations:
    if station["Synoniemen"] != None:
        print('{:4} - {}'.format(station['Code'], station["Synoniemen"]["Synoniem"]))

print("\nDit is de lange naam van elk station: ")
for station in stations:
    print('{:4} - {}'.format(station['Code'], station['Namen']['Lang']))