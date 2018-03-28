
class admin():
	def __init__(self):
		self.username=str(input("enter username"))
		self.password=str(input("enter password"))
		self.admin={}

	def createaccount(self):
		
		self.admin[self.username]=self.password
		return self.admin

	def login(self):
		name=input("enter username")
		if name in self.admin:
			password=input("enter pasword")
			if password==self.admin[name]:
				return"logged in "
		else:
			return "user or passwors is wrong "



	# def edit(self):
		


	# def delete(self)

x=admin()
print(x.createaccount())
print(x.login())