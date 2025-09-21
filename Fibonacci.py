x = 0
y = 1
vysledky = []
delka_rady = 15

while len(vysledky) < delka_rady:
    vysledky.append(x)
    novy = x + y
    x = y
    y = novy

print(vysledky)