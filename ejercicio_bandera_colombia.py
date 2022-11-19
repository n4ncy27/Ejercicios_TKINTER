# Se importa la librería tkinter con todas sus funciones
from tkinter import *

# -----------------
# Ventana principal
# -----------------

# Se crea una variable ventana_principal que adquiere las características de un objeto Tk
ventana_principal = Tk()

#Título de la ventana
ventana_principal.title("Sistemas UIS")

#Dimensiones o tamaño de la ventana
ventana_principal.geometry("500x500")

# Deshabilitar botón de maximizar
ventana_principal.resizable(0, 0)

ventana_principal.config(bg="black")

# -----------------------
# frame entrada de datos
# -----------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="yellow", width=480, height=240)
frame_entrada.place(x=10,y=10)


frame_operaciones= Frame(ventana_principal)
frame_operaciones.config(bg="blue", width=480, height=120)
frame_operaciones.place(x=10,y=240)

frame_resultado = Frame(ventana_principal)
frame_resultado.config(bg="red", width=480, height=120)
frame_resultado.place(x=10,y=360)


#Logo de la app
logo = PhotoImage(file="img/logo_uis.png")
lb_logo = Label(frame_entrada, image=logo)
lb_logo.place(x=60, y=60)


#Etiqueta para el título
titulo = Label(frame_entrada, text="suma enteros")
titulo.config(bg="white", fg="blue", font=("Arial", 16))
titulo.place(x=170,y=10, width=230, height=30)

# etiqueta para x
lb_x = Label(frame_entrada, text= "X = ")
lb_x.config(bg="white", fg="blue", font=("Arial",16))
lb_x.place(x=240,y=50, width=115, height=30)

# entry para x 
entry_x = Entry(frame_entrada)
entry_x.config(font=("Arial",20), justify=LEFT,fg="blue")
entry_x.focus_set()
entry_x.place(x=355, y=50, width=115, height=30)

#se ejecuta el metodo mainloop () de la clase TK a atraves de la 
ventana_principal.mainloop()


#Se ejecuta el método mainloop() de la clase Tk a través de la instancia venatana_principal.
#  Este método despliega una ventana simple en pantalla y queda a la espera de lo que el usuario haga
#  (click en un botón, escribir, etc) cada acción del usuario se conoce como un evento. El método mainloop() 
# es un bucle infinito

ventana_principal.mainloop()