import racuni
import salon
import kategorije
from datetime import timedelta, date
import os
import time

def cls():
    os.system('cls' if os.name=='nt' else 'clear')


def meni_izvestaj():
	print('1. Izvestavanje po datumu ')
	print('2. Izvestavanje po kategoriji ')
	print('m - meni menadzera ')
	izbor = input('Uneti izbor >> ')
	if izbor == '1':
		cls()
		izvestaj_datum()
		meni_izvestaj()
	elif izbor == '2':
		cls()
		izvestaj_kategorija()
		meni_izvestaj()
	elif izbor == 'm':
		cls()
		salon.meni_menadzer()
	else:
		cls()
		print('Pogresan izbor')
		meni_izvestaj()

def izvestaj_datum():
	datum3 = input("Unesite datum u gggg-mm-dd formatu >> ")
	datum4 = input('Unesite datum u gggg-mm-dd formatu >> ')
	datum1 = datum3.split('-')
	datum2 = datum4.split('-')
	cls()
	d1 = datum1[2]
	m1 = datum1[1]
	g1 = datum1[0]
	d2 = datum2[2]
	m2 = datum2[1]
	g2 = datum2[0]
	if is_date_valid(g1,m1,d1) == False:
		print('Pogresan datum')
		izvestaj_datum()
	if is_date_valid(g2,m2,d2) == False:
		print('Pogresan datum')	
		izvestaj_datum()

	start_date = date(int(g1), int(m1), int(d1))
	end_date = date(int(g2), int(m2), int(d2))
	ukupno_period = 0
	datumi = []
	cls()
	print('----------------------------------------')
	print('{:<20}{:<20}'.format('Datum od', datum3))
	print('{:<20}{:<20}'.format('Datum do', datum4))
	print('----------------------------------------')
	print('{:<20}{:<20}'.format('Datum','Ukupno za datum'))
	print('----------------------------------------')
	for single_date in daterange(start_date, end_date):
	    x = single_date.strftime("%Y-%m-%d")
	    for racun in racuni.racuni:
	    	if racun['datum'] == x:
	    		datum = racun['datum']
	    		if datum not in datumi:
	    			datumi.append(datum)
	    			ukupno_dan = izvestaj_dan(datum)
	    			ukupno_period += ukupno_dan
	    			print('{:<20}{:<20}'.format(datum,ukupno_dan))
	print('----------------------------------------')
	print()
	print('{:<20}{:<20}'.format('Ukupno za period:',ukupno_period))

def is_date_valid(year, month, day):
    try:
    	this_date = date(int(year), int(month), int(day))
    except ValueError:
        return False
    else:
        return True

def izvestaj_dan(datum):
	ukupno_dan = 0
	for racun in racuni.racuni:
		if racun['datum'] == datum:
			r = int(racun['cena'])
			ukupno_dan += r
	return ukupno_dan




def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)



def izvestaj_kategorija():
	datum3 = input("Unesi te datum u gggg-mm-dd formatu: ")
	datum4 = input('Unesite datum u gggg-mm-dd formatu>> ')
	datum1 = datum3.split('-')
	datum2 = datum4.split('-')
	d1 = datum1[2]
	m1 = datum1[1]
	g1 = datum1[0]
	d2 = datum2[2]
	m2 = datum2[1]
	g2 = datum2[0]
	start_date = date(int(g1), int(m1), int(d1))
	end_date = date(int(g2), int(m2), int(d2))
	print('*'*55)
	print('{:^55}'.format('Izvestaj'))
	print('-'*55)
	print('{:<27}{:>28}'.format('Datum od', datum3))
	print('{:<27}{:>28}'.format('Datum do', datum4))
	print('-'*55)
	print('{:<15}{:<5}{:<10}{:<15}{:<10}'.format('Naziv kat.', 'kol', 'U. cena', 'Naziv NPRF','cena'))
	datumi = []
	lista_kategorija = []
	for single_date in daterange(start_date, end_date):
	    x = single_date.strftime("%Y-%m-%d")
	    for racun in racuni.racuni:
	    	if racun['datum'] == x:
	    		datum = racun['datum']
	    		if datum not in datumi:
	    			datumi.append(datum)
	    			izvestaj_kategorija2(datum3, datum4,lista_kategorija)

	print()
	print('*'*55)
	print()

