from app.circunferencia import circunferencia

if __name__ == "__main__":
    radio =  float(input("radio: "))
    c1 = circunferencia(radio)
    c1_area = c1.calcular_area()
    c1_diametro = c1.calcular_diametro()
    print("area: "+ str(c1_area))
    print("diamtro: " + str(c1_diametro))

