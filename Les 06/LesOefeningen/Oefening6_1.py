lengte = eval(input('Wat is je lengte?: '))
gewicht = eval(input('Hoeveel weeg je?: '))
BMI = (gewicht/lengte**2)

if BMI <= 18.5:
    print ('ondergewicht')
elif BMI >18.5 and BMI >= 25:
    print('normaal')
else:
    print('overgewicht')