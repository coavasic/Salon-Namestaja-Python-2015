from os.path import exists
import salon
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def login(username, password):
	for korisnik in korisnici:
		if korisnik['korisnicko_ime'] == username and korisnik['lozinka'] == password:
			korisnikmorp = korisnik['uloga']
			global korisnikmorp
			global korisnik
			return True
	return False

def dodavanje_prodavca():
	korisnik = {}
	korisnicko_ime = input('Uneti korisnicko ime >> ')
	k_ime = provera_korisnickog(korisnicko_ime)
	if k_ime == False:
		print('Korisnicko ime vec postoji! ')
		dodavanje_prodavca()
	else:
		korisnik['korisnicko_ime'] = korisnicko_ime
		korisnik['lozinka'] = input('Uneti lozinku >> ')
		korisnik['ime'] = input('Uneti ime >> ')
		korisnik['prezime'] = input('Uneti prezime >> ')
		korisnik['uloga'] = 'p'
		korisnici.append(korisnik)
		cuvanje()


def recnik2korisnici(korisnik):
	return '/'.join([korisnik['korisnicko_ime'], korisnik['lozinka'], korisnik['ime'], korisnik['prezime'], korisnik['uloga']])

def cuvanje():
	f = open('korisnici.txt','w')
	for korisnik in korisnici:
		f.write(recnik2korisnici(korisnik))
		f.write('\n')
	f.close()


def informacije_korisnik():
	cls()
	print('-' * 40)
	print('{:<10}{:>30}'.format('Korisnik', korisnik['ime'] + ' ' + korisnik['prezime']))


def provera_korisnickog(korisnicko_ime):
	for korisnik in korisnici:
		if korisnik['korisnicko_ime'] == korisnicko_ime:
			return False
	return True

	
def morp():
	if korisnikmorp == 'm':
		
		return True
	else:
		
		return False

def ucitavanje_korisnika():
	checkFile()
	for line in open('korisnici.txt','r').readlines():
		if len(line) > 1:
			korisnik = korisnik2recnik(line)
			korisnici.append(korisnik)
			#print(korisnici)

def korisnik2recnik(line):
	if line[-1] == '\n':
		line = line[:-1]
	korisnicko_ime, lozinka, ime, prezime, uloga = line.split('/')
	korisnik = {
	'korisnicko_ime' : korisnicko_ime,
	'lozinka' : lozinka,
	'ime' : ime,
	'prezime' : prezime,
	'uloga' : uloga
	}
	return korisnik





def checkFile():
    if not exists('korisnici.txt'):
        open('korisnici.txt', 'w').close()


korisnici = []

ucitavanje_korisnika()