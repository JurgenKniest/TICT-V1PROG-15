def ticker():
    infile = open('ticker_symbols.txt', 'r')
    regels = infile.readlines()
    tickerdict = {}
    for regel in regels:
        tickerregel = regel.split(':')
        sleutel = tickerregel[0]
        waarde = tickerregel[1].strip()
        tickerdict[sleutel] = waarde
    return tickerdict

ticker()
print(ticker())

def tickername():
    tickerbestand = ticker()


