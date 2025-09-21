zadany_text = '''\
Lorem ipsum dolor sit amet, consectetur adipiscing
elit. Mauris vulputate lacus id eros consequat tempus.
Nam viverra velit sit amet lorem lobortis, at tincidunt
tiger123@email.cz auctor massa molestie at. Nunc 
tristique fringilla congue. Donec ante diam cnn@info.com,
dapibus lacinia vulputate vitae, ullamcorper in justo.
vitae massa. Cras abc@gmail.com vel libero felis.
In augue elit, porttitor nec molestie quis, auctor
a quam. Quisque b2b@money.fr pretium dolor et tempor
luctus lacinia risus. Maecenas posuere leo sit amet
spam@info.cz. elit tincidunt maximus. Aliquam erat
volutpat. Donec eleifend felis at leo ullamcorper
fringilla est. Maecenas gravida turpis nec ultrices
aliquet.'''
def je_email(slovo: str) -> bool:
  if "@" in slovo:
    return True
  else:
    return False

def uloz_emailove_adresy(text: str, kontrola) -> set:
  emailove_adresy = set()
  for slovo in text.split():
    ciste = slovo.strip(",.:;")
    if kontrola(ciste):
      emailove_adresy.add(ciste)
  return emailove_adresy

vysledky = uloz_emailove_adresy(zadany_text, je_email)
print("Načtené emaily:", ", ".join(sorted(vysledky)))
