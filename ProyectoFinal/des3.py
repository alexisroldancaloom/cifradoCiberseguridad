import pedirDatos
from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes 

# le pasamos el numero de bytes que necesitamos para generar nuestra Key, en este caso, usaremos get_random_bytes con un largo de 24
def createKey():
    # Creamos una llave con una extensión de 24 bytes
    key = DES3.adjust_key_parity(get_random_bytes(24))
    return key


def encryptDES3():
    texto=pedirDatos.pedirDatos()
    key=createKey()
    cifrado = DES3.new(key, DES3.MODE_EAX)
    textoCifrado = cifrado.encrypt(texto.encode('ascii'))
    return textoCifrado
