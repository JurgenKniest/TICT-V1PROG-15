vraag = input('Voer een willekeurige zin in: ')
vraag1 =vraag.split()
acroniem = ''

for i in vraag1:
    acroniem = acroniem+i[0].capitalize()

print(acroniem)