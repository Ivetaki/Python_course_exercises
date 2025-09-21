samohlasky = 'aeiouáéíóú'
souhlasky = 'bcčdďfghjklmnňprřsštťvzžcdž'

vysledky = {'souhlasky': 0, 'samohlasky': 0}
veta = 'Zvuk řeči je produkován otevřenou konfigurací vokálního traktu'

for znak in veta:
  znak_maly = znak.lower()
  if znak.lower() in samohlasky or znak.lower() in souhlasky:
    if znak_maly in samohlasky:
      vysledky['samohlasky'] += 1
    else:
      vysledky['souhlasky'] += 1

print(f"Počet souhlásek: {vysledky['souhlasky']} | Počet samohlásek: {vysledky['samohlasky']}")