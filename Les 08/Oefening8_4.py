string = input('Voer een string in: ')

for letter in string:
    code = ord(letter)
    print('{:2} {:3} {:4b} {:4x}'.format(letter, code, code, code))
