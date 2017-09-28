som = 0
getallenlijst= []
while True:
    getal = eval(input('Geef een getal: '))
    getallenlijst.append(getal)
    if getal == 0:
        break

sumlijst = (sum(getallenlijst))
lenlijst = (len(getallenlijst))
print('Er zijn {} getallen ingevoerd, de som is {}'.format(lenlijst, sumlijst))