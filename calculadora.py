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


# Pantalla
pantalla = tk.Entry(ventana, width=12, bd=6, justify="right", font=("Arial", 24))
pantalla.grid(row=0, column=0, columnspan=4)


# Botones

siete = tk.Button(ventana, text=7, width=7, height=4, command=lambda: agregar_en_pantalla(7), font=("Arial", 12))
siete.grid(row=1, column=0)
ocho = tk.Button(ventana, text=8, width=7, height=4, command=lambda: agregar_en_pantalla(8))
ocho.grid(row=1, column=1)
nueve = tk.Button(ventana, text=9, width=7, height=4, command=lambda: agregar_en_pantalla(9))
nueve.grid(row=1, column=2)
division = tk.Button(ventana, text="/", width=7, height=4, command=lambda: operar("/"))
division.grid(row=1, column=3)

cuatro = tk.Button(ventana, text=4, width=4, height=4, command=lambda: agregar_en_pantalla(4))
cuatro.grid(row=2, column=0)
cinco = tk.Button(ventana, text=5, width=4, height=4, command=lambda: agregar_en_pantalla(5))
cinco.grid(row=2, column=1)
seis = tk.Button(ventana, text=6, width=4, height=4, command=lambda: agregar_en_pantalla(6))
seis.grid(row=2, column=2)
multiplicacion = tk.Button(ventana, text="*", width=4, height=4, command=lambda: operar("*"))
multiplicacion.grid(row=2, column=3)

uno = tk.Button(ventana, text=1, width=4, height=4, command=lambda: agregar_en_pantalla(1))
uno.grid(row=3, column=0)
dos = tk.Button(ventana, text=2, width=4, height=4, command=lambda: agregar_en_pantalla(2))
dos.grid(row=3, column=1)
tres = tk.Button(ventana, text=3, width=4, height=4, command=lambda: agregar_en_pantalla(3))
tres.grid(row=3, column=2)
resta = tk.Button(ventana, text="-", width=4, height=4, command=lambda: operar("-"))
resta.grid(row=3, column=3)

punto = tk.Button(ventana, text=".", width=4, height=4, command=lambda: agregar_en_pantalla("."))
punto.grid(row=4, column=0)
cero = tk.Button(ventana, text=0, width=4, height=4, command=lambda: agregar_en_pantalla(0))
cero.grid(row=4, column=1)
igual = tk.Button(ventana, text="=", width=4, height=4, command=resultado_igual)
igual.grid(row=4, column=2)
suma = tk.Button(ventana, text="+", width=4, height=4, command=lambda: operar("+"))
suma.grid(row=4, column=3)

borrar = tk.Button(ventana, text="Borrar", width=22, height=4, command=borrar)
borrar.grid(row=5, column=0, columnspan=8)

ventana.mainloop()
