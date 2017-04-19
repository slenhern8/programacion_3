if __name__ == "__main__":
    print("MENU\n   1. Imprimir Hola\n   2. Guardar Hola\n   3. Salir")
    flag = True
    while flag:
        try:
            op = int(input("Introduzca el numero de la opcion deseada: "))
            if op > 3 or op < 1:
                raise
            if op == 1:
                print(" Hola ")
            elif op == 2:
                sa=input("A: ")
                try:
                    archivo = open("archiv.csv", "a", newline='')
                    #archivo.write("Hola \n")
                    #archivo.write("hola2 \n")
                    archivo.write("\n" + sa + ", Hola")
                    archivo.close()
                except FileNotFoundError:
                    print("No existe el archivo")
                except:
                    print("Error")
            else:
                print(" Adios ")
                flag = False
        except ValueError:
            print("No introdujo un numero")
        except:
            print("Error")

