from tkinter import *


class SquareRoot():
	def __init__(self, master):

		self.menubar = Menu(master)
		self.master = master

		self.menu = Menu(self.menubar, tearoff=0)
		self.menu.add_command(label="Raiz", command=self.calcSquare)
		self.menu.add_separator()
		self.menu.add_command(label="Fechar", command=root.quit)
		self.menubar.add_cascade(label="Calculos", menu=self.menu)
		self.master.config(menu=self.menubar)


		self.widget1 = Frame(master)
		self.widget1["pady"] = 10
		self.widget1.pack()

		self.valor = Frame(master)
		self.valor["pady"] = 10
		self.valor.pack()

		self.widget2 = Frame(master)
		self.widget2.pack()

		self.widget3 = Frame(master)
		self.widget3.pack()

		self.label = Label(self.widget1, text="Cálculo Raiz Quadrada")
		self.label.pack()

		self.valor = Entry(self.valor, width="10")
		#self.valor.insert(0," Insira o valor aqui")
		#self.valor.delete(0, END)
		self.valor.pack()

		self.button1 = Button(self.widget2)
		self.button1["text"] = "Calcular"
		self.button1["command"] = self.calcSquare
		self.button1.pack(side=LEFT)

		self.clear = Button(self.widget2)
		self.clear["text"] = "Limpar"
		self.clear["command"] = self.clearEntry
		self.clear.pack()

		self.resultado = Label(self.widget3, text="0")
		self.resultado["font"] = ("Calibri", "14", "bold")
		self.resultado["pady"] = 25
		self.resultado.pack(side=LEFT)

	def calcSquare(self):
		if self.valor.get() != "":
			self.resultado["text"] = pow(int(self.valor.get()), 2)

	def clearEntry(self):
		if self.valor.get() != 0:
			self.valor.delete(0, END)
			self.resultado["text"] = 0

root = Tk()
SquareRoot(root)
root.title("Calculadora de raízes")
root.mainloop()
