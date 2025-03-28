import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    """Añade una nueva tarea a la lista."""
    task = entry_task.get().strip()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Advertencia", "No puedes añadir una tarea vacía.")

def mark_completed():
    """Marca la tarea seleccionada como completada cambiando su apariencia."""
    try:
        selected_index = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_index)
        listbox_tasks.delete(selected_index)
        listbox_tasks.insert(tk.END, f"✔ {task}")
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para marcarla como completada.")

def delete_task():
    """Elimina la tarea seleccionada de la lista."""
    try:
        selected_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_index)
    except IndexError:
        messagebox.showwarning("Advertencia", "Selecciona una tarea para eliminar.")

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")
root.geometry("400x400")

# Crear un campo de entrada para nuevas tareas
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=10)
entry_task.bind("<Return>", add_task)  # Permite añadir tareas con Enter

# Crear un Listbox para mostrar las tareas
listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.pack(pady=10)

# Crear botones para añadir, completar y eliminar tareas
btn_add = tk.Button(root, text="Añadir Tarea", command=add_task)
btn_add.pack(pady=5)

btn_complete = tk.Button(root, text="Marcar como Completada", command=mark_completed)
btn_complete.pack(pady=5)

btn_delete = tk.Button(root, text="Eliminar Tarea", command=delete_task)
btn_delete.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
