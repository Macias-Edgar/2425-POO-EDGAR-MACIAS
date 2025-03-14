import tkinter as tk
from tkinter import messagebox

# Función para agregar datos a la lista
def agregar_dato():
    dato = entrada_texto.get()
    if dato:  # Verifica que el campo no esté vacío
        lista_datos.insert(tk.END, dato)  # Agrega el dato a la lista
        entrada_texto.delete(0, tk.END)  # Limpia el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Ingrese un dato antes de agregar.")

# Función para limpiar los datos seleccionados o toda la lista
def limpiar_datos():
    seleccion = lista_datos.curselection()  # Obtiene los elementos seleccionados
    if seleccion:
        for i in reversed(seleccion):  # Borra los elementos seleccionados
            lista_datos.delete(i)
    else:
        lista_datos.delete(0, tk.END)  # Borra todos los datos si no hay selección

# Creación de la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")  # Título de la ventana
ventana.geometry("400x300")  # Tamaño de la ventana

# Etiqueta descriptiva
tk.Label(ventana, text="Ingrese un dato:").pack(pady=5)

# Campo de texto para entrada de datos
entrada_texto = tk.Entry(ventana, width=40)
entrada_texto.pack(pady=5)

# Botón para agregar datos
boton_agregar = tk.Button(ventana, text="Agregar", command=agregar_dato)
boton_agregar.pack(pady=5)

# Lista para mostrar los datos ingresados
lista_datos = tk.Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=5)

# Botón para limpiar datos
boton_limpiar = tk.Button(ventana, text="Limpiar", command=limpiar_datos)
boton_limpiar.pack(pady=5)

# Iniciar el bucle de eventos de Tkinter
ventana.mainloop()
