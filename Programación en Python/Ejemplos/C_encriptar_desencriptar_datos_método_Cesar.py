# este programa encripta datos 
# Explicación del Tema: Encriptar y Desencriptar un Mensaje
# La encriptación es un proceso crucial en la seguridad informática utilizado para proteger datos sensibles. 
# Consiste en convertir información legible en una forma cifrada que solo puede ser leída 
# o revertida a su forma original mediante un proceso de desencriptación con la clave adecuada.

# Métodos de Encriptación
# Hay dos tipos principales de encriptación: simétrica (donde se usa la misma clave para encriptar y desencriptar) 
# y asimétrica (donde se usan claves diferentes para encriptar y desencriptar, 
# conocidas como clave pública y clave privada).

# Ejemplo en Python: Encriptación Simple
# Aquí utilizaremos un método muy básico de encriptación simétrica llamado cifrado César, 
# que es un tipo de cifrado por sustitución en el que cada letra en el texto plano se "desplaza" 
# un cierto número de lugares a lo largo del alfabeto.

def cifrado_cesar(texto, desplazamiento):
    resultado = ""

    for i in range(len(texto)):
        char = texto[i]
        # Cifrar caracteres alfabéticos
        if char.isalpha():
            mayuscula = char.isupper()
            char = chr((ord(char) + desplazamiento - 65) % 26 + 65) if mayuscula else chr((ord(char) + desplazamiento - 97) % 26 + 97)
        resultado += char

    return resultado

def descifrado_cesar(texto_cifrado, desplazamiento):
    return cifrado_cesar(texto_cifrado, -desplazamiento)

# Uso del cifrado César
texto_original = "Hola Mundo"
desplazamiento = 4

texto_cifrado = cifrado_cesar(texto_original, desplazamiento)
print("Texto Cifrado:", texto_cifrado)

texto_descifrado = descifrado_cesar(texto_cifrado, desplazamiento)
print("Texto Descifrado:", texto_descifrado)

# Cuestionario sobre Encriptar y Desencriptar un Mensaje

# ¿Qué es la encriptación?
# a) Proceso de limpieza de datos
# b) Proceso de convertir información legible en cifrada
# c) Proceso de hacer copias de seguridad de datos
# Correcta: b

# ¿Cuál es el propósito principal de la encriptación?
# a) Aumentar la velocidad de transmisión de datos
# b) Proteger la integridad física de los dispositivos
# c) Proteger datos sensibles de accesos no autorizados
# Correcta: c

# ¿Qué tipo de encriptación utiliza la misma clave para encriptar y desencriptar?
# a) Asimétrica
# b) Simétrica
# c) Automática
# Correcta: b

# ¿Cómo funciona el cifrado César?
# a) Desplazando cada letra del texto un número específico de lugares en el alfabeto
# b) Reemplazando cada letra con un símbolo
# c) Invertiendo el orden de las letras
# Correcta: a

# ¿Qué tipo de clave se utiliza en la encriptación asimétrica para desencriptar un mensaje?
# a) Clave pública
# b) Clave privada
# c) Clave simétrica
# Correcta: b

# ¿Cuál es un ejemplo de encriptación simétrica?
# a) Cifrado RSA
# b) Cifrado César
# c) Cifrado de clave pública
# Correcta: b

# ¿Qué tipo de encriptación utiliza claves diferentes para encriptar y desencriptar?
# a) Simétrica
# b) Asimétrica
# c) Bidireccional
# Correcta: b

# ¿Para qué se usa la clave pública en la encriptación asimétrica?
# a) Para desencriptar mensajes
# b) Para encriptar mensajes
# c) No se utiliza en la encriptación
# Correcta: b
