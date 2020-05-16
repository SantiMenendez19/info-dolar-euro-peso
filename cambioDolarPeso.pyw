# Modulos
from tkinter import *
from tkinter import messagebox
from bs4 import BeautifulSoup
import requests
import sys
import os

# Funciones


def actualizarDolarOficial():
    req = requests.get("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
    if req.status_code != 200:
        return messagebox.showerror("Error al cargar la pagina", "La pagina no responde o no esta conectado")
    json = req.json()
    return json[0].get('casa').get('nombre') + "\nCompra: $ " + json[0].get('casa').get('compra') + " Venta: $ " + json[0].get('casa').get('venta')

def actualizarDolarBlue():
    req = requests.get("https://www.dolarsi.com/api/api.php?type=valoresprincipales")
    if req.status_code != 200:
        return messagebox.showerror("Error al cargar la pagina", "La pagina no responde o no esta conectado")
    json = req.json()
    return json[1].get('casa').get('nombre') + "\nCompra: $ " + json[1].get('casa').get('compra') + " Venta: $ " + json[1].get('casa').get('venta')

def actualizarEuro():
    req = requests.get("https://www.precioeuro.com.ar/")
    if req.status_code != 200:
        return messagebox.showerror("Error al cargar la pagina", "La pagina no responde o no esta conectado")
    soup = BeautifulSoup(req.text, "html.parser")
    return "Euro Oficial" + "\nVenta: $" + soup.find_all("td")[20].get_text() + "  Compra: $" + soup.find_all("td")[18].get_text()


def actualizarLabels():
    dolar_peso_label.config(text=actualizarDolar())
    messagebox.showinfo("Actualizacion", "Precios actualizados")


def fuenteMensaje():
    messagebox.showinfo("Acerca de las fuentes",
                        "Fuentes utilizadas:\nhttps://www.dolarsi.com\nhttps://www.precioeuro.com.ar")

def salida():
    valor = messagebox.askyesno("Salida","Desea salir?")
    if valor == 1:
        sys.exit(0)

# Main
ventanaPrincipal = Tk()
ventanaPrincipal.geometry("300x400+500+200")
ventanaPrincipal.resizable(0, 0)
ventanaPrincipal.title("Tasa de cambio")
ventanaPrincipal.iconbitmap("src/monedas.ico")

titulo_label = Label(ventanaPrincipal, text="Tasa de cambio Dolar-Peso-Euro",
                     font=("Arial", 14), bg="cyan").pack()

imagen_dolar = PhotoImage(file="src/billete-dolar.png")
imagen_dolar = imagen_dolar.subsample(4)
Label(ventanaPrincipal, image=imagen_dolar).place(x=70, y=30)

dolar_peso_oficial_label = Label(
    ventanaPrincipal, text=actualizarDolarOficial(), font=("calibri", 12))
dolar_peso_oficial_label.place(x=30, y=110)

dolar_peso_blue_label = Label(
    ventanaPrincipal, text=actualizarDolarBlue(), font=("calibri", 12))
dolar_peso_blue_label.place(x=30, y=150)

imagen_euro = PhotoImage(file="src/billete-euro.png")
imagen_euro = imagen_euro.subsample(15)
Label(ventanaPrincipal, image=imagen_euro).place(x=70, y=200)

euro_peso_label = Label(
    ventanaPrincipal, text=actualizarEuro(), font=("calibri", 12))
euro_peso_label.place(x=30, y=280)

actualizar_button = Button(
    ventanaPrincipal, text="Actualizar", font="Arial", command=actualizarLabels)
actualizar_button.place(x=100, y=320)

barraMenu = Menu(ventanaPrincipal)
ventanaPrincipal.config(menu=barraMenu)
fuentesMenu = Menu(barraMenu, tearoff=0)
fuentesMenu.add_command(label="Fuentes", command=fuenteMensaje)
fuentesMenu.add_command(label="Salir", command=salida)

barraMenu.add_cascade(label="Ayuda", menu=fuentesMenu)

ventanaPrincipal.mainloop()
