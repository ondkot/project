class kostka:
	from random import randrange
	def hod(self):
		self.cislo = self.randrange(0,6)
		self.seznam = [
		[[" "," "," "],
		 [" ","*"," "],
		 [" "," "," "]
		 ],
		[[" "," "," "],
		 [" ","*"," "],
		 [" "," "," *"]
		 ],
		[["*"," "," "],
		 [" "," *"," "],
		 [" "," ","  *"]],
		[[" "," "," "],
		 [" ","* ","*"],
		 [" ","* ","*"]],
		[["*  "," ","*"],
		 [" "," *"," "],
		 ["*  "," ","*"]],
		[["* ","*"," "],
		 ["* ","*"," "],
		 ["* ","*"," "]]
		]
		self.proVypis = self.seznam[self.cislo]
	def vypis(self):
		self.hod()
		for i in range(0,len(self.proVypis)):
			for j in range(0,len(self.proVypis[i])):
				print(self.proVypis[i][j],end="")
			print("\n")
kostka = kostka()
kostka.vypis()
