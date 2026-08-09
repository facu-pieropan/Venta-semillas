# Sistema de Gestión de Venta de Semillas

Sistema de escritorio desarrollado en Python bajo el patrón de diseño **Modelo-Vista-Controlador (MVC)**, diseñado para la gestión eficiente de ventas, clientes y registro de productos mediante interfaces gráficas intuitivas.

---

## Características Principales

* **Arquitectura MVC**: Separación clara de responsabilidades entre la lógica de datos, la interfaz de usuario y el controlador de eventos.
* **Persistencia de Datos**: Integración con **SQLite** para el almacenamiento local de registros.
* **Validación de Datos**: Reglas estrictas para el ingreso de información (validación de formatos numéricos, números telefónicos y campos obligatorios).
* **Gestión de Errores**: Sistema centralizado de excepciones personalizadas para garantizar la estabilidad de la aplicación.
* **Registro de Auditoría (Logging)**: Decoradores personalizados que generan registros detallados de las operaciones realizadas y trazas de errores para facilitar el mantenimiento.

---

## Estructura del Proyecto

* **`principal.py`**: Archivo de inicialización de la aplicación.
* **`modelo.py`**: Gestión de la lógica de datos y base de datos SQLite.
* **`vista.py`**: Interfaz gráfica de usuario construida con Tkinter.
* **`controlador.py`**: Lógica de interacción entre la vista y el modelo.
* **`entidades.py`**: Definición de la estructura de datos y métodos de validación.
* **`excepciones.py`**: Definición de errores personalizados del sistema.
* **`decoradores.py`**: Herramientas para el registro y monitoreo de la actividad (logging).

---

## Ejecución

1. Asegúrate de tener instalado **Python**.
2. Descarga los archivos del repositorio en una misma carpeta.
3. Ejecuta el siguiente comando en tu terminal dentro de la carpeta del proyecto:

```bash
python principal.py
