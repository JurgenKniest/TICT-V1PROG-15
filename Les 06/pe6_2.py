lijst = eval(input('Geef een lijst met minimaal 10 strings: '))
lijst1 =[]
for string in lijst:
    if len(string) == 4:
        lijst1.append(string)

print('De nieuw-gemaakte lijst met alle vier-letter strings is:\n',(lijst1))