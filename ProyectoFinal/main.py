# Modulo principal del proyecto
import des3
import aes
import blowfish

# Función con el unico objetivo de dar espacios arriba de los resultados
def marginTop():
    print("\t\t\t\t")    

# Funcion main
def main():
    # Bucle infinito para el menú
    while True:
        opcion = menu()
        print("\n \n \n ")

        # DES3
        if opcion == "1":
            print("Ha seleccionado la opción 1. DES3")
            mensajeCifrado=des3.encryptDES3()
            marginTop()
            print(f"---El mensaje cifrado es: {mensajeCifrado}")
            marginTop()
        # AES
        elif opcion == "2":
            print("Ha seleccionado la opción 2. AES")
            mensajeCifrado, descifrado=aes.encryptAES()
            marginTop()
            print(f"El mensaje cirfrado es {mensajeCifrado}")
            print(f"El mensaje descirfrado es {descifrado}")
            marginTop()

        # BlowFish
        elif opcion == "3":
            print("Ha seleccionado la opción 3. Blowfish")
            mensajeCifrado=blowfish.encryptBlowfish()
            marginTop()
            print(f"---El mensaje cifrado es: {mensajeCifrado}")
            marginTop()
        # Salir
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        # Opcion invalida
        else:
            print("Opción inválida. Intente de nuevo.")

# Menu de opciones
def menu():
    
    print("Bienvenido al menú.")
    print("1. Cifrado por DES3")
    print("2. Cifrado por AES")
    print("3. Cifrado por Blowfish")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")
    return opcion

# Vamos a llamar al main()

if __name__ == "__main__":
    main()