cijferICOR = 7
cijferPROG = 9
cijferCSN = 6
gemiddelde = round((cijferICOR + cijferPROG +cijferCSN)/3,1)
beloning = (cijferICOR + cijferPROG + cijferCSN) *10
overzicht = ('Mijn cijfers (gemiddeld een) ' + str(gemiddelde) + ' leveren een beloning van ' + str(beloning) + ' euro op!')
print(overzicht)