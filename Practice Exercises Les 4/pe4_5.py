def kwadraten_som(grondgetallen):
    som=0
    for x in grondgetallen:
        if x > 0:
            som = som + (x**2)
    return som


resultaat =  kwadraten_som([5,6,-4,7])
print(resultaat)
