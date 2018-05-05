from tkinter import *

class UserAdd():
	"""Class User add"""
	def __init__(self, master):
		# Frame pai de title
		self.head = Frame(master)
		self.head["padx"] = 110
		self.head["pady"] = 30
		self.head.pack()
		
		# Widget Label filho do frame title
		self.title = Label(self.head, text="User Registration")
		self.title["font"] = ("Calibri", "20", "bold")
		self.title["padx"] = 50
		self.title.pack()
		# Frame pai de user
		self.userName = Frame(master)
		self.userName.pack()
		# Widget Entry filho do frame user: name
		self.nameLabel = Label(self.userName, text="Username:")
		self.nameLabel["width"] = 10
		self.nameLabel["font"] = ("Arial", "18")
		self.nameLabel.pack(side=LEFT)
		# Entrada de name
		self.name = Entry(self.userName)
		self.name["width"] = 20
		self.name.pack()
	
		# Frame pai de password
		self.userPass = Frame(master)
		self.userPass.pack()
		# Widget Entry filho do frame user: password
		self.passLabel = Label(self.userPass, text="Password:")
		self.passLabel["width"] = 10
		self.passLabel["font"] = ("Arial", "18")
		self.passLabel.pack(side=LEFT)
		# Entrada de password
		self.password = Entry(self.userPass, show="*")
		self.password["width"] = 20
		self.password.pack()

		# Frame Button login
		self.buttonLogin = Frame(master)
		self.buttonLogin["pady"] = 30
		self.buttonLogin.pack()
		# Button widget
		self.button = Button(self.buttonLogin)
		self.button["text"] = "Register"
		self.button["font"] = ("Calibri", "20")
		self.button["command"] = self.check_user
		self.button.pack()

		# Frame message
		self.message = Frame(master)
		self.message["pady"] = 20
		self.message.pack()
		# Widget login message
		self.messagelogin = Label(self.message)
		self.messagelogin["font"] = ("Arial", "18")
		self.messagelogin.pack()

		self.file = "users.db"
		self.login_user = "paulo"
		self.password_user = "123123"

	def check_user(self):
		if self.name.get() == self.login_user and self.password.get() == self.password_user:
			self.messagelogin["text"] = "Login sucess"
		else:
			if self.name.get() != self.login_user:
				self.messagelogin["text"] = "User incorrect"
			elif self.password.get() != self.password_user:
				self.messagelogin["text"] = "Wrong password"

root = Tk()
UserAdd(root)
root.title("User Registration")
root.mainloop()
