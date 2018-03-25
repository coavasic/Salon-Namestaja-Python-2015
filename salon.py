import korisnici
import namestaj
import usluge
import kategorije
import racuni
import izvestaj
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def main():
	print('*********************************')
	print('*                               *')
	print('* Dobrodosli u salon namestaja! *')
	print('*                               *')
	print('*********************************')
	#Ponavlja funkciju login dok se ne prijavimo sa tacnim korisnickim imenom i sifrom
	log()


def log():
	print('*********************************')
	print('* Molimo vas da se ulogujete    *')
	print('*********************************')
	print('')
	while not login():
		print('\nPogresan username i/ili lozinka')
	#Preuzima vredonst (F/T) iz funkcije morp i proverava da li prijavljeni korisnik prodavac ili menadzer
	morp = korisnici.morp()
	korisnici.informacije_korisnik()
	if morp == True:
		meni_menadzer()
	else:
		meni_prodavac()



def meni_menadzer():
	print('-' * 40)
	print('{:<20}{:>20}'.format('Uloga:','Menadzer'))
	print('-' * 40)
	print('1. Namestaj')
	print('2. Pretraga ')
	print('3. Kategorije')
	print('4. Usluge')
	print('5. Izvestaji')
	print('6. Dodavanje prodavaca')
	print('x - Logout')
	print('-' * 40)
	izbor = input("Unesite izbor >> ")
	if izbor == '1':
		cls()
		namestaj.meni_namestaj()
	elif izbor == '2':
		cls()
		meni_pretraga()
	elif izbor == '3':
		cls()
		kategorije.meni_kategorije()
	elif izbor == '4':
		cls()
		usluge.meni_usluge()
	elif izbor == '5':
		cls()
		izvestaj.meni_izvestaj()
	elif izbor == '6':
		cls()
		korisnici.dodavanje_prodavca()
		meni_menadzer()
	elif izbor == 'x':
		cls()
		log()
	else:
		print('Pogresan izbor! ')
		main()

		
def meni_pretraga():
	print('1. Petraga namestaja ')
	print('2. Pretraga usluga')
	print('3. Pretraga kategorija ')
	print('4. Pretraga racuna')
	print('x - Logout ')
	izbor = input('Uneti izbor >> ')
	if izbor == '1':
		cls()
		namestaj.meni_pretraga()
	elif izbor == '2':
		cls()
		usluge.pretraga_usluga()
	elif izbor == '3':
		cls()
		kategorije.meni_pretraga()
	elif izbor == '4':
		cls()
		racuni.meni_pretraga()
	elif izbor == 'x':
		cls()
		log()
	else:
		print('Pogresan izbor!')
		meni_pretraga()





def meni_prodavac():
	print('-' * 40)
	print('{:<20}{:>20}'.format('Uloga:','Prodavac'))
	print('-' * 40)
	print('1. Pretraga')
	print('2. Izdavanje racuna')
	print('x - Logout')
	print('-' * 40)
	izbor = input('Unesite izbor >> ')
	if izbor == '1':
		cls()
		meni_pretraga()
	elif izbor == '2':
		cls()
		racuni.izdavanje()
	elif izbor == 'x':
		cls()
		log()
	else:
		cls()
		print('Pogresan izbor!')
		meni_prodavac()




def login():
	username1 = input('Unesite korisnicko ime >> ')
	password1 = input('Unesite lozinku >> ')
	return korisnici.login(username1,password1)











if __name__ == '__main__':
	main()