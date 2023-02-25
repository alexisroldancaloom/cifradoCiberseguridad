from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import pedirDatos

def bitearMsj(mensaje):
    e=mensaje
    return bytes(e,"utf-8")


def encryptAES():

    # Mensaje y llave para cifrar
    mensaje=pedirDatos.pedirDatos()

    key = get_random_bytes(16)
    mensajeTo = bitearMsj(mensaje)

    # Definir modo de cifrado y vector de inicialización
    cifrado=AES.new(key,AES.MODE_CFB)
    iv=cifrado.iv

    mensajeEncriptado=cifrado.encrypt(mensajeTo)
    cifrado=AES.new(key,AES.MODE_CFB,iv=iv)
    descifrado=cifrado.decrypt(mensajeEncriptado)

    return mensajeEncriptado, descifrado 
