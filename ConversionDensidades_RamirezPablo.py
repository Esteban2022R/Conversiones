import tkinter as tk
#
ventana = tk.Tk()
ventana.title("Conversor")
ventana.geometry("700x600+800+200")
ventana.minsize(width=300, height=200)
ventana.configure(bg="orange")

#
def convertir():

    try:
        densidad = entrada_densidad.get()
        resultado = (float(densidad) * 62.428) 
        rotulo_resultado.config(text=resultado)
            
    except ValueError:
        pass



# 

rotulo_titulo = tk.Label(ventana, 
	text="CONVERSION DENSIDADES",
    bg="grey", fg="black",
    font= "consolas 20 bold",
    relief = tk.GROOVE, bd=2,
    padx=10, pady=10)
rotulo_titulo.pack(padx=20, pady=20)


# 

cuadro1 = tk.Frame(ventana,
    bg="grey")

rotulo_D1 = tk.Label(cuadro1,
    text="DENSIDAD\n(gr/cm3):",
    bg="grey",
    font="consolas 18 bold",
    width=12,
    anchor=tk.W)
rotulo_D1.pack(side=tk.LEFT, padx=15, pady=15)

entrada_densidad = tk.Entry(cuadro1,
    bg="white", fg="black",
    font="consolas 18 bold",
    relief=tk.SUNKEN,
    width=10,
    justify=tk.RIGHT,
    state="normal")
entrada_densidad.pack(side=tk.LEFT, padx=15, pady=15)

cuadro1.pack(pady=15)


# 

cuadro2 = tk.Frame(ventana,
    bg="grey")

rotulo_D2 = tk.Label(cuadro2,
    text="DENSIDAD\n(lbm/ft3):",
    bg="grey",
    font="consolas 18 bold",
    width=12,
    anchor=tk.W)
rotulo_D2.pack(side=tk.LEFT, padx=15, pady=15)

rotulo_resultado = tk.Label(cuadro2,
    text="",
    bg="grey",
    font="consolas 18 bold",
    width=10,
    relief = tk.GROOVE,
    anchor=tk.E)
rotulo_resultado.pack(side=tk.LEFT, padx=15, pady=15)

cuadro2.pack(pady=15)


#

cuadro3 = tk.Frame(ventana,
    bg="grey")

boton_borrar = tk.Button(cuadro3,
    text="Borrar",
    bg="grey",
    font="consolas 18 bold",
    width=10)
boton_borrar.pack(side=tk.LEFT, padx=20, pady=20)

boton_convertir = tk.Button(cuadro3,
    text="Convertir",
    bg="orange",
    font="consolas 18 bold",
    width=10,
    state="normal",
    command=convertir)
boton_convertir.pack(side=tk.LEFT, padx=20, pady=20)

cuadro3.pack(pady=10)


entrada_densidad.focus()


#

ventana.mainloop()
