# coding=utf-8

""" 
	Traductor Dirigido por la Sintáxis
	Recibe números {1 , 0} separados entre espacios y retorna la suma en su valor decimal
	Ejemplo:
		input: "10 111 01"
		output: 10

	@author: Juan Cañiza y María José Melgarejo
"""

inicio = 0
indice = 0
resultado = 0
lista_aux = []
msg_error = 'Se ingreso caracter no valido'

def suma(entrada):
	nro(entrada) 
	calcular(lista_aux)	
	print("El resultado es:", resultado)

def nro(entrada):
	global lista_aux, mayor

	lista(entrada[indice])
	if (indice < len(entrada)):
		calcular(lista_aux)
		lista_aux = []
		escape(entrada[indice])

def escape(e):
	if (e == ' '):
		match(e)
		nro(entrada)

def lista(e):
	bit(e)
	if (indice < len(entrada)):
		R(entrada[indice])

def R(e):
	if (e == '1' or e == '0'):
		lista(e)
	elif(e != ' '):
		raise NameError(msg_error)

def bit(e):
	if (e == '1' or e == '0'):
		match(int(e))
	else:
		raise NameError(msg_error)

def match(valor):
	global indice, lista_aux, inicio
	
	if (valor == 1):
		lista_aux.append(1)
	elif (valor == 0):
		lista_aux.append(0)
	elif(valor == ' '):
		inicio = indice + 1
	else:
		raise NameError(msg_error)
	indice += 1

def calcular(lista):
	global resultado
	
	mayor = len(lista)-1
	i=0
	for numero in lista:
		resultado += numero * 2**(mayor-i)
		i+=1

entrada = input("Ingrese la cadena a traducir: ")
suma(entrada)