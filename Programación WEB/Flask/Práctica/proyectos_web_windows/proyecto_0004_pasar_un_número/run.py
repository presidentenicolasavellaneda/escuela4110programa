"""Este es el script de arranque de tu aplicación Flask. Aquí, si este archivo es ejecutado como programa principal 
(no importado), la aplicación Flask se inicia. El debug=True permite que la aplicación 
muestre errores detallados en el navegador, lo que ayuda durante el desarrollo."""

from app import app  # Importa la instancia de la aplicación Flask desde el paquete app

if __name__ == "__main__":
    app.run(debug=True)  # Ejecuta la aplicación con el modo de depuración activado
