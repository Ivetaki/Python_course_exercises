jmeno = "Marek"
heslo = "1234"
uzivatele = {
    "Marek": "1234",
    "Petra": "abcd"
}
if jmeno in uzivatele and heslo == uzivatele[jmeno]:
  zprava = f"Ahoj {jmeno}, vítej v aplikaci! Pokračuj..."
else:
  zprava = f"Uživatelské jméno nebo heslo nejsou v pořádku!"
print("Výstup: ", zprava)