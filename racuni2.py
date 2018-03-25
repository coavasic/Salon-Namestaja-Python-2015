# =================================================================== RACUN ============================================================================================================================
def racun_namestaj(nova_lista,imen,prezimen):
	lista_namestaja = entiteti.ucitavanje_namestaja()
	sifra = input("Unesite sifru zeljenog namestaja: ")
	proveri = entiteti.provera_izmene_namestaja(sifra,lista_namestaja)
	if proveri[0] == True:
		if proveri[1]['obrisan'] == "True":
			print("Komad namestaja ne postoji")
			racun_namestaj(nova_lista,imen,prezimen)
	if proveri[1]['kolicina'] <= "0":
		print("Taj namestaj vise nema na stanju")
		racun_namestaj(nova_lista,imen,prezimen)
	if proveri[0] == True:
		print("\nSIFRA: "+proveri[1]['sifra'],"NAZIV: "+proveri[1]['naziv'],"BOJA: "+proveri[1]['boja'],"KOLICINA: "+proveri[1]['kolicina'],"CENA: "+proveri[1]['cena'],"KATEGORIJA: "+proveri[1]['kategorija'],"\n\n")
		unos_kolicine = int(input("Unesite zeljenu kolicinu koju zelite da prodate: "))
		while unos_kolicine > int(proveri[1]['kolicina']):
			print("Nema toliko proizvoda na stanju!\n")
			unos_kolicine = int(input("Unesite zeljenu kolicinu koju zelite da prodate: "))
		while unos_kolicine <= 0:
			print("Unos ne moze da bude 0!\n")
			unos_kolicine = int(input("Unesite zeljenu kolicinu koju zelite da prodate: "))
		
		nova_kolicina = int(proveri[1]['kolicina']) - unos_kolicine
		proveri[1]['kolicina'] = nova_kolicina
		entiteti.cuvanje_namestaja(lista_namestaja)
		
		cena = unos_kolicine * int(proveri[1]['cena'])

		dodavanje_namestaja = []
		nam = {
		
		'naziv': proveri[1]['naziv'],
		'cena': cena,
		'kolicina': unos_kolicine,

		}
		dodavanje_namestaja.append(nam)
		nova_lista.append(dodavanje_namestaja)
		x = input("Ako zelite da dodate jos koji proizvod prtisnite Y ako ne zelite pritisnite N [Y:N]: ")
	
		while x!= "Y" and x!="y" and x!="N" and x!="n":
			print("Greska morate da pritinite Y ili N")
			x = input("Ako zelite da dodate jos koji proizvod prtisnite Y ako ne zelite pritisnite N [Y:N]: ")
		if x == "N" or x == "n":
			lista = [] 
			racun_usluge(lista,nova_lista,imen,prezimen)
		else:
			racun_namestaj(nova_lista,imen,prezimen)
				
def racun_usluge(lista,lista_namestaja,imen,prezimen):

	lista_usluga = entiteti.ucitavanje_usluga()
	naziv_usluge = input("Unesite naziv usluge koju zelite da dodate: ")
	proveri = entiteti.provera_izmene_usluga(naziv_usluge,lista_usluga)
	if proveri[0] == True:
		if proveri[1]['obrisan'] == "True":
			print("Usluga ne postoji")
			racun_usluge(lista,lista_namestaja,imen,prezimen,cena)
	if proveri[0] == True:
		print("\nNAZIV: "+proveri[1]['naziv'],"OPIS: "+proveri[1]['opis'],"CENA: "+proveri[1]['cena'],"\n\n")
		
		lista_usluga = []
		usluge = {
		
		'naziv': proveri[1]['naziv'],
		'opis': proveri[1]['opis'],
		'cena': proveri[1]['cena'],
		

		}
		lista_usluga.append(usluge)	
		lista.append(lista_usluga)
		x = input("Ako zelite da dodate jos koju uslugu prtisnite Y ako ne zelite pritisnite N [Y:N]: ")
	
		while x!= "Y" and x!="y" and x!="N" and x!="n":
			print("Greska morate da pritinite Y ili N")
			x = input("Ako zelite da dodate jos koju uslugu prtisnite Y ako ne zelite pritisnite N [Y:N]: ")
		if x == "N" or x == "n":
			print(lista)
			racun(lista,lista_namestaja,imen,prezimen)
		else:
			racun_usluge(lista,lista_namestaja,imen,prezimen)

def racun(lista_usluga,lista_namestaja,imen,prezimen):
	lista_racuna = ucitavanje_racuna()
	for i in lista_racuna:
		z = int(i['br_racuna']) + 1
	br_racuna = z
	porez = "20"
	cena = 0
	for i in lista_namestaja:
		cena += int(i[0]['cena'])


	for l in lista_usluga:
		cena += int(l[0]['cena'])

	ukupna_cena = cena * 1.2
	ime = imen
	prezime = prezimen
	datum = time.strftime("%d/%m/%Y")
	vreme = time.strftime("%I:%M:%S")
	obrisan = "False"
	dodavanje_racuna = []
	racun = {
		"lista_namestaja": lista_namestaja,
		"lista_usluga": lista_usluga,
		"porez": porez,
		"ukupna_cena": ukupna_cena,
		"datum": datum,
		"vreme": vreme,
		"ime": ime,
		"prezime": prezime,
		"br_racuna": br_racuna,
		"obrisan": obrisan,
	}
	lista_racuna.append(racun)
	cuvanje_racuna(lista_racuna)
	prikazivanje_racuna(racun)