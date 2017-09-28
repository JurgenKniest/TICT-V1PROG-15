week = {'ma': 'maandag', 'di': 'dindag', 'wo': 'woensdag','do': 'donderdag','vr': 'vrijdag'}

week['di'] = 'dinsdag'
week['za'] = 'zaterdag'

#for afkorting in week.keys():
#    print(afkorting)
#for langeNaam in week.values():
#    print(langeNaam)
#for beide in week.items():
#    print(beide)

for afkorting in week.keys():
    print('Afkorting: {}, lange naam: {}'.format(afkorting, week[afkorting]))