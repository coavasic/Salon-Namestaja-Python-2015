from os.path import exists
import salon
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
#Meniji*********************************************************************************************

def meni_kategorije():
	print('1. Dodavanje kategorije')
	print('2. Brisanje kategorije')
	print('3. Izmena kategorije')
	print('m - Povratak na meni')
	izbor = input('Unesite izbor >> ')
	if izbor == '1':
		cls()
		dodavanje_kategorija()
		meni_kategorije()
	elif izbor == '2':
		cls()
		brisanje_kategorije()
		meni_kategorije()
	elif izbor == '3':
		cls()
		izmena_kategorije()
		meni_kategorije()
	elif izbor == 'm':
		cls()
		salon.meni_menadzer()

	else:
		print('Pogresan izbor!')
		meni_kategorije()


#Operacije nad kategorijama*************************************************************************



def ucitavanje_kategorije():
	checkFile()
	for line in open('kategorije.txt').readlines():
		if len(line) > 1:
			kat = kategorije2recnik(line)
			kategorije.append(kat)

def dodavanje_kategorija():
	f = open('kategorije.txt', 'r').readlines()

	print('3. Dodavanje nove kategorije')
	kat = {}
	kat['rb'] = str(len(f)+1)
	y = 'naziv'
	kat['naziv'] = mora_nesto(y)
	y = 'opis'
	kat['opis'] = mora_nesto(y)
	kat['stanje'] = 'True'

	dodavanje_kategorija1(kat)
	cuvanje()

def mora_nesto(y):
	x = input('Unesite ' + y +' kategorije >> ')
	if x != '' and x != '/':
		return x
	else:
		print('Morate nesto uneti')
		return mora_nesto(y)


def brisanje_kategorije():
	prikaz_kategorija()
	sifra = input('Uneti redni broj kategorije za brisanje >> ')
	for kat in kategorije:
		if kat['rb'] == sifra:
			kat['stanje'] = 'False'
	cuvanje()


def izmena_kategorije():
	prikaz_kategorija()
	sifra = input('Uneti redni broj kategorije za izmenu>> ')
	for kat in kategorije:
		if sifra == kat['rb']:
			kljuc = input('Uneti kljuc za izmenu>> ')
			vrednost = input('Uneti novu vrednost>> ')
			kat[kljuc] = vrednost
	cuvanje()

def kategorije2recnik(line):
	if line[-1] == '\n':
		line = line [:-1]
	rb, naziv, opis, stanje = line.split('/')
	kat = {
	'rb' : rb,
	'naziv' : naziv,
	'opis' : opis,
	'stanje' : stanje
	}
	return kat

def recnik2kategorije(kat):
	return '/'.join([kat['rb'], kat['naziv'], kat['opis'],kat['stanje']])

def namestaj2kategorija():
	prikaz_kategorija()
	rb = str(input('Uneti redni broj kategorije iz liste kojoj namestaj pripada>> '))
	for kat in kategorije:
		if kat['rb'] == rb and kat['stanje'] == 'True':
			return kat['naziv']
	print('Ne postoji trazena kategorija!')
	print('1. Unesite opet redni broj kategorije')
	print('2. Dodajte novu kategoriju')
	izbor = input('Unesite izbor >>')
	if izbor == '1':
		return namestaj2kategorija()
	elif izbor == '2':
		kategorije.dodavanje_kategorija()
		return namestaj2kategorija



def dodavanje_kategorija1(kat):
	kategorije.append(kat)

def cuvanje():
	f = open('kategorije.txt','w')
	for kat in kategorije:
		f.write(recnik2kategorije(kat))
		f.write('\n')
	f.close()

#Formatiranje kategorija******************************************************************************

def formatiranje_kategorija(kategorije):
	print()
	print("-" * 45 )
	print('{:^45}'.format('Kategorije'))
	print("-" * 45 )
	print('{:<5}{:<20}{:<30}'.format("RB." , "NAZIV", "OPIS"))
	print("-" * 45 )
	for kat in kategorije:
		if kat['stanje'] == 'True':
			print("{:<5}{:<20}{:<30}".format(kat['rb'], kat['naziv'], kat['opis']))
	print("-" * 45 )




def prikaz_kategorija():
	formatiranje_kategorija(kategorije)

#Ostalo****************************************************************


def checkFile():
    if not exists('kategorije.txt'):
        open('kategorije.txt', 'w').close()



kategorije = []
ucitavanje_kategorije()