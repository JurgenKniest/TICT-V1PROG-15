infile = open('hardlopers.txt', 'w')
count= 0

while count < 10:
    naam = input('Wat is je naam?: ')
    import datetime
    vandaag = datetime.datetime.today()
    s = vandaag.strftime("%a %d %b %Y, %H:%M:%S")
    infile.write('{}{}{}\n'.format(s,' ', naam))
    count = count+1