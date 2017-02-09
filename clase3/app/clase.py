def imprime_saludo():
    print("Xopa")

def imprime_nombre(nombre):
    imprime_saludo()
    print(nombre)

def suma(a,b):
    return a + b

if __name__ == "__main__":
    n = input("nombre: ")
    imprime_nombre(n)
    c = suma(1,5)
    print("La suma es " + str(c))
