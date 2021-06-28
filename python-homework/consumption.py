# Feladat: Python Adatok és változók feladat
# 2

road = int(input("Hány litert fogyaszt az autód országúton? "))
city = int(input("Hány litert fogyaszt az autód városban? "))
road_distance = int(input("Hány kilómétert fogsz országúton megtenni?" ))
city_distance = int(input("Hány kilométert fogsz városban megtenni?" ))
price_of_fuel = int(input("Mennyibe kerül egy liter benzin (forint)? "))



one_way = ((road_distance / 100) * road) + ((city_distance / 100) * city)
round = one_way * 2

price_of_round = int(round * price_of_fuel)

print(f"Az autód {one_way} litert fogyaszt az odaút során.")
print(f"Az autód {round} litert fogyaszt az oda-vissza út során.")
print(f"A benzin {price_of_round} forintba kerül a teljes útra. ")


