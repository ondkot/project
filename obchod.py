jidlaClovek = ["hranolky","zmrzlina","bonbóny","nanuk","sušenky"]
jidlaUfo = ["žáby","lidské oči"]
print("Menu:")
for i in jidlaClovek:
	print(i)
for j in jidlaUfo:
	print(j)
jidlo = input("Na co máš chuť?: ").lower()
while (jidlo not in jidlaClovek) and (jidlo not in jidlaUfo):
	print("Zadej jídlo znovu.")
	jidlo = input("Na co máš chuť?: ").lower()

if jidlo in jidlaClovek:
	print("To máme!")
else:
	coJe = input("Jsi člověk nebo UFO?: ").lower()
	while (coJe != "člověk") and (coJe != "ufo"):
		print("Nerozumím.")
		coJe = input("Jsi člověk nebo UFO?: ").lower()
	if coJe == "ufo":
		print("Pro ufa jídlo nemáme.")
	else:
		print("A proč sis nekoupil lidské jídlo????")
