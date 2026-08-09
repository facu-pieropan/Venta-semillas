# Sistema de Gestión de Venta de Semillas 

Sistema de escritorio desarrollado en Python utilizando el patrón de diseño **Modelo-Vista-Controlador (MVC)**, interfaces gráficas con **Tkinter** y persistencia de datos con **SQLite**.

---

## Estructura del Proyecto

* **`principal.py`**: Punto de entrada de la aplicación[cite: 6].
* **`modelo.py`**: Lógica de negocio y gestión de la base de datos SQLite (`venta_semillas.db`)[cite: 3].
* **`vista.py`**: Interfaz gráfica construida con Tkinter, menús desplegables y tablas dinámicas (*Treeview*)[cite: 5].
* **`controlador.py`**: Intermediario que gestiona las acciones de la interfaz y la comunicación con el modelo[cite: 4].
* **`entidades.py`**: Definición de la clase `Venta` y sus reglas de validación de datos (teléfonos, cantidades, campos obligatorios)[cite: 1].
* **`excepciones.py`**: Manejo de excepciones personalizadas para errores de validación y de base de datos[cite: 2].
* **`decoradores.py`**: Sistema de registro de eventos (*Logging*) para auditoría de operaciones y captura de errores[cite: 7].

---

## Requisitos y Ejecución

1. Tener instalado **Python** en la computadora.
2. Clonar o descargar este repositorio.
3. Abrir una terminal en la carpeta del proyecto y ejecutar el archivo principal:

```bash
python principal.py
