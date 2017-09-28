cijferlijst = {'Pietje': 8, 'Kareltje':7, 'Bertje':5, 'Henkie':9, 'Truusje':6,'Beppie':10,'Keesje':4,'Gijsje':8}

for cijfer in cijferlijst:
    if cijferlijst[cijfer] > 9:
        print('{} heeft godverdomme een {}!!!!!'.format(cijfer, cijferlijst[cijfer]))


