def scitat(scitanec1,scitanec2):
	vysledek = scitanec1 + scitanec2
	print(f"{scitanec1} + {scitanec2} = {vysledek}")
def odcitat(mensenec,mensitel):
	vysledek = mensenec - mensitel
	print(f"{mensenec} - {mensitel} = {vysledek}")
def nasobit(soucinitel1,soucinitel2):
	vysledek = soucinitel1 * soucinitel2
	print(f"{soucinitel1} * {soucinitel2} = {vysledek}")
def delit(delenec,delitel):
	vysledek = delenec / delitel
	print(f"{delenec} / {delitel} = {vysledek}")

volba = int(input("Zadej co chceš dělat(1. sčítat,2. odčítat,3. násobit,4.dělit): "))
if volba in range(0, 5):
	if volba == 1:
		a = float(input("Zadej sčítanec 1: "))
		b = float(input("Zadej sčítanec 2: "))
		scitat(a,b)

	if volba == 2:
		a = float(input("Zadej menšenec: "))
		b = float(input("Zadej menšitel: "))
		odcitat(a,b)

	if volba == 3:
		a = float(input("Zadej činitel 1: "))
		b = float(input("Zadej činitel 2: "))
		nasobit(a, b)

	if volba == 4:
		a = float(input("Zadej dělenec: "))
		b = float(input("Zadej dělitel: "))
		delit(a,b)

else:
	print("Zadej volbu 1,2,3 nebo 4.")

