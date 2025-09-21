vyska = 1.75 #vyska v metrech
vaha = 82 #vaha v kilogramech
jmeno = "Radek"
bmi = vaha / vyska**2
print("Jméno:", jmeno, "- BMI:", round(bmi, 2))

if bmi < 18.5:
    kategorie = "Podvýživa"
elif 18.5 <= bmi <= 24.9:
    kategorie = "Zdravá váha"
elif 25 <= bmi <= 29.9:
    kategorie = "Mírná nadváha"
elif 30 <= bmi <= 39.9:
    kategorie = "Obezita"
else:
    kategorie = "Těžká obezita"

print(f"Jméno: {jmeno}, kategorie: {kategorie}")