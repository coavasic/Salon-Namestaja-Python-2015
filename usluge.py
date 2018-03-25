from os.path import exists
import salon
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Meniji *************************************************************************************
def meni_usluge():
	print('1. Dodavanje usluga')
	print('2. Brisanje usluga')
	print('3. Izmena usluga')
	izbor = input('Unesite izbor >> ')
	if izbor == '1':
		cls()
		dodavanje_usluga()
		meni_usluge()
	elif izbor == '2':
		cls()
		brisanje_usluge()
		meni_usluge()
	elif izbor == '3':
		cls()
		izmena_usluge()
		meni_usluge()
	else:
		print('Pogresan unos!')
		meni_usluge()



def meni_pretraga():
	print('1. Pretraga po nazivu')
	print('2. Pretraga po opsegu cena')
	print('m - Povratak na meni pretrage')
	izbor =	input('Uneti izbor >> ')
	if izbor == '1':
		cls()
		pretraga_naziv()
	elif izbor == '2':
		cls()
		pretraga_cena()
	elif izbor == 'm':
		cls()
		salon.meni_pretraga()
	else:
		cls()
		print('Pogresan izbor! ')
		meni_pretraga()


def pretraga_naziv():
	pronadjeno = []
	naziv = input('Uneti naziv za pretragu: ')
	for usl in usluge:
		if naziv == usl['naziv']:
			pronadjeno.append(usl)
			formatiranje_usluga(pronadjeno)
			meni_usluge()

def pretraga_cena():
	pass

#Operacije nad uslugama***************************************************


def ucitavanje_usluga():
	checkFile()
	for line in open('usluge.txt', 'r').readlines():
		if len(line) > 1:
			usl = usluge2recnik(line)
			usluge.append(usl)


def dodavanje_usluga():
	f = open('usluge.txt', 'r').readlines()

	print('1. Dodavanje usluge ')
	usl = {}
	usl['rb'] = str(len(f)+1)
	y = 'naziv'
	usl['naziv'] = mora_nesto(y)
	y = 'opis'
	usl['opis'] = mora_nesto(y)
	cena = dodavanje(usl)
	usl['stanje'] = 'True'

	dodavanje_usluga1(usl)
	cuvanje()
	meni_usluge()

def mora_nesto(y):
	x = input('Unesite ' + y +' usluge >> ')
	if x != '' and x != '/':
		return x
	else:
		print('Morate nesto uneti')
		return mora_nesto(y)


def dodavanje(usl):
	usl['cena'] = input('Unesite cenu usluge')
	if provera(usl['cena']) == False:
		print('Pogresan unos')
		dodavanje(usl)
	else:
		return usl['cena']

def dodavanje_usluga1(usl):
	usluge.append(usl)

def izmena_usluge():
	prikaz_usluga()
	sifra = input('Uneti redni broj usluge za izmenu>> ')
	for usl in usluge:
		if sifra == usl['rb']:
			kljuc = input('Uneti kljuc za izmenu>> ')
			vrednost = input('Uneti novu vrednost>> ')
			usl[kljuc] = vrednost
	cuvanje()
	meni_usluge()


def brisanje_usluge():
	prikaz_usluga()
	sifra = input('Uneti redni broj usluge za brisanje >> ')
	for usl in usluge:
		if usl['rb'] == sifra:
			usl['stanje'] = 'False'
	cuvanje()
	meni_usluge()



def usluge2recnik(line):
	if line[-1] == '\n':
		line = line[:-1]
	rb, naziv, opis, cena, stanje = line.split('/')
	usl= {
	'rb' : rb,
	'naziv':naziv,
	'opis':opis,
	'cena':cena,
	'stanje': stanje

	}
	return usl

def recnik2usluge(usl):
	return '/'.join([usl['rb'], usl['naziv'], usl['opis'], usl['cena'], usl['stanje']])

def cuvanje():
	f = open('usluge.txt','w')
	for usl in usluge:
		f.write(recnik2usluge(usl))
		f.write('\n')
	f.close()


#Formatiranje *********************************************************************



def formatiranje_usluga(usluge):
	print()
	print("-" * 63 )
	print('{:^63}'.format('Usluge'))
	print("-" * 63 )
	print('{:<5}{:<20}{:<30}{:<8}'.format("RB." , "NAZIV", "OPIS", "CENA"))
	print("-" * 63 )
	for usl in usluge:
		if usl['stanje'] == 'True':
			print("{:<5}{:<20}{:<30}{:<8}".format(usl['rb'], usl['naziv'], usl['opis'], usl['cena']))
	print("-" * 63 )

def prikaz_usluga():
	formatiranje_usluga(usluge)



#Ostalo ****************************************************************************

def provera(vrednost):                  
    try:                 
        int(vrednost)
        return True
    except:
        return False


def checkFile():
    if not exists('usluge.txt'):
        open('usluge.txt', 'w').close()



usluge = []
ucitavanje_usluga()