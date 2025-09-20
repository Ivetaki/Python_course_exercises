vstupni_text = "Ahoj všem, tady Engeto"
def zdvojnasob_znaky(text: str) -> str:
  zdvojene_znaky = list()
  for znak in text:
    zdvojene_znaky.append(znak * 2)
  return "".join(zdvojene_znaky)
zdvojeny_text = zdvojnasob_znaky(vstupni_text)
print(f"Zdvojené znaky: {zdvojeny_text}")