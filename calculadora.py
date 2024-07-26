import tkinter as tk

ventana = tk.Tk()
valor_a = 0
valor_b = 0
operacion = "sumar"
resultado = 0

# Funciones
def sumar():
    global valor_a
    global valor_b
    return valor_a + valor_b

def restar():
    global valor_a
    global valor_b
    return valor_a - valor_b

def multiplicar():
    global valor_a
    global valor_b
    return valor_a*valor_b

def dividir():
    global valor_a
    global valor_b
    return valor_a/valor_b

def borrar():
    global pantalla
    pantalla.delete(0, tk.END)
   
    
def agregar_en_pantalla(valor):
    global pantalla
    pantalla.insert(tk.END, valor)
    
def operar(simbolo):
    global pantalla 
    global valor_a
    global operacion
    valor_a = float(pantalla.get())
    pantalla.delete(0, tk.END)
    if simbolo == "/":
        operacion = 'dividir'
    elif simbolo == "*":
        operacion = 'multiplicar'
    elif simbolo == "-":
        operacion = 'restar'
    else:
        operacion = 'sumar'
        
def resultado_igual():
    global pantalla
    global valor_a
    global valor_b
    global operacion
    global resultado
    valor_b = float(pantalla.get())
    pantalla.delete(0, tk.END)
    evaluacion = eval(operacion)
    resultado = evaluacion()
    pantalla.insert(tk.END, resultado)    
    

# Interfaz grafica

# Título
titulo = tk.Label(ventana, text="CALCULADORA", font=("Arial", 24, "bold"))
titulo.grid(row=0, column=0, columnspan=4)


# Pantalla
pantalla = tk.Entry(ventana, width=20, bd=6, justify="right", font=("Arial", 24))
pantalla.grid(row=1, column=0, columnspan=4)

# Tamaño de los botones
button_width = 5
button_height = 2
button_font = ("Arial", 20, "bold")

# Botones
siete = tk.Button(ventana, text=7, width=button_width, height=button_height, command=lambda: agregar_en_pantalla(7), font=button_font)
siete.grid(row=2, column=0)
ocho = tk.Button(ventana, text=8, width=button_width, height=button_height, command=lambda: agregar_en_pantalla(8), font=button_font)
ocho.grid(row=2, column=1)
nueve = tk.Button(ventana, text=9, width=button_width, height=button_height, command=lambda: agregar_en_pantalla(9), font=button_font)
nueve.grid(row=2, column=2)
division = tk.Button(ventana, text="/", width=button_width, height=button_height, command=lambda: operar("/"), font=button_font)
division.grid(row=2, column=3)

cuatro = tk.Button(ventana, text=4, width=button_width, height=button_height, command=lambda: agregar_en_pantalla(4), font=button_font)
cuatro.grid(row=3, column=0)
cinco = tk.Button(ventana, text=5, width=button_width, height=button_height, command=lambda: agregar_en_pantalla(5), font=button_font)
cinco.grid(row=3, column=1)
seis = tk.Button(ventana, text=6, width=button_width, height=button_height, command=lambda: agregar_en_pantalla(6), font=button_font)
seis.grid(row=3, column=2)
multiplicacion = tk.Button(ventana, text="*", width=button_width, height=button_height, command=lambda: operar("*"), font=button_font)
multiplicacion.grid(row=3, column=3)

uno = tk.Button(ventana, text=1, width=button_width, height=button_height, command=lambda: agregar_en_pantalla(1), font=button_font)
uno.grid(row=4, column=0)
dos = tk.Button(ventana, text=2, width=button_width, height=button_height, command=lambda: agregar_en_pantalla(2), font=button_font)
dos.grid(row=4, column=1)
tres = tk.Button(ventana, text=3, width=button_width, height=button_height, command=lambda: agregar_en_pantalla(3), font=button_font)
tres.grid(row=4, column=2)
resta = tk.Button(ventana, text="-", width=button_width, height=button_height, command=lambda: operar("-"), font=button_font)
resta.grid(row=4, column=3)

punto = tk.Button(ventana, text=".", width=button_width, height=button_height, command=lambda: agregar_en_pantalla("."), font=button_font)
punto.grid(row=5, column=0)
cero = tk.Button(ventana, text=0, width=button_width, height=button_height, command=lambda: agregar_en_pantalla(0), font=button_font)
cero.grid(row=5, column=1)
igual = tk.Button(ventana, text="=", width=button_width, height=button_height, command=resultado_igual, font=button_font)
igual.grid(row=5, column=2)
suma = tk.Button(ventana, text="+", width=button_width, height=button_height, command=lambda: operar("+"), font=button_font)
suma.grid(row=5, column=3)

borrar = tk.Button(ventana, text="Borrar", width=22, height=button_height, command=borrar, font=button_font)
borrar.grid(row=6, column=0, columnspan=4)

ventana.mainloop()