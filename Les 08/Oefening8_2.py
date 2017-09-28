set1 = set()
set2 = set()
set3 = set()

for getal in range(1, 1000):
    set3.add(getal)
    if getal % 3 == 0:
        set1.add(getal)
    if getal % 7 == 0:
        set2.add(getal)

print(set1&set2)
print(set2|set2)
print(set1-set2)
print(set3-set1-set2)