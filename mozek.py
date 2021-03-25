import random
from time import sleep
from os import system
mesice = ["leden","únor","březen","duben","květen","červen","červenec","srpen","září","říjen","listopad","prosinec"]
kontrola = []
def zamichej(slovo):
	slovo = list(slovo)
	vysledek = []
	vysledek.append(slovo[0])
	prostredek = slovo[1:-1]
	random.shuffle(prostredek)
	vysledek.extend(prostredek)
	vysledek.append(slovo[-1])
	zamichane = ""
	for i in range(len(vysledek)):
		zamichane += vysledek[i]
	return zamichane
mesic = random.choice(mesice)
zamichaneSlovo = zamichej(mesic)
while zamichaneSlovo == mesic:
	zamichaneSlovo = zamichej(mesic)
tip = input(f"Co je {zamichaneSlovo}? Zadej: ").lower()
kontrola.append(tip==mesic)
while tip != mesic:
	tip = input(f"Co je {zamichaneSlovo}? Zadej: ").lower()
	kontrola.append(tip==mesic)
print(f"Udělal jsi {len(kontrola) - 1} chyb.")
sleep(5)
system("cls")

