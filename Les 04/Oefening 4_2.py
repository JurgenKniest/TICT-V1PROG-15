def rng(getallen):
    verschil = max(getallen) - min(getallen)
    return verschil

getallen = [4, 0, 1, -2]
res = rng(getallen)

print(res)