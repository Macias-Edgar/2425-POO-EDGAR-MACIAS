import tkinter as tk
from tkinter import messagebox

def add_task(event=None):
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "No puedes agregar una tarea vacía.")

def mark_completed(event=None):
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        task_text = listbox_tasks.get(selected_task_index)
        if not task_text.startswith("✔ "):
            listbox_tasks.delete(selected_task_index)
            listbox_tasks.insert(selected_task_index, "✔ " + task_text)
    except IndexError:
        messagebox.showwarning("Aviso", "Selecciona una tarea para marcarla como completada.")

def delete_task(event=None):
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Aviso", "Selecciona una tarea para eliminarla.")

def exit_app(event=None):
    root.quit()

# Configurar la ventana principal
root = tk.Tk()
root.title("Gestor de Tareas")
root.geometry("400x400")

# Crear widgets
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=10)
entry_task.bind("<Return>", add_task)

btn_add = tk.Button(root, text="Añadir Tarea", command=add_task)
btn_add.pack()

listbox_tasks = tk.Listbox(root, width=50, height=15)
listbox_tasks.pack(pady=10)

btn_complete = tk.Button(root, text="Marcar Completada", command=mark_completed)
btn_complete.pack()

btn_delete = tk.Button(root, text="Eliminar Tarea", command=delete_task)
btn_delete.pack()

# Atajos de teclado
root.bind("<c>", mark_completed)
root.bind("<C>", mark_completed)
root.bind("<d>", delete_task)
root.bind("<D>", delete_task)
root.bind("<Delete>", delete_task)
root.bind("<Escape>", exit_app)

# Ejecutar la aplicación
root.mainloop()