import tkinter as tk
from tkinter import messagebox
from biblioteca import Biblioteca

class BibliotecaApp:
    def __init__(self, root):
        self.biblioteca = Biblioteca()
        self.root = root
        self.root.title("Sistema de Reservas de Libros")

        # Cargar y mostrar imagen
        self.logo_image = tk.PhotoImage(file="logo.png")
        self.logo_label = tk.Label(root, image=self.logo_image)
        self.logo_label.pack()

        # Crear widgets para la interfaz de usuario
        self.title_label = tk.Label(root, text="Título")
        self.title_label.pack()

        self.title_entry = tk.Entry(root)
        self.title_entry.pack()

        self.author_label = tk.Label(root, text="Autor")
        self.author_label.pack()

        self.author_entry = tk.Entry(root)
        self.author_entry.pack()

        self.add_button = tk.Button(root, text="Agregar Libro", command=self.agregar_libro)
        self.add_button.pack()

        self.search_button = tk.Button(root, text="Buscar Libro", command=self.buscar_libro)
        self.search_button.pack()

        self.reserve_button = tk.Button(root, text="Reservar Libro", command=self.reservar_libro)
        self.reserve_button.pack()

        self.show_button = tk.Button(root, text="Mostrar Libros", command=self.mostrar_libros)
        self.show_button.pack()

    def agregar_libro(self):
        title = self.title_entry.get()
        author = self.author_entry.get()
        if title and author:
            self.biblioteca.agregar_libro(title, author)
            messagebox.showinfo("Éxito", f"El libro '{title}' ha sido agregado.")
        else:
            messagebox.showwarning("Error", "Por favor ingrese título y autor.")

    def buscar_libro(self):
        title = self.title_entry.get()
        if title:
            libro = self.biblioteca.buscar_libro(title)
            if libro:
                messagebox.showinfo("Búsqueda de Libro", f"Libro encontrado: {libro}")
            else:
                messagebox.showwarning("Error", "Libro no encontrado.")
        else:
            messagebox.showwarning("Error", "Por favor ingrese el título del libro.")

    def reservar_libro(self):
        title = self.title_entry.get()
        if title:
            exito = self.biblioteca.reservar_libro(title)
            if exito:
                messagebox.showinfo("Reserva de Libro", f"El libro '{title}' ha sido reservado.")
            else:
                messagebox.showwarning("Error", "No se pudo reservar el libro o el libro ya está reservado.")
        else:
            messagebox.showwarning("Error", "Por favor ingrese el título del libro.")

    def mostrar_libros(self):
        libros = []
        def callback(libro):
            libros.append(str(libro))
        
        self.biblioteca.arbol.in_orden(callback)
        if libros:
            messagebox.showinfo("Libros en Biblioteca", "\n".join(libros))
        else:
            messagebox.showinfo("Libros en Biblioteca", "No hay libros en la biblioteca.")

if __name__ == "__main__":
    main_window = tk.Tk()
    app = BibliotecaApp(main_window)
    main_window.mainloop()
