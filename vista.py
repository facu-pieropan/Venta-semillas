import customtkinter as ctk
from tkinter import ttk, messagebox

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("green")

class VentasVista:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Ventas")
        self.root.geometry("850x680")
        self.root.minsize(800, 600)
        self.root.configure(bg="#1a1a1a")
        self.crear_widgets()
        
    def crear_widgets(self):
        self.titulo_label = ctk.CTkLabel(
            self.root, 
            text="🌱 Sistema de Registro de Ventas", 
            font=("Roboto", 24, "bold"),
            text_color="white")
        self.titulo_label.pack(pady=(20, 15))
        
        self.form_frame = ctk.CTkFrame(self.root, fg_color="#2b2b2b", corner_radius=12)
        self.form_frame.pack(fill="x", padx=20, pady=10)
        
        self.form_frame.grid_columnconfigure(0, weight=1)
        self.form_frame.grid_columnconfigure(1, weight=1)
        
        self.cultivar_combobox = ctk.CTkComboBox(self.form_frame, values=["Boyero FCA", "Chané FCA", "Cambá FCA"], width=240, height=38)
        self.cultivar_combobox.grid(row=0, column=0, padx=20, pady=15, sticky="ew")
        self.cultivar_combobox.set("Seleccionar Cultivar")
        
        self.cantidad_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Cantidad (KG)", width=240, height=38)
        self.cantidad_entry.grid(row=0, column=1, padx=20, pady=15, sticky="ew")
        
        self.cliente_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Nombre del Cliente", width=240, height=38)
        self.cliente_entry.grid(row=1, column=0, padx=20, pady=15, sticky="ew")
        
        self.telefono_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Teléfono (10 dígitos)", width=240, height=38)
        self.telefono_entry.grid(row=1, column=1, padx=20, pady=15, sticky="ew")
        
        self.vendedor_combobox = ctk.CTkComboBox(self.form_frame, values=["Alex", "Florencia", "Andrea", "Carlos"], width=240, height=38)
        self.vendedor_combobox.grid(row=2, column=0, padx=20, pady=15, sticky="ew")
        self.vendedor_combobox.set("Seleccionar Vendedor")
        
        self.fecha_entry = ctk.CTkEntry(self.form_frame, placeholder_text="Fecha (día/mes/año)", width=240, height=38)
        self.fecha_entry.grid(row=2, column=1, padx=20, pady=15, sticky="ew")
        
        self.btn_frame = ctk.CTkFrame(self.root, fg_color="transparent")
        self.btn_frame.pack(fill="x", padx=20, pady=10)
        
        self.btn_agregar = ctk.CTkButton(self.btn_frame, text="Agregar Venta", fg_color="#2fa572", hover_color="#248f5d", height=40, font=("Roboto", 12, "bold"))
        self.btn_agregar.pack(side="left", expand=True, padx=5, fill="x")
        
        self.btn_ver = ctk.CTkButton(self.btn_frame, text="Actualizar / Ver", fg_color="#1f538d", hover_color="#143d6b", height=40, font=("Roboto", 12, "bold"))
        self.btn_ver.pack(side="left", expand=True, padx=5, fill="x")
        
        self.btn_modificar = ctk.CTkButton(self.btn_frame, text="Modificar", fg_color="#d97706", hover_color="#b45309", height=40, font=("Roboto", 12, "bold"))
        self.btn_modificar.pack(side="left", expand=True, padx=5, fill="x")
        
        self.btn_eliminar = ctk.CTkButton(self.btn_frame, text="Eliminar", fg_color="#dc2626", hover_color="#b91c1c", height=40, font=("Roboto", 12, "bold"))
        self.btn_eliminar.pack(side="left", expand=True, padx=5, fill="x")
        
        self.tabla_frame = ctk.CTkFrame(self.root, fg_color="#2b2b2b", corner_radius=12)
        self.tabla_frame.pack(fill="both", expand=True, padx=20, pady=(10, 20))
        
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Treeview", 
            background="#1a1a1a", 
            foreground="white", 
            fieldbackground="#1a1a1a",
            rowheight=28,
            font=("Arial", 10)
        )
        style.configure("Treeview.Heading", 
            background="#333333", 
            foreground="white", 
            font=("Arial", 10, "bold")
        )
        style.map("Treeview", background=[('selected', '#2fa572')])

        self.ventas_treeview = ttk.Treeview(
            self.tabla_frame, 
            columns=("ID", "Cultivar", "Cantidad", "Cliente", "Telefono", "Vendedor", "Fecha"), 
            show="headings"
        )
        
        columnas_anchos = {"ID": 50, "Cultivar": 120, "Cantidad": 100, "Cliente": 140, "Telefono": 110, "Vendedor": 110, "Fecha": 100}
        for col in columnas_anchos:
            self.ventas_treeview.heading(col, text=col)
            self.ventas_treeview.column(col, width=columnas_anchos[col], anchor="center")
            
        self.ventas_treeview.pack(fill="both", expand=True, padx=12, pady=12)

    def limpiar_campos(self):
        self.cultivar_combobox.set("Seleccionar Cultivar")
        self.cantidad_entry.delete(0, "end")
        self.cliente_entry.delete(0, "end")
        self.telefono_entry.delete(0, "end")
        self.vendedor_combobox.set("Seleccionar Vendedor")
        self.fecha_entry.delete(0, "end")
        
    def mostrar_message_info(self, title, message):
        messagebox.showinfo(title, message)
    
    def mostrar_message_warning(self, title, message):
        messagebox.showwarning(title, message)
    
    def actualizar_treeview(self, ventas_list):
        for item in self.ventas_treeview.get_children():
            self.ventas_treeview.delete(item)
        for venta_obj in ventas_list:
            self.ventas_treeview.insert("", "end", values=(
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
            'cultivar': self.cultivar_combobox.get() if self.cultivar_combobox.get() != "Seleccionar Cultivar" else "",
            'cantidad': self.cantidad_entry.get(),
            'cliente': self.cliente_entry.get(),
            'telefono': self.telefono_entry.get(),
            'vendedor': self.vendedor_combobox.get() if self.vendedor_combobox.get() != "Seleccionar Vendedor" else "",
            'fecha': self.fecha_entry.get()
        }
        
    def set_input_data(self, data):
        if hasattr(data, 'cultivar'):
            self.cultivar_combobox.set(data.cultivar if data.cultivar else "Seleccionar Cultivar")
            self.cantidad_entry.delete(0, "end")
            self.cantidad_entry.insert(0, data.cantidad if data.cantidad is not None else '')
            self.cliente_entry.delete(0, "end")
            self.cliente_entry.insert(0, data.cliente if data.cliente is not None else '')
            self.telefono_entry.delete(0, "end")
            self.telefono_entry.insert(0, data.telefono if data.telefono is not None else '')
            self.vendedor_combobox.set(data.vendedor if data.vendedor else "Seleccionar Vendedor")
            self.fecha_entry.delete(0, "end")
            self.fecha_entry.insert(0, data.fecha if data.fecha is not None else '')
        else:
            self.cultivar_combobox.set(data.get('cultivar', 'Seleccionar Cultivar'))
            self.cantidad_entry.delete(0, "end")
            self.cantidad_entry.insert(0, data.get('cantidad', ''))
            self.cliente_entry.delete(0, "end")
            self.cliente_entry.insert(0, data.get('cliente', ''))
            self.telefono_entry.delete(0, "end")
            self.telefono_entry.insert(0, data.get('telefono', ''))
            self.vendedor_combobox.set(data.get('vendedor', 'Seleccionar Vendedor'))
            self.fecha_entry.delete(0, "end")
            self.fecha_entry.insert(0, data.get('fecha', ''))
    
    def set_agregar_callback(self, callback):
        self.btn_agregar.configure(command=callback)
    
    def set_ver_callback(self, callback):
        self.btn_ver.configure(command=callback)
    
    def set_eliminar_callback(self, callback):
        self.btn_eliminar.configure(command=callback)
    
    def set_modificar_callback(self, callback):
        self.btn_modificar.configure(command=callback)
    
    def get_selected_venta_id(self):
        selected_items = self.ventas_treeview.selection()
        if selected_items:
            item = selected_items[0]
            venta = self.ventas_treeview.item(item, 'values')
            return venta[0] 
        return None
