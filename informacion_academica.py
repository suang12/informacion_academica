#---------------------------------
# Desktop app No. 4 - Informacion Academica
#---------------------------------

# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

#periodo 1
def p1():
    messagebox.showinfo("Periodo 1", "Periodo 1")

#periodo 2
def p2():
    messagebox.showinfo("Periodo 2", "Periodo 2")
#periodo 3
def p3():    
    messagebox.showinfo("Periodo 3", "Periodo 3")

#periodo 4
def p4():
    messagebox.showinfo("Periodo 4", "Periodo 4")

#-----------------------------
# ventana principal de la app
#-----------------------------

# se declara una variable llamada ventana_principal, que adquiere las caracteristicas de un objeto Tk()
ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Brayan Suan")

# tamaño de la ventana
ventana_principal.geometry("600x600")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="blue")

#--------------------------------
# frame entrada datos
#--------------------------------
frame_entrada = Frame(ventana_principal)
frame_entrada.config(bg="white", width=480, height=180)
frame_entrada.place(x=60, y=20)

# logo de la app
logo = PhotoImage(file="IMG/boletinn.png", width=150, height=150)
lb_logo = Label(frame_entrada, image=logo, bg="white")
lb_logo.place(x=320,y=35)

# titulo de la app
titulo = Label(frame_entrada, text="Informacion Academica")
titulo.config(bg = "white",fg="blue", font=("Helvetica", 20))
titulo.place(x=110,y=10)

#--------------------------------
# barra menu
#--------------------------------
barra_menu = Menu()
ventana_principal.config(menu=barra_menu)

menu_periodo = Menu(tearoff=0)
menu_periodo.add_command(label="Menu", command=Menu)
menu_periodo.add_separator()
menu_periodo.add_command(label="p1", command=p1)
menu_periodo.add_command(label="p2", command=p2)
menu_periodo.add_command(label="p3", command=p3)
menu_periodo.add_command(label="p4", command=p4)
menu_salir = Menu(tearoff=0)
menu_salir.add_command(label="Salir", command="salir")

barra_menu.add_cascade(label="Menu", menu=menu_periodo)
barra_menu.add_cascade(label="Salir", menu=menu_salir)

#--------------------------------
# variables globales
#--------------------------------
nombre= StringVar()
apellido = StringVar()

 # etiqueta para nombre
lb_nombre= Label(frame_entrada, text = "nombre = ")
lb_nombre.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_nombre.place(x=60, y=60)

 # caja de texto para nombre
entry_nombre = Entry(frame_entrada, textvariable="Nombre")
entry_nombre.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
entry_nombre.focus_set()
entry_nombre.place(x=210,y=60)

# etiqueta para apellido
lb_apellido= Label(frame_entrada, text = "apellido = ")
lb_apellido.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_apellido.place(x=60, y=100)

entry_apellido = Entry(frame_entrada, textvariable="Apellido")
entry_apellido.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
entry_apellido.focus_set()
entry_apellido.place(x=210,y=100)

# etiqueta para grado
lb_grado= Label(frame_entrada, text = "grado = ")
lb_grado.config(bg="white", fg="blue", font=("Helvetica", 18))
lb_grado.place(x=60, y=140)

 # caja de texto para nombre
entry_grado = Entry(frame_entrada, textvariable="grado")
entry_grado.config(bg="white", fg="blue", font=("Times New Roman", 18), width=6)
entry_grado.focus_set()
entry_grado.place(x=210,y=140)


# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()