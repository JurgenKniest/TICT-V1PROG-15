try:
    bedrag = 4356
    aantal = eval(input("Geef het aantal personen: "))
    if bedrag > 0:
        print("Negatieve getallen niet toegestaan.")
    else:
        print("Prijs per persoon is {} euro.".format(bedrag/aantal))
except ZeroDivisionError:
    print("Delen door 0 mag niet.")
except NameError:
    print("Graag cijfers invoeren.")
except:
    print("Onjuiste invoer.")