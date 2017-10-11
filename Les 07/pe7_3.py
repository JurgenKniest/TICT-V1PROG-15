cijferlijst = {'Pietje': 8.0, 'Kareltje':7.0, 'Bertje':5.0, 'Henkie':9.1, 'Truusje':6.0,'Beppie':10,'Keesje':4.0,'Gijsje':8.9}

for cijfer in cijferlijst:
    if cijferlijst[cijfer] > 9.0:
        print('{} heeft godverdomme een {}!!!!!'.format(cijfer, cijferlijst[cijfer]))