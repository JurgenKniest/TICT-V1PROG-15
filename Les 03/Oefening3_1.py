naam = (input ('Wat is je naam?: '))
leeftijd = eval(input ('Hoe oud ben je?: '))

if leeftijd > 17:
    print (naam + ', je mag stemmen!')
else:
    print (naam + ', je mag nog niet stemmen...')
