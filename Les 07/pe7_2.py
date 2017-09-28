woord=''
while len(woord) !=4:
    woord = input('Geef een string van 4 letters: ')
    print('{} heeft {} letters'.format(woord, len(woord)))
    if len(woord) == 4:
        break

print('Inlezen van correcte string: {} is geslaagd'.format(woord))
