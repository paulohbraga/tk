import tkinter as tk

def show_img():

	class Image:

		def __init__(self, master=None):

			self.frame = tk.Frame(master)
			self.frame.pack()
			self.label = tk.Label(self.frame, text="Texto")
			self.label.pack()
			self.text = tk.Text(self.frame)
			self.text["font"] = ("Calibri", "25")
			self.text["width"] = 50
			self.text["height"] = 10
			self.text.pack()
			self.botao = tk.Button(self.frame)
			self.botao["text"] = "Converter"
			self.botao["command"] = self.texto
			self.botao.pack()

			self.text2 = tk.Text(self.frame)
			self.text2["font"] = ("Calibri", "25")
			self.text2["width"] = 50
			self.text2["height"] = 10
			self.text2.pack()

		def texto(self):
			self.text2.insert("1.0", self.text.get("1.0", "end"))

	root1 = tk.Tk()
	Image(root1)
	root1.mainloop()
