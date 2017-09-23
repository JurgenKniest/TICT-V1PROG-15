def convert(gradenCelcius):
    gradenFahrenheit = gradenCelcius *1.8 + 32
    return gradenFahrenheit

def table():
    for x in range(-30, 50, 10):
        print('{:6} {:6}'.format(convert(x),float(x)))

print('{:9}{:9}'.format('   F',' C'))
table()