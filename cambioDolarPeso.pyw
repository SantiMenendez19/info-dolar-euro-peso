# Modulos
from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests

# Funciones


def actualizarDolar():
    req = requests.get("https://www.precio-dolar.com.ar/")
    if req.status_code != 200:
        return messagebox.showerror("Error al cargar la pagina", "La pagina no responde o no esta conectado")
    soup = BeautifulSoup(req.text, "html.parser")
    return soup.find_all("span")[6].get_text() + "   " + soup.find_all("span")[5].get_text()


def actualizarEuro():
    req = requests.get("https://www.precioeuro.com.ar/")
    if req.status_code != 200:
        return messagebox.showerror("Error al cargar la pagina", "La pagina no responde o no esta conectado")
    soup = BeautifulSoup(req.text, "html.parser")
    return "Venta: $" + soup.find_all("td")[20].get_text() + "  Compra: $" + soup.find_all("td")[18].get_text()


def actualizarLabels():
    dolar_peso_label.config(text=actualizarDolar())
    messagebox.showinfo("Actualizacion", "Precios actualizados")


def fuenteMensaje():
    messagebox.showinfo("Acerca de las fuentes",
                        "Fuentes utilizadas:\nhttps://www.precio-dolar.com.ar/\nhttps://www.precioeuro.com.ar/")


# Main
ventanaPrincipal = Tk()
ventanaPrincipal.geometry("300x300+500+200")
ventanaPrincipal.resizable(0, 0)
ventanaPrincipal.title("Tasa de cambio")
ventanaPrincipal.iconbitmap("monedas.ico")

titulo_label = Label(ventanaPrincipal, text="Tasa de cambio Dolar-Peso-Euro",
                     font=("Arial", 14), bg="green").pack()

imagen_dolar = PhotoImage(file="billete-dolar.png")
imagen_dolar = imagen_dolar.subsample(4)
Label(ventanaPrincipal, image=imagen_dolar).place(x=70, y=30)

dolar_peso_label = Label(
    ventanaPrincipal, text=actualizarDolar(), font=("calibri", 12))
dolar_peso_label.place(x=30, y=90)

imagen_euro = PhotoImage(file="billete-euro.png")
imagen_euro = imagen_euro.subsample(15)
Label(ventanaPrincipal, image=imagen_euro).place(x=70, y=130)

euro_peso_label = Label(
    ventanaPrincipal, text=actualizarEuro(), font=("calibri", 12))
euro_peso_label.place(x=30, y=200)

actualizar_button = Button(
    ventanaPrincipal, text="Actualizar", font="Arial", command=actualizarLabels)
actualizar_button.place(x=40, y=250)

barraMenu = Menu(ventanaPrincipal)
ventanaPrincipal.config(menu=barraMenu)
fuentesMenu = Menu(barraMenu, tearoff=0)
fuentesMenu.add_command(label="Fuentes", command=fuenteMensaje)

barraMenu.add_cascade(label="Ayuda", menu=fuentesMenu)

ventanaPrincipal.mainloop()
