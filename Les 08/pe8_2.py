def monopolyworp():
    import random
    gelijkeworp = 0
    aantalworpen = 0
    while True:
        dobbelsteen1 = random.randrange(1, 7)
        dobbelsteen2 = random.randrange(1, 7)
        count = dobbelsteen2 + dobbelsteen1
        aantalworpen += 1
        if dobbelsteen1 != dobbelsteen2:
            print('{} + {} = {}'.format(dobbelsteen2,dobbelsteen1, count))
            break
        elif dobbelsteen2 == dobbelsteen1:
            print('{} + {} = {} (dubbel)'.format(dobbelsteen2, dobbelsteen1, count))
            gelijkeworp += 1
        elif gelijkeworp == 3:
            print('{} + {} = (direct naar gevangenis)'.format(dobbelsteen2, dobbelsteen1))
            
monopolyworp()
