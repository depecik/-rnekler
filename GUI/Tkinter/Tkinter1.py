from tkinter import *
from tkinter import messagebox
pencere = Tk()
pencere.geometry("200x300+150+400")
pencere.resizable(width=False, height=False)
pencere.title("Vektörel Bilişim Python")
etiket = Label(text="Vektörel Bilişim",fg="blue",bg="white",cursor="man")
etiket["font"] = "Times 18 underline"
etiket.pack()
def degistir():
    etiket["text"] = "Düğme Çalıştı"
def ekranaYaz2():
    sonuc = messagebox.askquestion("Mesaj Baslik", "Buton2 Islendi")
    if sonuc == "yes":
        messagebox.showwarning("Baak","Emin Misin")


button1 = Button(text="Değiştir",command=degistir)
button1.pack()
button2 = Button(text="Mesaj",command=ekranaYaz2)
button2.pack()

mainloop()
