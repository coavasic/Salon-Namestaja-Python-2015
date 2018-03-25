from os.path import exists
import kategorije
import salon
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Meniji: 


def meni_namestaj():
	print('0. Prikaz namestaja ')
	print('1. Dodavanje namestaja ')
	print('2. Brisanje namestaja ')
	print('3. Izmena namestaja ')
	print('m - Povratak na meni')
	izbor = input('Unesite izbor >> ')

	if izbor == '1':
		cls()
		dodavanje_namestaja()
		meni_namestaj()
	elif izbor == '2':
		cls()
		brisanje_namestaja()
		meni_namestaj()
	elif izbor == '3':
		cls()
		izmena_namestaja()
		meni_namestaj()
	elif izbor == 'm':
		cls()
		salon.meni_menadzer()
	elif izbor == '0':
		cls()
		prikaz_namestaja()
		meni_namestaj()
	else:
		cls()
		print('Pogresan izbor! ')
		meni_namestaj()


def meni_pretraga():
	print('1. Pretraga po nazivu: ')
	print('2. Pretraga po opsegu cena: ')
	print('3. Pretraga po raspolozivoj kolicini')
	print('4. Pretraga po sifri namestaja')
	print('p - Povratak na meni pretrage ')
	izbor = input('Uneti izbor >> ')
	if izbor == '1':
		cls()
		pretraga_naziv()
	elif izbor == '2':
		cls()
		pretraga_cena()
	elif izbor == '3':
		cls()
		pretraga_kolicina()
	elif izbor == '4':
		cls()
		pretraga_sifra()
	elif izbor == 'p':
		cls()
		salon.meni_pretraga()
	else:
		cls()
		print('Pogresam izbor!')
		meni_pretraga_namestaja()




#Operacije nad namestajem****************************************************************************


def ucitavanje_namestaja():
	checkFile()
	for line in open('namestaj.txt').readlines():
		if len(line) > 1:
			nam = namestaj2recnik(line)
			namestaj.append(nam)


def dodavanje_namestaja():
	f = open('namestaj.txt','r').readlines()
	print('1. Dodavanje novog namestaja')
	nam = {}
	nam['rb'] = str(len(f)+1)
	y = 'naziv'
	nam['naziv'] = mora_nesto(y)
	y = 'boju'
	nam['boja'] = mora_nesto(y)
	kolicina = dodavanje(nam, 'kolicina')
	cena = dodavanje(nam,'cena')

	kol = kategorije.namestaj2kategorija()
	nam['kategorija'] = kol
	nam['stanje'] = 'True'
	dodavanje_namestaja1(nam)
	cuvanje()

def mora_nesto(y):
	x = input('Unesite ' + y +' namestaja >> ')
	if x != '' and x !='/':
		return x
	else:
		print('Morate nesto uneti')
		return mora_nesto(y)

def dodavanje(nam, x):
	nam[x] = input('Unesite ' + x + ' namestaja >> ')
	if provera(nam[x]) == False:
		print('Pogresan unos')
		dodavanje(nam, x)
	else:
		return nam[x]

def dodavanje_namestaja1(nam):
	namestaj.append(nam)


def izmena_namestaja():
	prikaz_namestaja()
	rb = input('Uneti sifru namestaja za izmenu>> ')
	for nam in namestaj:
		if rb == nam['rb']:
			kljuc = input('Uneti kljuc za izmenu>> ')
			vrednost = input('Uneti novu vrednost>> ')
			nam[kljuc] = vrednost

	print('Uspesno ste izvrsili izmenu namestaja. ')
	prikaz_namestaja()
	cuvanje()


def brisanje_namestaja():
	prikaz_namestaja()
	rb = input('Uneti sifru namestaja za brisanje >> ')
	for nam in namestaj:
		if nam['rb'] == rb:
			nam['stanje'] = 'False'
	print('Uspesno ste izbrisali komad namestaja!')
	cuvanje()


def namestaj2recnik(line):
	if line[-1] == '\n':
		line = line [:-1]
	rb, naziv, boja, kolicina, cena, kategorija, stanje = line.split('/')
	nam = {
	'rb' : rb,
	'naziv' : naziv,
	'boja' : boja,
	'kolicina' : kolicina,
	'cena' : cena,
	'kategorija' : kategorija,
	'stanje' : stanje
	}
	return nam

def recnik2namestaj(nam):
	return '/'.join([nam['rb'], nam['naziv'], nam['boja'], nam['kolicina'],
		nam['cena'], nam['kategorija'], nam['stanje']])




def azuriranje_kolicine(rb, kolicina):
	for nam in namestaj:
		if nam['rb'] == rb:
			r = int(nam['kolicina'])
			nam['kolicina'] = str(r - kolicina)
			cuvanje()

def cuvanje():
	f = open('namestaj.txt','w')
	for nam in namestaj:
		f.write(recnik2namestaj(nam))
		f.write('\n')
	f.close()

#Pretraga namestaja *******************************************************


def pretraga_naziv():
	naziv = input('Uneti naziv za pretragu: ')
	pronadjeno = []
	for nam in namestaj:
		if naziv == nam['naziv']:
			pronadjeno.append(nam)
			formatiranje_namestaja(pronadjeno)
	meni_pretraga()


def pretraga_cena():
	pronadjeno = []
	print('Uneti opsege cena za pretragu')
	m = input('Uneti minimalnu cenu >> ')
	x = input('Uneti maksimalnu cenu >> ')
	for nam in namestaj:
		r = nam['cena']
		if int(r) < int(x) and int(r) > int(m):
			pronadjeno.append(nam)
			formatiranje_namestaja(pronadjeno)
	meni_pretraga()
			
def pretraga_sifra():
	rb = input('Uneti sifru za pretragu: ')
	pronadjeno = []
	for nam in namestaj:
		if rb == nam['rb']:
			pronadjeno.append(nam)
			formatiranje_namestaja(pronadjeno)
	meni_pretraga()


			
def pretraga_kolicina():
	pronadjeno = []
	kolicina = input('Uneti kolicinu za pretragu: ')
	for nam in namestaj:
		r = nam['kolicina']
		if int(r) < int(kolicina):
			pronadjeno.append(nam)
			formatiranje_namestaja(pronadjeno)
	meni_pretraga()
			

#Formatiranje*************************************************************************
			
def prikaz_namestaja():
	formatiranje_namestaja(namestaj)


def formatiranje_namestaja(namestaj):


    print()
    print("-" * 66 )
    print('{:^60}'.format('NAMESTAJ'))
    print("-" * 66 )
    print('{:<10}{:<20}{:<20}{:<6}{:<10}'.format("SIFRA","NAZIV", "KATEGORIJA", "KOL", "CENA"))
    print("-" * 66 )
    for nam in namestaj:
        if nam['stanje'] == 'True':
        	print('{:<10}{:<20}{:<20}{:<6}{:<10}'.format(nam['rb'], nam['naziv'], nam['kategorija'], nam['kolicina'], nam['cena']))

    print("-" * 66 )
    print()


#Ostalo**************************************************************************************

def checkFile():
    if not exists('korisnici.txt'):
        open('korisnici.txt', 'w').close()



def provera(vrednost):                  
    try:                                            
        int(vrednost)
        return True
    except:
        return False


namestaj = []
ucitavanje_namestaja()

