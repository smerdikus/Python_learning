# Radek zacinajici # timto symbolem (hashtag) je takzvany komentar
# Ten v kodu nic nedela a je jen pro popis jak kod funguje
"""
To same toto, ale to si vysvetlime pozdeji, zatim bereme ze je to take komentar (proste pismo mezi tremi uvozovkami jsou take komentare)
"""


# toto je funkce print() vse co je v zavorkach se vypise na obrazovku, musi se to psat do zavorek, jinak by to byla promenna
# vsimnete si taky ze print se vzdycky vypise na novou radku
print("ahoj")

# toto je promenna, do te si muzeme ulozit co chceme, treba 10, nebo moje jmeno atd, text je potreba psat do "tady" jinak to neni text ale promenne
ahoj = 10
# ahoj je jmeno promenne, 10 je to co je v ni ulozene

# tady vidime problem proc to musime psat do uvozovek, jinak to vypise promennou ahoj, ve ktere je 10
print(ahoj) # komentar muze byt i tady, ale od # je komentar az do konce radku

a = 5
ahoj = a
print(ahoj) # takhle vymenime to co je v ahoj za to co je v a

ahoj = ahoj
print(ahoj) # proc se ahoj nezmenilo? (protoze v ahoj je ulozeno 5 a do ahoj davame to co je ulozene v ahoj, takze 5)

ahoj = "ahoj"
print(ahoj) # pokud chceme do ahoj ulozit ahoj, musime to dat do uvozovek jako text

ahoj = 10 # vratime tam 10

# matematicke zaklady
print(ahoj * 5)
print(ahoj + ahoj) # normalni scitani, 10 + 10 = 20, vypiseme 20

# funkce str(ahoj) udela z toho co je v ahoj text takze "10"
print(str(ahoj) + str(ahoj)) # spojovani veci v uvozovek je prida za sebe takze "10" + "10" = "1010"
print(ahoj, ahoj) # funguje to stejne napriklad s pouzitim carky

# vypis dnesniho datumu
den = 15
mesic = 4
rok = 2025 # muzete ho upravit a prepsat na dnesni datum a zkusit

# dokazes prijit na to proc tohle nefunguje?
print(den + mesic + rok)

# reseni jak by to melo fungovat, ale nevypada to hezky, chtelo by to nejake tecky mezi
print(str(den) + str(mesic) + str(rok))

# co napriklad takto?
print(str(den) + "." + str(mesic) + "." + str(rok)) # muzeme mezi kazde cislo datumu vlozit tecku ale musi byt v uvozovkach

# pokud nechceme aby se print vypsal pokazde na novou radku muzeme napriklad pouzit tohle
print(den, end=".") # , end="" znamena ze za nas den se neudela nova radka ale vypise se "." takze .
print(mesic, end=".")
print(rok, end="\n") # toto je pro zajimavost, "\n" znamena nova radka muzeme videt v dalsi ukazce
print("ahoj\nna\nnove\nradce") # kazde \n se vymenilo za novou radku

# jak bysme vypsali nejake lehke matematicke veci?

# Vypocet obvodu ctverce o strane 5
strana = 5
print("Obvod čtverce o straně", strana, "je", strana * 4)

# Vypocet obsahu obdelniku se stranami 4 a 7
a = 4
b = 7
print("Obsah obdélníku se stranami", a, "a", b, "je", a * b)
print("Obvod toho sameho obdelniku je", 2 * a + 2 * b)

# Vypocet kolik minut je v 5 hodinach
hodiny = 5
print(hodiny, "hodin je", hodiny * 60, "minut")
hodiny = hodiny - 4 # do promenne hodiny si ulozime hodiny (to je 5) - 4, takze celkem 1 hodina (5-4=1)
print(hodiny, "hodin je", hodiny * 60, "minut")
# muzeme si vsimnout ze jsme jenom zmenili obsah nasi promenne ale pouzili tu samou radku na vypis kolik minut je v jedne hodine


# Kolik sekund je v 3 dnech?
dny = 3
print(dny, "dny mají", dny * 24 * 60 * 60, "sekund") # den ma 24 hodin, hodina ma 60 minut a ta ma 60 sekund


# Scitani roku - kolik ti bude za 10 let?
vek = 15
print("Za 10 let ti bude", vek + 10)

# Ukazka zbytku po deleni
# zbytek z 10 děleno 3 je 1, kdyz udelame 9 / 3 tak vysledek je 3, kdyz ale udelame 10 / 3 tak je to vysledek 3 ale zbytek 1, pro to mame speciali znak %
print("Zbytek po dělení 10 / 3 je", 10 % 3)


# Sestaveni vety z cisel a textu
cislo = 7
print("Šťastné číslo je " + str(cislo))


# Kolik dni trva 5 tydnu?
tydny = 5
print(tydny, "týdnů má", tydny * 7, "dní")


# Co jsme se naucili?
# Vypisovat na obrazovku neco z naseho programu, velmi dulezite v programech, co by to bylo za program kdyby neco delal ale my jsme to nevideli? :(
# Dale take ulozeni do promenne a vypsani promenne, kdybysme si nemohli ukladat zkuste si sami ukol v souboru uloha.py, koukejte se sem, na internet, nepouzivejte chatgpt, to se naucime pouzivat, ale pozdeji
