# PRACTICA DE TKINTER
#Se importa libreria tkinter con todas sus funciones

from tkinter import *

from tkinter import messagebox

#--------------------
# funciones de la app
#--------------------



def sumar():
    messagebox.showinfo("Suma 1.0", "Hizo click en el boton sumar")
    z = int(x.get()) + int(y.get())
    t_resultados.insert(INSERT, "La suma de " + x.get() + " + " + y.get() +" casi siempre es " + str(z) + "\n")

def borrar():
    messagebox.showinfo("Suma 1.0", "Los datos seran borrados...")
    x.set("")
    y.set("")
    t_resultados.delete("1.0","end")
def salir():
    messagebox.showinfo("Suma 1.0", "La app se cerrará...")
    ventana_principal.destroy()
    



# Ejercicio 1 tkinter 

#ventana principal





#se crea una variable llamada ventana_principal, que adquiere las caracteristiccas de un objeto Tk
ventana_principal = Tk()

#titulo de la ventana
ventana_principal.title("Sistemas UIS")

#Tamaño de la ventana, ancho y alto
ventana_principal.geometry("500x500")

#Deshabilitar el boton de maximizar
ventana_principal.resizable(0,0)

# Color de la ventana
ventana_principal.config(bg="black")


#--------------------
# variables globales
#--------------------

x = StringVar()
y = StringVar()
#--------------------
#frame entrada datos
#--------------------

frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg = "white", width = 480 , height = 240)
frame_entrada.place(x = 10, y = 10)

# Logo de la app
#logo = PhotoImage(file = "img/logo-uis.png")
#lb_logo = Label(frame_entrada, image = logo)
#lb_logo.place(x = 61 , y = 61)

# Etiquetas par el titulo de app
titulo = Label(frame_entrada, text = "Suma enteros")
titulo.config(bg = "white", fg = "blue", font = ("Arial",16))
titulo.place(x = 180, y = 10)

# Etiqueta para x
lb_x = Label(frame_entrada, text = "X = ")
lb_x.config(bg="white", fg="blue", font=("Arial",16))
lb_x.place(x=240, y=50, width=115, height=30)

# Entry para x
entry_x = Entry(frame_entrada, textvariable= x)
entry_x.config(font=("Arial",20), justify=LEFT,fg="blue")
entry_x.focus_set()
entry_x.place(x=335, y=50, width=115, height=30)

# Etiqueta para y
lb_y = Label(frame_entrada, text = "Y = ")
lb_y.config(bg="white", fg="blue", font=("Arial",16))
lb_y.place(x=240, y=90, width=115, height=30)

# Entry para y
entry_y = Entry(frame_entrada, textvariable= y)
entry_y.config(font=("Arial",20), justify=LEFT,fg="blue")
entry_y.place(x=335, y=90, width=115, height=30)


#--------------------
#frame operaciones
#--------------------

frame_operaciones = Frame(ventana_principal)
frame_operaciones.config(bg = "white", width = 480 , height = 120)
frame_operaciones.place(x = 10, y = 260)

# Boton para sumar
bt_sumar = Button(frame_operaciones, text="Sumar", command=sumar)
bt_sumar.place(x=45, y=45, width=100, height=30)

#Boton borrar
bt_borrar = Button(frame_operaciones, text="Borrar", command=borrar)
bt_borrar.place(x=190, y=45, width=100, height=30)




# Boton salir
bt_salir = Button(frame_operaciones, text="Salir", command=salir)
bt_salir.place(x=335, y=45, width=100, height=30)

# fram resultados

frame_resultados = Frame(ventana_principal)
frame_resultados.config(bg="white", width=480, height=100)
frame_resultados.place(x=10, y = 390)

#area de texto para resultados
t_resultados = Text(frame_resultados)
t_resultados.config(bg="green", fg="black", font=("Arial",20))
t_resultados.place(x=10,y=10, width=460, height= 80)

ventana_principal.mainloop()