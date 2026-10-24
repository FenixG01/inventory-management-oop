import tkinter as tk
from tkinter import ttk, messagebox
from controller.producto_controller import ProductoController

class DashboardVentana:
    def __init__(self, root, usuario):
        self.root = root
        self.usuario = usuario # Guardamos el objeto (Admin o Empleado)
        self.root.title("Panel Principal - Papelería")
        self.root.geometry("820x540")
        self.root.configure(bg="#232326")

        self.controller = ProductoController()
        self._configurar_estilos()

        tk.Label(self.root, text=f"Bienvenido/a, {self.usuario.nombre_completo} ({self.usuario.rol})", 
                 font=("Helvetica", 12, "bold"), fg="#ffffff", bg="#232326").pack(pady=(15, 10))

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=25, pady=(0, 20))

        self.tab_inventario = tk.Frame(self.notebook, bg="#1a1a1c")
        self.notebook.add(self.tab_inventario, text="Inventario de Productos")

        self._crear_modulo_inventario()
        self._cargar_productos()

    def _configurar_estilos(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("TNotebook", background="#232326", borderwidth=0)
        style.configure("TNotebook.Tab", background="#37373a", foreground="#d0d0d0", padding=[12, 5])
        style.map("TNotebook.Tab", background=[("selected", "#505054")], foreground=[("selected", "#ffffff")])
        style.configure("Treeview", background="#18181a", foreground="#ffffff", fieldbackground="#18181a", rowheight=24)
        style.configure("Treeview.Heading", background="#252528", foreground="#e0e0e0")

    def _crear_modulo_inventario(self):
        contenedor = tk.Frame(self.tab_inventario, bg="#1a1a1c")
        contenedor.pack(fill="both", expand=True, padx=15, pady=15)

        # Formulario
        frame_form = tk.LabelFrame(contenedor, text=" Registrar Producto ", font=("Helvetica", 9, "bold"), 
                                   fg="#ffffff", bg="#1a1a1c", padx=12, pady=12)
        frame_form.pack(side="left", fill="y", padx=(0, 15))

        tk.Label(frame_form, text="Nombre:", fg="#ffffff", bg="#1a1a1c").pack(anchor="w")
        self.entry_nombre = tk.Entry(frame_form, bg="#111113", fg="#ffffff")
        self.entry_nombre.pack(fill="x", pady=(0, 10))

        tk.Label(frame_form, text="Número (ID):", fg="#ffffff", bg="#1a1a1c").pack(anchor="w")
        self.entry_numero = tk.Entry(frame_form, bg="#111113", fg="#ffffff")
        self.entry_numero.pack(fill="x", pady=(0, 10))

        tk.Label(frame_form, text="Descripción:", fg="#ffffff", bg="#1a1a1c").pack(anchor="w")
        self.entry_desc = tk.Entry(frame_form, bg="#111113", fg="#ffffff")
        self.entry_desc.pack(fill="x", pady=(0, 10))

        tk.Label(frame_form, text="Cantidad:", fg="#ffffff", bg="#1a1a1c").pack(anchor="w")
        self.entry_cant = tk.Entry(frame_form, bg="#111113", fg="#ffffff")
        self.entry_cant.pack(fill="x", pady=(0, 10))
        
        tk.Label(frame_form, text="Estado:", fg="#ffffff", bg="#1a1a1c").pack(anchor="w")
        self.combo_estado = ttk.Combobox(frame_form, values=["Disponible", "Agotado"])
        self.combo_estado.current(0)
        self.combo_estado.pack(fill="x", pady=(0, 18))

        tk.Button(frame_form, text="Guardar", bg="#ffffff", fg="#000000", command=self._guardar_producto).pack(fill="x", ipady=4)

        frame_botones = tk.Frame(frame_form, bg="#1a1a1c")
        frame_botones.pack(fill="x", pady=(15, 0))

        btn_modificar = tk.Button(frame_botones, text="Modificar", bg="#f1c40f", fg="#000000",
                      command=self._modificar_producto)
        btn_modificar.pack(fill="x", ipady=3, pady=(0, 5))

        btn_eliminar = tk.Button(frame_botones, text="Eliminar", bg="#e74c3c", fg="#ffffff",
                     command=self._eliminar_producto)
        btn_eliminar.pack(fill="x", ipady=3)

        # Tabla
        cols = ("ID", "Nombre", "Número", "Descripción", "Cantidad", "Estado")
        self.tabla = ttk.Treeview(contenedor, columns=cols, show="headings")
        for col in cols:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=100 if col != "Descripción" else 150)
        self.tabla.pack(side="left", fill="both", expand=True)

    def _cargar_productos(self):
        for item in self.tabla.get_children():
            self.tabla.delete(item)
        
        productos = self.controller.obtener_productos()
        for p in productos:
            self.tabla.insert("", tk.END, values=(p.id, p.nombre, p.numero, p.descripcion, p.cantidad, p.estado))

    def _guardar_producto(self):
        # Obtenemos los datos de la vista
        nombre = self.entry_nombre.get()
        numero = self.entry_numero.get()
        desc = self.entry_desc.get()
        cant = self.entry_cant.get()
        estado = self.combo_estado.get()

        # El controlador hace las validaciones y llama al modelo
        exito, mensaje = self.controller.guardar_producto(nombre, numero, desc, cant, estado)

        if exito:
            messagebox.showinfo("Éxito", mensaje, parent=self.root)
            self._cargar_productos()
        else:
            messagebox.showerror("Error", mensaje, parent=self.root)
    def _modificar_producto(self):
        # 1. Verificar que se seleccionó un producto de la tabla
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona un producto de la tabla para modificar.", parent=self.root)
            return
        
        # 2. Obtener los datos de la fila seleccionada
        item = self.tabla.item(seleccion[0])
        valores = item['values']
        id_producto = valores[0]

        # 3. Mandar los datos al controlador (necesitas crear este método en ProductoController)
        exito, mensaje = self.controller.actualizar_producto(
            id_producto, self.entry_nombre.get(), self.entry_numero.get(), 
            self.entry_desc.get(), self.entry_cant.get(), self.combo_estado.get()
        )

        if exito:
            messagebox.showinfo("Éxito", mensaje, parent=self.root)
            self._cargar_productos() # Refrescar tabla
        else:
            messagebox.showerror("Error", mensaje, parent=self.root)

    def _eliminar_producto(self):
        # 1. Verificar selección
        seleccion = self.tabla.selection()
        if not seleccion:
            messagebox.showwarning("Atención", "Selecciona un producto de la tabla para eliminar.", parent=self.root)
            return
        
        item = self.tabla.item(seleccion[0])
        valores = item['values']
        id_producto = valores[0]

        # 2. Confirmar acción
        confirmar = messagebox.askyesno("Confirmar", f"¿Seguro que deseas eliminar el producto '{valores[1]}'?", parent=self.root)
        
        if confirmar:
            # Llamar al controlador
            exito, mensaje = self.controller.eliminar_producto(id_producto)
            
            if exito:
                messagebox.showinfo("Éxito", mensaje, parent=self.root)
                self._cargar_productos()
            else:
                messagebox.showerror("Error", mensaje, parent=self.root)