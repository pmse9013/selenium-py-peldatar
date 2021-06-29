# 028-as feladat

menu = ["sör", "kóla"]
print(f"Itallap : {menu}")
age = int(input("Hány éves vagy? "))
drink = input("Mit iszol, sört vagy kólát ?")

if age < 18 and drink == "sör" :
    print("Sajnos nem szolgálhatok ki kiskorúakat sörrel.")
elif age > 60 and drink == "kóla" :
    print("A kóla megemelheti a vérnyomását!")
elif drink not in menu:
    print("Ez az ital nincsen az itallapon.")
else:
    print(f"Parancsoljon, itt a {drink}")
