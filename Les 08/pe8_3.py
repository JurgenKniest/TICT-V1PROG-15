def code(asciiwaarde):
    legestring=''
    for i in asciiwaarde:
        asciiNaam =ord(i)
        asciiNaam += 3
        legestring += chr(asciiNaam)
    print(legestring)

code("RutteAlkmaarDen Helder")
