from cowin_api import CoWinAPI #pip install cowin
import time

cowin = CoWinAPI()

def avilablestates():
	print('States in which vaccine drive is being conducted :')
	states = cowin.get_states()
	states = states['states']
	statesavilableidwise = {}
	statesavilablenamewise = {}
	print ('ID  | states Name')
	for i in states:
		s = i.values()
		s = list(s)
		print(s[0],':',s[1])
		statesavilableidwise[s[0]]=s[1]
		statesavilablenamewise[s[1].lower()]=s[0]
	st = [statesavilablenamewise,statesavilableidwise]
	return st

def avilabledistricts(state_id):
	print('Districts in which vaccine drive is being conducted:')
	cowin = CoWinAPI()
	districts = cowin.get_districts(state_id)
	districts = districts['districts']
	districtsavilable = []
	districtsavilableidwise = {}
	districtsavilablenamewise = {}
	print ('ID  | Districts Name')
	for i in districts:
		d = i.values()
		d = list(d)
		print(d[0],':',d[1])
		districtsavilable.append(d)
		districtsavilableidwise[d[0]]=d[1]
		districtsavilablenamewise[d[1].lower()]=d[0]
	dt = [districtsavilablenamewise,districtsavilableidwise]
	return dt

def avilablecenterbydistrictID(district_id,date=time.strftime("%d-%m-%Y")):

	available_centers = cowin.get_availability_by_district(district_id, date)
	available_centers = available_centers['centers']
	print(available_centers)

def avilablecenterbypincode(pin_code,date=time.strftime("%d-%m-%Y")):
	
	available_centers = cowin.get_availability_by_pincode(pin_code, date)
	available_centers = available_centers['centers']

	print(available_centers)


