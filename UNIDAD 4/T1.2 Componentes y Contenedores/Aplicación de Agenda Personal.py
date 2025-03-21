import tkinter as tk
from tkinter import ttk, messagebox


def agregar_evento():
    fecha = fecha_entry.get()
    hora = hora_entry.get()
    descripcion = descripcion_entry.get()

    if fecha and hora and descripcion:
        tree.insert('', 'end', values=(fecha, hora, descripcion))
        limpiar_campos()
    else:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")


def eliminar_evento():
    selected_item = tree.selection()
    if selected_item:
        confirm = messagebox.askyesno("Confirmación", "¿Está seguro de eliminar este evento?")
        if confirm:
            tree.delete(selected_item)
    else:
        messagebox.showwarning("Advertencia", "Seleccione un evento para eliminar")


def limpiar_campos():
    fecha_entry.delete(0, tk.END)
    hora_entry.delete(0, tk.END)
    descripcion_entry.delete(0, tk.END)


# Configuración de la ventana principal
root = tk.Tk()
root.title("Agenda Personal")
root.geometry("500x400")

# Frame para la entrada de datos
datos_frame = tk.Frame(root)
datos_frame.pack(pady=10)

tk.Label(datos_frame, text="Fecha:").grid(row=0, column=0, padx=5, pady=5)
fecha_entry = tk.Entry(datos_frame)
fecha_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(datos_frame, text="Hora:").grid(row=1, column=0, padx=5, pady=5)
hora_entry = tk.Entry(datos_frame)
hora_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(datos_frame, text="Descripción:").grid(row=2, column=0, padx=5, pady=5)
descripcion_entry = tk.Entry(datos_frame)
descripcion_entry.grid(row=2, column=1, padx=5, pady=5)

# Frame para botones
botones_frame = tk.Frame(root)
botones_frame.pack(pady=10)

tk.Button(botones_frame, text="Agregar Evento", command=agregar_evento).pack(side=tk.LEFT, padx=5)
tk.Button(botones_frame, text="Eliminar Evento", command=eliminar_evento).pack(side=tk.LEFT, padx=5)
tk.Button(botones_frame, text="Salir", command=root.quit).pack(side=tk.LEFT, padx=5)

# Frame para lista de eventos
lista_frame = tk.Frame(root)
lista_frame.pack(pady=10)

tree = ttk.Treeview(lista_frame, columns=("Fecha", "Hora", "Descripción"), show="headings")
tree.heading("Fecha", text="Fecha")
tree.heading("Hora", text="Hora")
tree.heading("Descripción", text="Descripción")
tree.pack()

# Ejecutar aplicación
root.mainloop()
