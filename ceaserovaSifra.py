volba = int(input("Co chceš dělat?(1.šifrovat,2.dešifrovat): "))
if volba == 1:
	mala = "abcdefghijklmnopqrstuvwxyz"
	velka = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	sifra = input("Zadej text k zašifrování: ").upper()
	klic = input("Zadej šifrovací klíč: ")
	while (klic not in mala and klic not in velka) or len(klic) != 1:
		print("Klíč musí být jedno písmeno.")
		klic = input("Zadej šifrovací klíč: ")
	klic = klic.upper()
	klic = velka.find(klic)
	vysledek = []
	for i in range(0,len(sifra)):
		pomocna = velka.find(sifra[i])
		pomocna = pomocna + klic
		while pomocna > 25:
			pomocna -= 25
		vysledek.append(velka[pomocna])
	for j in range(0,len(vysledek)):
		print(vysledek[j],end="")
elif volba == 2:
	mala = "abcdefghijklmnopqrstuvwxyz"
	velka = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	sifra = input("Zadej text k dešifrování: ").upper()
	klic = input("Zadej šifrovací klíč: ")
	while (klic not in mala and klic not in velka) or len(klic) != 1:
		print("Klíč musí být jedno písmeno.")
		klic = input("Zadej šifrovací klíč: ")

	klic = klic.upper()
	klic = velka.find(klic)
	vysledek = []
	for i in range(0,len(sifra)):
		pomocna = velka.find(sifra[i])
		pomocna -= klic
		while pomocna < 0:
			pomocna += 25
		vysledek.append(velka[pomocna])
	for j in range(0,len(vysledek)):
		print(vysledek[j],end="")
else:
	while volba not in range(1,3):
		print("Zadej 1 nebo 2.")
		if volba == 1:
			mala = "abcdefghijklmnopqrstuvwxyz"
			velka = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
			sifra = input("Zadej text k zašifrování: ").upper()
			klic = input("Zadej šifrovací klíč: ")
			while (klic not in mala and klic not in velka) or len(klic) != 1:
				print("Klíč musí být jedno písmeno.")
				klic = input("Zadej šifrovací klíč: ")
			klic = klic.upper()
			klic = velka.find(klic)
			vysledek = []
			for i in range(0,len(sifra)):
				pomocna = velka.find(sifra[i])
				pomocna = pomocna + klic
				while pomocna > 25:
					pomocna -= 25
				vysledek.append(velka[pomocna])
			for j in range(0,len(vysledek)):
				print(vysledek[j],end="")
		elif volba == 2:
			mala = "abcdefghijklmnopqrstuvwxyz"
			velka = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
			sifra = input("Zadej text k dešifrování: ").upper()
			klic = input("Zadej šifrovací klíč: ")
			while (klic not in mala and klic not in velka) or len(klic) != 1:
				print("Klíč musí být jedno písmeno.")
				klic = input("Zadej šifrovací klíč: ")

		klic = klic.upper()
		klic = velka.find(klic)
		vysledek = []
		for i in range(0,len(sifra)):
			pomocna = velka.find(sifra[i])
			pomocna -= klic
			while pomocna < 0:
				pomocna += 25
			vysledek.append(velka[pomocna])
		for j in range(0,len(vysledek)):
			print(vysledek[j],end="")
