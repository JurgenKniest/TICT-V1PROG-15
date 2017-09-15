def Efteling_attractie(lang_genoeg):
    if lang_genoeg >= 120:
        return 'Je bent lang genoeg voor de attractie!'
    else:
        return 'Sorry, je bent te klein..'

lengte = eval(input('Hoe lang (in cm) ben je?: '))
resultaat = (Efteling_attractie(lengte))
print (resultaat)