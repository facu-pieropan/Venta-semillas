import functools
import logging
from datetime import datetime

logging.basicConfig(
    filename='app_log.log', 
    level=logging.INFO,     
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def log_operacion(func):
   
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
       
        try:
           
            relevant_args = [repr(a) for i, a in enumerate(args) if i > 0 or not isinstance(a, object)]
            relevant_kwargs = [f"{k}={repr(v)}" for k, v in kwargs.items()]
            signature = ", ".join(relevant_args + relevant_kwargs)
            if not signature and args and hasattr(args[0], '__class__'):
               
                signature = f"Método de {args[0].__class__.__name__}"
            elif not signature:
                signature = "Sin argumentos"

        except Exception:
            signature = "Argumentos no representables" 

        logging.info(f"Iniciando '{func_name}' con argumentos: ({signature})")

        try:
            result = func(*args, **kwargs)
            logging.info(f"Finalizado '{func_name}' exitosamente.") 
            return result
        except Exception as e:
            logging.error(f"Error en '{func_name}': {e}", exc_info=True)
            raise 
    return wrapper

def log_errores_bd(func):
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            logging.error(f"Error de BD en '{func.__name__}': {e}", exc_info=True)
            raise 
    return wrapper