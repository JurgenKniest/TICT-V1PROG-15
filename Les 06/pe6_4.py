studentencijfers = [ [95, 92, 86],[66, 75, 54],[89, 72, 100],[34, 0, 0] ]


def gemiddelde_per_student(studentencijfers):
    antw = []
    for cijferlijst in studentencijfers:
        gemiddelde = (sum(cijferlijst)/len(cijferlijst))
        antw.append(gemiddelde)
    return antw

def gemiddelde_van_alle_studenten(studentencijfers):
    avgstudent = gemiddelde_per_student(studentencijfers)
    antw = int(sum(avgstudent)/len(avgstudent))
    return antw

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))