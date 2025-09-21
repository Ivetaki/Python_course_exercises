import random
moznosti = ['kamen', 'nuzky', 'papir']
hrac_volby = [random.choice(moznosti) for _ in range(3)]
pocitac_volby = [random.choice(moznosti) for _ in range(3)]
for hrac, pocitac in zip(hrac_volby, pocitac_volby):
  if hrac == pocitac:
    vysledek = "Remíza!"
  elif (hrac == 'kamen' and pocitac == 'nuzky') \
    or (hrac == 'nuzky' and pocitac == 'papir') \
    or (hrac == 'papir' and pocitac == 'kamen'):
    vysledek = "Vyhrává hráč!"
  else:
    vysledek = "Vyhrává počítač!"
print(f"Hráč: {hrac:6}  Počítač: {pocitac:6}  → {vysledek}")