# Modulo que cifra con el metodo Blowfish

from Crypto.Cipher import Blowfish
import secrets
import pedirDatos


# Generamos llave
def createKey():
    e=secrets.token_urlsafe(11)
    return e

# 
def encryptBlowfish():
    # Pedimos datos y creamos datos
    texto=pedirDatos.pedirDatos()
    e=createKey()
    
    # convertimos esa clave en Bites
    clave = bytes(e,"utf-8")
    print(clave)

    # Crear un objeto Blowfish para cifrar
    cipher = Blowfish.new(clave, Blowfish.MODE_CBC)
    
    # Nos aseguramos que la longitud sea multiplo de 8
    mensaje_bytes = texto.encode()
    longitud = 8 - (len(mensaje_bytes) % 8)
    mensaje_bytes += bytes([longitud] * longitud)

    # Ciframos el mensaje
    mensaje_cifrado = cipher.encrypt(mensaje_bytes)

    # Lo regresamos en forma hexa
    return mensaje_cifrado.hex()
    