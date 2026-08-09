import tkinter as tk
from tkinter import ttk, messagebox

class VentasVista:
    def __init__(self, root):
        self.root = root
        self.root.title("Cátedra Forrajicultura - UNNE")
        self.color_fondo = "#B9FF93"
        self.color_texto = "#030704"
        self.root.configure(bg=self.color_fondo)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_columnconfigure(2, weight=1)
        self.root.grid_columnconfigure(3, weight=1)
        self.crear_widgets()
    
    def crear_widgets(self):
        # Título
        self.titulo_label = tk.Label(self.root, text="Facultad de Ciencias Agrarias - UNNE", 
                                     font=("Arial", 16), bg=self.color_fondo, fg=self.color_texto)
        self.titulo_label.grid(row=0, column=0, columnspan=4, pady=10)
        
        # Cultivar (Combobox)
        tk.Label(self.root, text="Cultivar:", bg=self.color_fondo, fg=self.color_texto).grid(row=1, column=0, sticky="e")
        self.cultivar_combobox = ttk.Combobox(self.root, values=["Boyero FCA", "Chané FCA", "Cambá FCA"], width=15)
        self.cultivar_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        
        # Botón Agregar Venta
        self.btn_agregar = tk.Button(self.root, text="Agregar Venta")
        self.btn_agregar.grid(row=1, column=2, padx=5, pady=5, sticky="ew")
        
        # Cantidad
        tk.Label(self.root, text="Cantidad (KG):", bg=self.color_fondo, fg=self.color_texto).grid(row=2, column=0, sticky="e")
        self.cantidad_entry = tk.Entry(self.root, width=15)
        self.cantidad_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        vcmd = (self.root.register(self.validar_num), '%P')
        self.cantidad_entry.config(validate="key", validatecommand=vcmd)
        
        # Botón Ver Ventas
        self.btn_ver = tk.Button(self.root, text="Ver Ventas")
        self.btn_ver.grid(row=2, column=2, padx=5, pady=5, sticky="ew")
        
        # Cliente
        tk.Label(self.root, text="Nombre del Cliente:", bg=self.color_fondo, fg=self.color_texto).grid(row=3, column=0, sticky="e")
        self.cliente_entry = tk.Entry(self.root, width=15)
        self.cliente_entry.grid(row=3, column=1, padx=5, pady=5, sticky="ew")
        
        # Botón Eliminar Venta
        self.btn_eliminar = tk.Button(self.root, text="Eliminar Venta")
        self.btn_eliminar.grid(row=3, column=2, padx=5, pady=5, sticky="ew")
        
        # Teléfono
        tk.Label(self.root, text="Teléfono del Cliente:", bg=self.color_fondo, fg=self.color_texto).grid(row=4, column=0, sticky="e")
        self.telefono_entry = tk.Entry(self.root, width=15)
        self.telefono_entry.grid(row=4, column=1, padx=5, pady=5, sticky="ew")
        vcmd_tel = (self.root.register(self.validar_num), '%P')
        self.telefono_entry.config(validate="key", validatecommand=vcmd_tel)
        
        # Botón Modificar Venta
        self.btn_modificar = tk.Button(self.root, text="Modificar Venta")
        self.btn_modificar.grid(row=4, column=2, padx=5, pady=5, sticky="ew")
        
        # Vendedor (Combobox)
        tk.Label(self.root, text="Nombre del Vendedor:", bg=self.color_fondo, fg=self.color_texto).grid(row=5, column=0, sticky="e")
        self.vendedor_combobox = ttk.Combobox(self.root, values=["Alex", "Florencia", "Andrea", "Carlos"], width=15)
        self.vendedor_combobox.grid(row=5, column=1, padx=5, pady=5, sticky="ew")
        
        # Fecha
        tk.Label(self.root, text="Fecha de Venta (día/mes/año):", bg=self.color_fondo, fg=self.color_texto).grid(row=6, column=0, sticky="e")
        self.fecha_entry = tk.Entry(self.root, width=15)
        self.fecha_entry.grid(row=6, column=1, padx=5, pady=5, sticky="ew")
        
        # Treeview para mostrar ventas
        self.ventas_treeview = ttk.Treeview(self.root, 
            columns=("ID", "Cultivar", "Cantidad", "Cliente", "Telefono", "Vendedor", "Fecha"), 
            show="headings")
        self.ventas_treeview.heading("ID", text="ID")
        self.ventas_treeview.heading("Cultivar", text="Cultivar")
        self.ventas_treeview.heading("Cantidad", text="Cantidad (KG)")
        self.ventas_treeview.heading("Cliente", text="Cliente")
        self.ventas_treeview.heading("Telefono", text="Teléfono")
        self.ventas_treeview.heading("Vendedor", text="Vendedor")
        self.ventas_treeview.heading("Fecha", text="Fecha")
        self.ventas_treeview.grid(row=7, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
    
    def validar_num(self, value):
        return value.isdigit() or value == ""
    
    def limpiar_campos(self):
        self.cultivar_combobox.set('')
        self.cantidad_entry.delete(0, tk.END)
        self.cliente_entry.delete(0, tk.END)
        self.telefono_entry.delete(0, tk.END)
        self.vendedor_combobox.set('')
        self.fecha_entry.delete(0, tk.END)
        
    def mostrar_message_info(self, title, message):
        messagebox.showinfo(title, message)
    
    def mostrar_message_warning(self, title, message):
        messagebox.showwarning(title, message)
    
    def actualizar_treeview(self, ventas_list): # Ahora espera una lista de objetos Venta
        # Limpiar el treeview
        for item in self.ventas_treeview.get_children():
            self.ventas_treeview.delete(item)
        # Insertar cada venta
        for venta_obj in ventas_list: # Iterar sobre objetos Venta
            self.ventas_treeview.insert("", tk.END, values=(
                venta_obj.id,
                venta_obj.cultivar,
                venta_obj.cantidad,
                venta_obj.cliente,
                venta_obj.telefono,
                venta_obj.vendedor,
                venta_obj.fecha
            ))
    
    def get_input_data(self):
        return {
            'cultivar': self.cultivar_combobox.get(),
            'cantidad': self.cantidad_entry.get(),
            'cliente': self.cliente_entry.get(),
            'telefono': self.telefono_entry.get(),
            'vendedor': self.vendedor_combobox.get(),
            'fecha': self.fecha_entry.get()
        }
        
    def set_input_data(self, data):
        
        if hasattr(data, 'cultivar'):
            self.cultivar_combobox.set(data.cultivar if data.cultivar is not None else '')
            self.cantidad_entry.delete(0, tk.END)
            self.cantidad_entry.insert(0, data.cantidad if data.cantidad is not None else '')
            self.cliente_entry.delete(0, tk.END)
            self.cliente_entry.insert(0, data.cliente if data.cliente is not None else '')
            self.telefono_entry.delete(0, tk.END)
            self.telefono_entry.insert(0, data.telefono if data.telefono is not None else '')
            self.vendedor_combobox.set(data.vendedor if data.vendedor is not None else '')
            self.fecha_entry.delete(0, tk.END)
            self.fecha_entry.insert(0, data.fecha if data.fecha is not None else '')
        else: 
            self.cultivar_combobox.set(data.get('cultivar', ''))
            self.cantidad_entry.delete(0, tk.END)
            self.cantidad_entry.insert(0, data.get('cantidad', ''))
            self.cliente_entry.delete(0, tk.END)
            self.cliente_entry.insert(0, data.get('cliente', ''))
            self.telefono_entry.delete(0, tk.END)
            self.telefono_entry.insert(0, data.get('telefono', ''))
            self.vendedor_combobox.set(data.get('vendedor', ''))
            self.fecha_entry.delete(0, tk.END)
            self.fecha_entry.insert(0, data.get('fecha', ''))
    
    # callbacks controlador.

    def set_agregar_callback(self, callback):
        self.btn_agregar.config(command=callback)
    
    def set_ver_callback(self, callback):
        self.btn_ver.config(command=callback)
    
    def set_eliminar_callback(self, callback):
        self.btn_eliminar.config(command=callback)
    
    def set_modificar_callback(self, callback):
        self.btn_modificar.config(command=callback)
    
    def get_selected_venta_id(self):
        selected_items = self.ventas_treeview.selection()
        if selected_items:
            item = selected_items[0]
            venta = self.ventas_treeview.item(item, 'values')
            return venta[0] 
        return None