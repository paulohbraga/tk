from tkinter import *
	
def img():


	class Image():

		def __init__(self, master=None):

			self.imagem = PhotoImage(file="/Users/paulobraga/image.png")
			self.w = Label(image=self.imagem)
			self.w.imagem = self.imagem
			self.w.pack()


	root = Tk()
	Image(root)

	root.mainloop()