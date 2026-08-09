import tkinter as tk
from modelo import VentasModelo
from vista import VentasVista
from controlador import VentasControlador

if __name__ == "__main__":
    root = tk.Tk()
    modelo = VentasModelo()
    vista = VentasVista(root)
    controlador = VentasControlador(modelo, vista)
    root.mainloop()
