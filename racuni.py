import namestaj
import korisnici
from os.path import exists
from datetime import date
import salon
import usluge
import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def meni_pretraga():
	print('1. Pretraga po prodavcu koji je izdao ')
	print('2. Pretraga po nazivu namestaja')
	print('3. Pretraga po nazivu usluge ')
	print('4. Pretraga po broju racuna ')
	print('5. Pretraga po datumu ')
	print('m - povratak na glavni meni pretrage ')
	izbor = input('Uneti izbor >> ')
	if izbor == '1':
		cls()
		pretraga_prodavac()
		meni_pretraga()
	elif izbor == '4':
		cls()
		pretraga_sifra()
		meni_pretraga()
	elif izbor == '5':
		cls()
		pretraga_datum()
		meni_pretraga()
	elif izbor == '2':
		cls()
		pretraga_namestaj()
		meni_pretraga()
	elif izbor == '3':
		cls()
		pretraga_usluga()
		meni_pretraga()
	elif izbor == 'm':
		cls()
		salon.meni_pretraga()
	else:
		print('Pogresan izbor!')
		meni_pretraga()


def pretraga_prodavac():
	ime = input('Uneti ime prodavca za pretragu >> ')
	for racun in racuni:
		if racun['ime'] == ime:
			priprema_za_formatiranje(racun)


def pretraga_sifra():
	sifra = input('Uneti sifru racuna >> ')
	for racun in racuni:
		if racun['rb'] == sifra:
			priprema_za_formatiranje(racun)

def pretraga_datum():
	datum = input('Uneti datum u obliku dd-mm-gggg >> ')
	for racun in racuni:
		if racun['datum'] == datum:
			priprema_za_formatiranje(racun)

def pretraga_namestaj():
	naziv = input('Uneti naziv namestaja za pretragu >> ')
	for racun in racuni:
		namestaj1 = racun['namestaj'].split('^')
		for namestaj in namestaj1:
			lista_namestaja = []
			lista_namestaja.append(namestaji_u_recnike(namestaj))
			for nam in lista_namestaja:
				if nam['naziv'] == naziv:
					priprema_za_formatiranje(racun)

def pretraga_usluga():
	naziv = input('Uneti naziv usluge za pretragu >> ')
	for racun in racuni:
		usluga1 = racun['usluge'].split('^')
		for usluga in usluga1:
			lista_usluga = []
			lista_usluga.append(usluga_u_recnike(usluga))
			for usl in lista_usluga:
				if usl['naziv'] == naziv:
					priprema_za_formatiranje(racun)

def usluga_u_recnike(line):
	naziv, jcena = line.split('*')
	usluga2 = {
	'naziv':naziv,
	'jcena':jcena
	}
	return usluga2


def namestaji_u_recnike(line):
	naziv, jcena, kolicina, kategorija = line.split('*')
	namestaj2 = {
	'naziv':naziv,
	'jcena':jcena,
	'kolicina':kolicina,
	'kategorija' :kategorija
	}
	return namestaj2

def priprema_za_formatiranje(racun):
	lista_namestaja = []
	lista_usluga = []
	namestaj1 = racun['namestaj'].split('^')
	usluga1 = racun['usluge'].split('^')
	for namestaj in namestaj1:
		lista_namestaja.append(namestaji_u_recnike(namestaj))
	for usluga in usluga1:
		lista_usluga.append(usluga_u_recnike(usluga))
	formatiranje_racuna(racun, lista_namestaja, lista_usluga)



def checkFile():
    if not exists('racuni.txt'):
        open('racuni.txt', 'w').close()

def izdavanje():
	lista_namestaja = []
	lista_usluga = []
	f = open('racuni.txt', 'r').readlines()
	racun = {}
	izdavanje_namestaja(lista_namestaja)
	hoces_uslugu = input('Zelite li ulsugu? (y/n) ')
	if hoces_uslugu == 'y':
		izdavanje_usluga(lista_usluga)
	else:
		usluga1 = {}
		usluga1['naziv'] = 'X'
		usluga1['jcena'] = '0'
		lista_usluga.append(usluga1)
	namestaj2 = []
	usluga2 = []
	for nam in lista_namestaja:
		namestaj2.append(join_nam(nam))
	for usl in lista_usluga:
		usluga2.append(join_usl(usl))
	namestaj3 = '^'.join(namestaj2)
	usluga3 = '^'.join(usluga2)
	racun['rb'] = str(len(f)+1)
	racun['ime'] = korisnici.korisnik['ime']
	racun['prezime'] = korisnici.korisnik['prezime']
	racun['namestaj'] = namestaj3
	racun['usluge'] = usluga3
	racun['datum'] = time.strftime("%Y-%m-%d")
	racun['vreme'] = time.strftime("%I:%M:%S")
	cena1 = cena(lista_namestaja, lista_usluga)
	pdv1 =	pdv(cena1)
	racun['pdv'] = str(pdv1)
	racun['cena'] = str(int(cena1) + pdv1)
	
	racuni.append(racun)
	cuvanje()
	cls()
	formatiranje_racuna(racun, lista_namestaja, lista_usluga)
	novi_rac = input('Zelite li izadavanje novog racuna? (y/n) ')
	cls()
	if novi_rac == 'y':
		izdavanje()
	else:
		salon.meni_prodavac()

#	print(racun)
#	print(namestaj3)
	#print(namestaj2)
	#print(usluga2)

