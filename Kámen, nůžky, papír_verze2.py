import random
moznosti = ['kamen', 'nuzky', 'papir']

# vygenerování tahů
hrac_volby = [random.choice(moznosti) for _ in range(3)]
pocitac_volby = [random.choice(moznosti) for _ in range(3)]

# pravidla vítězství hráče
vitez = {
    ("kamen", "nuzky"),
    ("nuzky", "papir"),
    ("papir", "kamen"),
}

# vyhodnocení jednotlivých her
for hrac, pocitac in zip(hrac_volby, pocitac_volby):
    if hrac == pocitac:
        vysledek = "Remíza!"
    elif (hrac, pocitac) in vitez:
        vysledek = "Vyhrává hráč!"
    else:
        vysledek = "Vyhrává počítač!"
    print(f"Hráč: {hrac:6}  Počítač: {pocitac:6}  → {vysledek}")