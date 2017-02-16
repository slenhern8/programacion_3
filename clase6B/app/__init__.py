import re

if __name__ == "__main__":
    c1 = "casa"
    c2 = "casas"
    c3 = "pasa"
    c4 = input("Ingrese un texto: ")

    if re.match(c1, c2):  #evalua si c1 esta dentro de c2 evalua cadenas
        print("casa y casas coiciden")
    else:
        print("casa y casas no coiciden")

    if re.match(c1, c3):
        print("casa y pasa coiciden")
    else:
        print("casa y pasa no coiciden")

    if re.match(".asa", c4):   #el punto indica que puede ser cualquier caracter menos salto linea no importa mayus/minus numero o simbolo
        print("coiciden")   # el punto viene siendo un comodin
    else:
        print("no coiciden")

    if re.match("\.py", c4):    #si quieres buscar un punto pones el \ para que deje de ver el punto como comodin
        print("coiciden")
    else:
        print("no coiciden")

    if re.match("jpg|png|gif",c4):
        print("encontrado")
    else:
        print("no encontrado")

    if re.match("ca(..|...)ta", c4):  #este dice que empiecen con ca termine en ta y tenga 2 o 3 en medio
        print("encontrado")
    else:
        print("no encontrado")

    palabras = ["mana", "mata", "mama", "mana"]
    for p in palabras:
        if re.match("ma(s|m|n)a", p):
            print("encontrado ma")
        else:
            print("no encontrado ma")

    if re.match("r2\-d[0-5]", c4): #el - tambien le pones el \para que lo tome literal y el [] es un rango de 0 a 5 un solo caracter
        print("hola")
    else:
        print("adios")

    if re.fullmatch("c3p[0-3a-z]", c4): #fullmatch tiene que ser exactamente eso no solo que empiece con eso como match
        print("sup") #el rango es de 0-3 y a-z solo un caracter y solo minus si quieres tambien mayus tendrias que añadir otro rango [0-3a-zA-Z]
    else:
        print("bye")
#caracteres predefinidos:
    if re.fullmatch("ho\d",c4): #\d cualquier caracter que sea numero \D_todo menos numeros \w caracteres alfanumericos \W no alfanumericos
        print("jo")  #\s espacio en blanco  \S que no sea espacio en blanco
    else:
        print("ju")

#repeticiones: + puede aparecer 1 o varias veces   * 0 o varias veces    ?  0 o 1 vez  {} rango
    if re.fullmatch("[A-Z]+[a-z]*\s[1-9]{1,3}", c4): #de 1-N letras en mayus ,de 0-N letra minus, un espacio , de (1-9) 1-3 veces
        print("valido")#ejem (AAAAAAAaaaaaa 555)valido  (A 6)valido
    else:
        print("no valido")# (aaa 7777) no valido una mayus min y no mas de 3 numeros
#^ busca en el inicio   $ busca en el final

    if re.search(("^http://")and("\.com$"),c4):
        print("URL")
    else:
        print("NO URL")
