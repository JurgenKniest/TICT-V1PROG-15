def new_password (oldpassword, newpassword):
    if oldpassword != newpassword and len(newpassword) >= 6 :
        for c in newpassword:
            if c in '0123456789':
                return True
        return False
    else:
        return False

#correcte wachtwoorden
res = new_password ('vakProg17', 'python17')
print(res)

#hetzelfde wachtwoord
print (new_password('huProg17', 'huProg17'))

#Te kort nieuw wachtwoord
print (new_password('vakProg17', 'Pro17'))

#Nieuw wachtwoord zonder cijfer -> False
print (new_password('vakProg17', 'HuVakProg'))


#oldpassword = input('oude wachtwoord: ')
#newpassword = input('nieuwe wachtwoord: ')
#print (res)

