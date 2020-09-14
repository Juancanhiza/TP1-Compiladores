# coding=utf-8

""" 
	Traductor Dirigido por la Sintáxis
	Recibe números {1 , 0} separados entre espacios y retorna la suma en su valor decimal
	Ejemplo:
		input: "10 111 01"
		output: 10

	@author: María José Melgarejo y Juan Cañiza
"""

entrada = input("Introduzca una cadena: ")
band=0
tam=len(entrada)

def sgte_caracter():
    
    global entrada, band
    if(entrada!=""):
        #Si la cadena empieza o termina con un espacio, se lanza un mensaje de error
        #y se finaliza la ejecucion
        if((entrada[0]==' ' and len(entrada)==1) or (entrada[0]==' ' and len(entrada)==tam)):
            print("Error.Cadena incompleta")
            entrada=""
            band=1

        #Si el primer caracter es 1, 0 o espacio se retorna el numero y se elimina
        #un caracter de la cadena de entrada
        elif(entrada[0]== '1' or entrada[0]== '0' or entrada[0]==' '):
            num = entrada[0]
            entrada = entrada[1:]
            return(num)

        #Si no el caracter no pertenece al alfabeto, se lanza un mensaje de error
        #y se termina la ejecucion
        else:
            print("Error. No pertenece al alfabeto de entrada")
            entrada=""
            band=1

    
def bit(b):
    #si el bit es 1 retorna 1, si es 0 retorna 0.
    if(b=='1'):
        return(1)
    else:
        return(0)

def lista(lista_x):
    num = sgte_caracter()

    #lista_x[0] --> valor en decimal de la cadena
    #lista_[1] --> exponente al que debe ser elevado el 2
    #Si el caracter es 1 o 0 se llama a la funcion bit, se vuelve a llamar a lista
    #Se eleva 2 al exponente guardado, se multiplica este por el valor obtenido en bit
    #Se le suma al valor acumulado en lista_x[0].
    if(num == '1' or num == '0'):
        bx = bit(num)
        lista_x = lista(lista_x)
        lista_x[0] = lista_x[0] + bx*(2**lista_x[1])
        lista_x[1]+=1
        return(lista_x)

    #Si es un espacio o vacio, se guarda 0 en lista_x[0] y lista_[1], se retorna el vector.
    else:
        lista_x=[0,0]
        return(lista_x)
   
def nro():
    Nro_x=0
    #Mientras la cadena no este vacia
    #Se llama a la funcion lista pasandole como parametro un vector inicializado en 0
    #El primer valor del vector lista_x se suma al acumulado en Nro_x
    while(entrada!=""):
        cadena=[0,0]
        lista_x = lista(cadena)
        Nro_x= Nro_x + lista_x[0]
    #Se retorna la suma
    return(Nro_x)

suma=nro()
if(band!=1):
    print("La suma decimal es: ",suma)

