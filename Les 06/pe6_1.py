maand = eval(input('Welk maandnummer is het?: '))

def seizoen(maand):
    if maand in range(3,6):
        return 'Lente'
    elif maand in range(6, 9):
        return'Zomer'
    elif maand in range (9, 12):
        return 'Herfst'
    else:
        return 'Winter'

print(seizoen(maand))