def izvestaj_kategorija2(datum3, datum4,lista_kategorija):
	lista_namestaja = svi_namestaji(datum3, datum4)
	
	for kategorija in kategorije.kategorije:
		if kategorija['naziv'] not in lista_kategorija:
			lista_kategorija.append(kategorija['naziv'])
			#print(kategorija['naziv'])
			ukupno_kat = ukupno_kategorija(kategorija['naziv'], lista_namestaja)
			naj = najprofitabilniji(kategorija['naziv'], lista_namestaja)
			kol = ukupno_kolicina(kategorija['naziv'], lista_namestaja)
			print('{:<15}{:<5}{:<10}{:<15}{:<10}'.format(kategorija['naziv'],kol,ukupno_kat,naj['naziv'], naj['maks']))

def ukupno_kolicina(kategorija, lista_namestaja):
	ukupna_kol = 0
	for nam in lista_namestaja:
		if nam['kategorija'] == kategorija:
			x = int(nam['kolicina'])
			ukupna_kol += x
	return ukupna_kol



def najprofitabilniji(kategorija, lista_namestaja):
	elementi = []
	maks1 = []
	naj = {}
	for nam in lista_namestaja:
		if nam['kategorija'] == kategorija:
			najpr = int(nam['jcena']) * int(nam['kolicina'])
			maks1.append(najpr)
			elementi.append(nam)
	maks3 = maks(maks1)
	if maks3 == '/':
		naj['naziv'] = '/'
		naj['maks'] = '/'
	else:
		ele = najprofitabilniji1(elementi, maks3)
		naj['naziv'] = ele['naziv']
		naj['maks'] = maks3

	return naj
def maks(maks1):
	if maks1 == []:
		return '/'
	else:
		maks2 = max(maks1)
		return maks2

def najprofitabilniji1(elementi, maks):
	for element in elementi:
		r = int(element['jcena']) * int(element['kolicina'])
		maks = int(maks)
		if r == maks:
			return element


def ukupno_kategorija(kat, lista_namestaja):
	ukupno_kat = 0
	for nam in lista_namestaja:
		if nam['kategorija'] == kat:
			x = int(nam['jcena']) * int(nam['kolicina'])
			ukupno_kat += x
	return ukupno_kat



def svi_namestaji(datum3, datum4):
	datum1 = datum3.split('-')
	datum2 = datum4.split('-')
	d1 = datum1[2]
	m1 = datum1[1]
	g1 = datum1[0]

	d2 = datum2[2]
	m2 = datum2[1]
	g2 = datum2[0]
	if is_date_valid(g1,m1,d1) == False:
		print('Pogresan datum')
		izvestaj_kategorija()
	if is_date_valid(g2,m2,d2) == False:
		print('Pogresan datum')	
		izvestaj_kategorija()

	datumi = []
	start_date = date(int(g1), int(m1), int(d1))
	end_date = date(int(g2), int(m2), int(d2))
	lista = []
	for single_date in daterange(start_date, end_date):
	    x = single_date.strftime("%Y-%m-%d")
	    for racun in racuni.racuni:
	    	if racun['datum'] == x:
	    		datum = racun['datum']
	    		if datum not in datumi:
	    			datumi.append(datum)
	    			lista_namestaja = svi_namestaji2(lista, datumi)
	return lista_namestaja

def svi_namestaji2(lista_namestaja, datumi):
	namestaj12 = []
	for racun in racuni.racuni:
		if racun['datum'] in datumi:
			namestaj1 = racun['namestaj'].split('^')
			namestaj12.append(namestaj1)
	for namestaj1 in namestaj12:
		for namestaj in namestaj1:
			lista_namestaja.append(racuni.namestaji_u_recnike(namestaj))
	return lista_namestaja








	
