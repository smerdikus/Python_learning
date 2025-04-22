"""
Toto je navod pro druhy domaci ukol, bude se probirat podminka if, else a elif
a vstup z klavesnice pomoci input (take funkci int(""), ktera prevede string na cislo napr "10" prevede na 10
"""


# pokud se chceme v programu rozhodnout jestli udelat neco nebo neudelat, pomaha nam k tomu tzv if (kdyz)
if 5 < 10:
	print("5 je min nez 10")
	
# pokud se tak nestane a chceme udelat neco jineho pouzije se jeste else
if 5 > 10:
	print("5 je vic nez 10")
else:
	print("5 je min nez 10")
	
# vsimnete si, ze pred nasemi print(...) jsou vzdy jakesi mezery
# to je takzvany blok kodu
if 5 < 10:
	print("vypise se toto")
	print("a toto")
	print("a vsechno co ma pred sebou tyto mezery")
	
a = 5
b = 10

# dalsi detail, pozor na dvojtecku za nasi podminkou
if a < b:
	print("da se to pouzivat i s promenymi")
	print("bez promennych by to nemelo smysl pouzivat")
	
# v programovani je rozdil mezi = a ==
# dvakrat = (psano takto ==) testuje jestli jsou dve cisla (nebo objekty, vysvetlime pozdeji) stejna
# jedno = nam do nejake promenne ulozi cislo
# ukazeme si
c = 10 # jedno rovna se uklada
if c == b: # potrebujeme 2 rovna se pro otestovani rovnosti
	print(f"{c} je stejne jako {b}")
	
# if se sklada z: if podminka:
# da se vlozit i vice podminek
c = 20
if a < b and b < c:
	# nyni si vsimnete, ze nemusime furt psat str(a) + " < " + str(b) + " < " + str(c)
	print(f"{a} < {b} < {c}")
	# to zpusobi takzvany formatovany string (string je vse mezi "") a ten se vyvtori vlozenim f"" pred string
	print(f"jejich soucet je {a + b + c}") # muzeme zde tvorit i matematicke prikazy nejake
	

vstup = input("zadej neco: ") # input je prikaz kdy muzeme zadavat klavesnici vstup, napiste neco tam kde se vypisuje nas vysledek
if vstup == "ahoj":
	print("jak se mate?")
else:
	print(f"zadali jste: {vstup}")
	
	
	
# funkce int() udela ze stringu cislo ("5" udela jen 5) potrebujeme to proto, ze na "5" nejde napriklad ani + - modulo atd
cislo = int(input("Zadej číslo: "))

if cislo % 2 == 0: # pokud je zbytek po deleni 1, je cislo liche pokud je nula je sude
	# 4 / 2 = 2 zbytek 0
	# tato operace % se nazyva modulo
	print("Číslo je sudé")
else:
	# 5 / 2 = 2 zbytek 1
	print("Číslo je liché")
	
a = int(input("Zadej první číslo: "))
b = int(input("Zadej druhé číslo: "))

operace = input("Jakou operaci chceš provést? (+, -, *, /): ")

if operace == "+":
	print(f"Výsledek: {a + b}")
elif operace == "-": # elif znamena pokud neni splnena prvni podminka u if, ale je splnena tato u elif
	print(f"Výsledek: {a - b}") # pak se stane toto
elif operace == "*": # pokud nejsou splneny predchozi dve podminky a je splnena tato
	print(f"Výsledek: {a * b}") # stane se toto
elif operace == "/":
	if b != 0: # jelikoz nemuzeme delit nulou
		print(f"Výsledek: {a / b}")
	else:
		print("Nelze dělit nulou!")
else:
	print("Neznámá operace.") # pokud neni splnena ani jedna z predchozich podminek stane se toto
	
	
	

