def namen():
    #lege lijst aanmaken
    namenlijst = {}
    while True:
        #naam invoeren:
        naam = input("Volgende naam: ")
        #als de naam al in de lijst zit, tel er een bij op
        if naam in namenlijst.keys():
            namenlijst[naam] += 1
        #als de naam nog niet in de lijst staat en hij leeg is, stop het proces.
        elif len(naam) == 0:
            break
        #als de naam er nog niet in zit en niet leeg is, voeg de naam toe met de waarde 1
        else:
            namenlijst[naam] = 1
    #roep de lijst aan
    return namenlijst

#print de functie
print(namen())