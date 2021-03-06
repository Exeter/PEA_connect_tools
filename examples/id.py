from PEA_connect import users
import json

#Repeatedly queries for ID numbers, and returns the appropriate info for that ID number

def pprint(x):
	print(json.dumps(x, indent=4, sort_keys=True))


u = users(by="EmployeeID")
def getEmailByEmployeeID(employeeid):
	user = u.get(employeeid)
	if not user:
		raise Exception('user not found')
	return user['WorkEmail']
def getNameByEmployeeID(employeeid):
	user = u.get(employeeid)
	if not user:
		raise Exception('user not found')
	first = user['FirstName']
	last = user['LastName']
	return first + ' ' + last

def query():
	try:
		employeeid = str(raw_input('EmployeeID: '))
		print(getNameByEmployeeID(employeeid))
		print(getEmailByEmployeeID(employeeid))
	except Exception:
		print('user not found')

if __name__ == '__main__':
	while True:
		query()
