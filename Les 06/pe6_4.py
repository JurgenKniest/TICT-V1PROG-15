studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]
lijst1 = []

def gemiddelde_per_student(studentencijfers):
    for cijferlijst in studentencijfers:
        antw = sum(cijferlijst)/len(cijferlijst)
    return antw

#def gemiddelde_van_alle_studenten(studentencijfers):

# return antw
print(gemiddelde_per_student(studentencijfers))
#print(gemiddelde_van_alle_studenten(studentencijfers))