def pdv(cena1):
	pdv = int(cena1) * 20/100
	return int(pdv)

def cena(lista_namestaja, lista_usluga):
	ukupno = 0
	for nam in lista_namestaja:
		r = int(nam['jcena'])
		k = int(nam['kolicina'])
		ukupno = ukupno + (r * k)
	for usl in lista_usluga:
		r = int(usl['jcena'])
		ukupno = ukupno + r
	ukupno = str(ukupno)
	return ukupno


def izdavanje_namestaja(lista_namestaja):
	namestaj1 = {}
	namestaj.prikaz_namestaja()
	sifra = provera_sifra1(namestaj.namestaj)
	kolicina = provera_kolicina(sifra)
	for nam in namestaj.namestaj:
		if nam['stanje'] == 'True' and nam['rb'] == sifra:
			namestaj1['naziv'] = nam['naziv']
			namestaj1['jcena'] = nam['cena']
			namestaj1['kolicina'] = str(kolicina)
			namestaj1['kategorija'] = nam['kategorija']
	lista_namestaja.append(namestaj1)
	namestaj.azuriranje_kolicine(sifra, int(kolicina))
	opet = input('Zelite li jos namestaja? (y/n) ')
	if opet == 'y':
		izdavanje_namestaja(lista_namestaja)
			#print(lista_namestaja)

def provera_kolicina(sifra):
	kolicina = input('Unesite kolicinu >> ')
	if provera_kolicina1(kolicina, sifra) == False:
		print('Nema dovoljno namestaja ili kolicina nije dobro uneta!')
		return provera_kolicina(sifra)
	else:
		return str(kolicina)

def provera_kolicina1(kolicina, sifra):
	for nam in namestaj.namestaj:
		r = int(nam['kolicina'])
		x = int(kolicina)
		if nam['rb'] == sifra:
			if r >= x:
				return True
	return False

def provera_sifra(sifra1, lista):
	for nam in lista:
		if nam['stanje'] == 'True' and nam['rb'] == sifra1:
			return True
	return False


def provera_sifra1(lista):
	sifra1 = input('Unesite sifru >> ')
	if provera_sifra(sifra1, lista) == False:
		print('Pogresna sifra namestaja ')
		return provera_sifra1(lista)
	else:
		return sifra1



def izdavanje_usluga(lista_usluga):
	cls()
	usluga1 = {}
	usluge.prikaz_usluga()
	sifra = provera_sifra1(usluge.usluge)
	for usl in usluge.usluge:
		if usl['stanje'] == 'True' and usl['rb'] == sifra:
			usluga1['naziv'] = usl['naziv']
			usluga1['jcena'] = usl['cena']
	lista_usluga.append(usluga1)
	opet = input('Zelite li jos usluga? (y/n) ')
	if opet == 'y':
		izdavanje_usluga(lista_usluga)
	#print(lista_usluga)

def join_nam(nam):
		return '*'.join([nam['naziv'], nam['jcena'], nam['kolicina'], nam['kategorija']])

def join_usl(usl):
		return '*'.join([usl['naziv'], usl['jcena']])


def cuvanje():
	f = open('racuni.txt','w')
	for racun in racuni:
		f.write(recnik2racuni(racun))
		f.write('\n')
	f.close()

def recnik2racuni(racun):
	return '/'.join([racun['rb'], racun['ime'], racun['prezime'], racun['namestaj'], racun['usluge'], racun['datum'], racun['vreme'],racun['pdv'], racun['cena']])

def ucitavanje_racuna():
	checkFile()
	for line in open('racuni.txt').readlines():
		if len(line) > 1:
			racun = racuni2recnik(line)
			racuni.append(racun)

def racuni2recnik(line):
	if line[-1] == '\n':
		line = line [:-1]
	rb, ime, prezime, namestaj, usluge, datum, vreme,pdv, cena = line.split('/')
	racun = {
	'rb' : rb,
	'ime' : ime,
	'prezime': prezime,
	'namestaj': namestaj,
	'usluge' : usluge,
	'datum' : datum,
	'vreme' : vreme,
	'pdv' :pdv,
	'cena' : cena
	}
	return racun


def formatiranje_racuna(racun, lista_namestaja, lista_usluga):
	print('************ Racun ***************')
	print('{:<17}{:>17}'.format(racun['datum'],racun['vreme']))
	print('{:<10}{:>24}'.format('Prodavac:', racun['ime'] + ' ' + racun['prezime']))
	print('{:<15}{:>19}'.format('Broj racuna:', racun['rb']))
	print('----------------------------------')
	print('{:<21}{:<4}{:>9}'.format('Naziv','kol','cena'))
	print('----------------------------------')
	for nam in lista_namestaja:
		print('{:<21}{:<4}{:>9}'.format(nam['naziv'],nam['kolicina'],nam['jcena']))
	print('----------------------------------')
	for usl in lista_usluga:
		print('{:<25}{:>9}'.format(usl['naziv'],usl['jcena']))
	print('----------------------------------')
	print('{:<17}{:>17}'.format('Cena bez pdv-a:',int(racun['cena'])-int(racun['pdv'])))
	print('{:<4}{:>30}'.format('PDV:',racun['pdv']))
	print('{:<8}{:>26}'.format('Ukupno:', racun['cena']))
	print('**********************************')
	print('\n')
	print('\n')




racuni = []


ucitavanje_racuna()