# encriptar y desencriptar metodo Fernet
# 1- pip install cryptography

from cryptography.fernet import Fernet

# Función para generar una clave de encriptación
def generar_clave():
    clave = Fernet.generate_key()
    with open("clave_secreta.key", "wb") as archivo_clave:
        archivo_clave.write(clave)

# Función para cargar la clave de encriptación
def cargar_clave():
    return open("clave_secreta.key", "rb").read()

# Generar y guardar la clave (solo necesita hacerse una vez)
generar_clave()

# Cargar la clave existente
clave = cargar_clave()
fernet = Fernet(clave)

# Mensaje a encriptar
mensaje = "Hola Mundo Seguro"
mensaje_bytes = mensaje.encode()

# Encriptar el mensaje
mensaje_encriptado = fernet.encrypt(mensaje_bytes)
print("Mensaje Encriptado:", mensaje_encriptado)

# Desencriptar el mensaje
mensaje_desencriptado = fernet.decrypt(mensaje_encriptado).decode()
print("Mensaje Desencriptado:", mensaje_desencriptado)

# Explicación del Código
# Generación de la clave: Primero, generamos una clave de encriptación segura usando Fernet.generate_key(), 
# y la guardamos en un archivo. Esto se hace solo una vez. 
# Puedes reutilizar la clave para futuras encriptaciones y desencriptaciones.

# Cargar la clave: La clave se lee desde el archivo cada vez que necesitas encriptar o desencriptar.

# Encriptación del mensaje: Convertimos el mensaje en bytes y luego lo encriptamos usando el método encrypt.

# Desencriptación del mensaje: El mensaje encriptado puede ser desencriptado usando el método decrypt, 
# y luego lo convertimos de bytes a string para que sea legible.

# Este método es mucho más seguro y robusto que el cifrado César y es adecuado 
# para aplicaciones prácticas donde la seguridad de los datos es crucial.
