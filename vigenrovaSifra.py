volba = int(input("Co chceš dělat?(1.šifrovat,2.dešifrovat): "))
if volba == 1:
	mala = "abcdefghijklmnopqrstuvwxyz"
	velka = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	sifra = input("Zadej text k zašifrování: ").upper()
	klic = list(input("Zadej šifrovací klíč: ").upper())
	for i in range(len(klic)):
		klic[i] = velka.find(klic[i])
	klic = klic * 100
	vysledek = []
	for j in range(0,len(sifra)):
		pomocna = velka.find(sifra[j])
		pomocna = pomocna + klic[j]
		while pomocna > 25:
			pomocna -= 25
		vysledek.append(velka[pomocna])
	for k in range(0,len(vysledek)):
		print(vysledek[k],end="")
elif volba == 2:
	mala = "abcdefghijklmnopqrstuvwxyz"
	velka = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	sifra = input("Zadej text k dešifrování: ").upper()
	klic = list(input("Zadej šifrovací klíč: ").upper())
	for i in range(len(klic)):
		klic[i] = velka.find(klic[i])
	klic = klic * 100
	vysledek = []
	for j in range(0,len(sifra)):
		pomocna = velka.find(sifra[j])
		pomocna = pomocna - klic[j]
		while pomocna < 0:
			pomocna += 25
		vysledek.append(velka[pomocna])
	for k in range(0,len(vysledek)):
		print(vysledek[k],end="")
else:
	while volba not in range(1,3):
		print("Zadej 1 nebo 2.")
		volba = int(input("Co chceš dělat?(1.šifrovat,2.dešifrovat): "))
		if volba == 1:
			mala = "abcdefghijklmnopqrstuvwxyz"
			velka = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
			sifra = input("Zadej text k zašifrování: ").upper()
			klic = list(input("Zadej šifrovací klíč: ").upper())
			for i in range(len(klic)):
				klic[i] = velka.find(klic[i])
			klic = klic * 100
			vysledek = []
			for j in range(0,len(sifra)):
				pomocna = velka.find(sifra[j])
				pomocna = pomocna + klic[j]
				while pomocna > 25:
					pomocna -= 25
				vysledek.append(velka[pomocna])
			for k in range(0,len(vysledek)):
				print(vysledek[k],end="")
		elif volba == 2:
			mala = "abcdefghijklmnopqrstuvwxyz"
			velka = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
			sifra = input("Zadej text k dešifrování: ").upper()
			klic = list(input("Zadej šifrovací klíč: ").upper())
			for i in range(len(klic)):
				klic[i] = velka.find(klic[i])
			klic = klic * 100
			vysledek = []
			for j in range(0,len(sifra)):
				pomocna = velka.find(sifra[j])
				pomocna = pomocna - klic[j]
				while pomocna < 0:
					pomocna += 25
				vysledek.append(velka[pomocna])
			for k in range(0,len(vysledek)):
				print(vysledek[k],end="")