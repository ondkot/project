import datetime
def naDny(datum):
	denNarozeni = int(datum[0:2])
	mesicNarozeni = int(datum[3:5])
	x = mesicNarozeni
	rokNarozeni = int(datum[6:-1] + datum[-1])
	prestupne = rokNarozeni // 4
	jePrestupny = bool(rokNarozeni % 4)
	dny = prestupne * 366
	rokNarozeni -= prestupne
	dny += rokNarozeni * 365
	dny += denNarozeni
	if x == 1:
		dny += 31
	if x == 2:
		if jePrestupny:
			dny += 29
		else:
			dny += 28
	if x == 3:
		dny += 31
	if x == 4:
		dny += 30
	if x == 5:
		dny += 31
	if x == 6:
		dny += 30
	if x == 7:
		dny += 31
	if x == 8:
		dny += 31
	if x == 9:
		dny += 30
	if x == 10:
		dny += 31
	if x == 11:
		dny += 30
	if x == 12:
		dny += 31
	return int(dny)
narozeni = naDny(input("Zadej datum narození ve tvaru dd.mm.yyyy: "))
dnes = naDny((datetime.date.today()).strftime("%d.%m.%Y"))
print(f"Je ti {((dnes - narozeni) / 365) - 0.5} let.")



