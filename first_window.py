from tkinter import *

def new():
	
	class Application:
		def __init__(self, master=None):
			self.widget1 = Frame(master)
			self.widget1["padx"] = 100
			self.widget1["pady"] = 100
			self.widget1.pack()
			self.widget2 = Frame(master)
			self.widget2["padx"] = 100
			self.widget2["pady"] = 100
			self.widget2.pack()
			self.segundoContainer = Frame(master)
			self.segundoContainer["padx"] = 20
			self.segundoContainer.pack()
			self.hello = Label(self.widget1, text="Olá Mundo!")
			self.hello["font"] = ("Calibri", "14", "italic", "bold")
			self.hello.pack()
			self.hello2 = Button(self.widget1)
			self.hello2["text"] = "Clique aqui"
			self.hello2["font"] = ("Calibri", "10")
			self.hello2["width"] = 10
			self.hello2["command"] = self.printHello
			self.hello2.pack()
			self.hello3 = Label(self.widget2, text="Olá Mundo!")
			self.hello3["font"] = ("Calibri", "14", "bold")
			self.hello3.pack(side=LEFT)
			self.nome = Entry(self.segundoContainer)
			self.nome["width"] = 30
			self.nome.pack(side=LEFT)

		def printHello(self):
			if self.hello["text"] == "Olá Mundo!":
				self.hello["text"] = "Hello World!"
			else:
				self.hello["text"] = "Olá Mundo!"


	root = Tk()
	Application(root)
	root.mainloop()

