import matplotlib
import matplotlib.pyplot as plt
import numpy as np 
from Token import Token, TokenDos


Productos=[]
Totales=[]

titulo=""
año=0

class AnalizadorLexico:
    def __init__(self):
        self.listaTokens = []
        self.listaErrores = []


    def analizar(self, cadena):
        self.listaTokens = []
        self.listaErrores = []

        cadena += '$'

        indice = 0
        buffer = ""
        estado = 'A'


        while indice < len(cadena):
            caracter = cadena[indice]
            #PARA LOS SIGNOS
            if estado == 'A':


                if caracter == '=':

                    buffer = ''
                    estado = 'A'
                elif caracter == ';':

                    buffer = ''
                    estado = 'A'
                elif caracter == '{':

                    buffer = ''
                    estado = 'A'
                elif caracter == '}':

                    buffer = ''
                    estado = 'A'
                elif caracter == '[':

                    buffer = ''
                elif caracter == ']':

                    buffer = ''
                    estado = 'A'
                elif caracter == '(':

                    buffer = ''
                elif caracter == ')':

                    buffer = ''
                    estado = 'A'
                elif caracter == ',':

                    buffer = ''
                    estado = 'A'

                elif caracter == ':':

                    buffer = ''
                    estado = 'A'
                elif caracter.isalpha() and (not caracter.isdigit()):
                    buffer = caracter

                    estado = 'B'
                elif caracter.isdigit():
                    buffer = caracter

                    estado = 'Z'



                elif caracter == '"':
                    buffer += caracter

                    estado = 'C'



                elif caracter == '$':

                    buffer = ''
                    estado = 'A'


            elif estado == 'B':
                if caracter.isalpha() and (not caracter.isdigit()):
                    buffer += caracter

                    estado = 'B'
                else:

                    global titulo
                    titulo=buffer
                    buffer = ''
                    estado = 'A'
                    indice -= 1

            elif estado == 'Z':
                if caracter.isdigit():
                    buffer += caracter

                    estado = 'Z'
                else:
                    #hacer validacion para las palabras reservadas
                    global año
                    año=buffer
                    buffer = ''
                    estado = 'A'
                    indice -= 1
                    #Para validar las cadenas
            elif estado == 'C':
                if caracter == '"':
                    buffer += caracter


                    producto =buffer.upper()
                    Productos.append(producto)
                    buffer = ''
                    estado = 'D'
                    indice+=1

                else:
                    buffer += caracter

                    estado = 'C'

            elif estado == 'D':
                if caracter == ',':

                    buffer = ''
                    estado = 'E'

                    #para numeros
            elif estado == 'E':
                if caracter.isdigit() or caracter==".":
                    buffer += caracter 

                    estado = 'E'
                else:
                    #antes de precio va un float
                    precio=float(buffer)

                    buffer = ''
                    indice -= 1
                    estado = 'F'

            if estado == 'F':
                if caracter == ',':

                    buffer = ''
                    estado = 'G'

            elif estado == 'G':
                if caracter.isdigit():
                    buffer += caracter 
                    estado = 'G'
                else:
                    cantidad=float(buffer)
                    precioFinal=float(cantidad*precio)
                    self.listaTokens.append(Token(producto, precio, cantidad, precioFinal))
                    Totales.append(precioFinal)

                    buffer = ''

                    estado = 'A'

            indice += 1
        return tuple(self.listaTokens), tuple(self.listaErrores)

    #INICIA SEGUNDO ANALIZADORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR

#--------------------------------------------------------------------------------------------------------------------


         #Definimos una lista con paises como string

    def graficaDeBarras(self):
        fig, ax = plt.subplots()
        #Colocamos una etiqueta en el eje Y
        ax.set_ylabel('TOTAL')
        #Colocamos una etiqueta en el eje X

        ax.set_title('REPORTE DE VENTAS '+ titulo.upper() )
        #Creamos la grafica de barras utilizando 'paises' como eje X y 'ventas' como eje y.
        plt.bar(Productos, Totales)
        plt.savefig('GraficaDebarras.png')
    #Finalmente mostramos la grafica con el metodo show()
        plt.show()

    def graficaPie(self):
        #Declaramos el tamaño de cada 'rebanada' y en sumatoria todos deben dar al 100%
        sizes = [45, 30, 15, 10]
        #En este punto señalamos que posicion debe 'resaltarse' y el valor, si se coloca 0, se omite
        fig1, ax1 = plt.subplots()
        #Creamos el grafico, añadiendo los valores
        ax1.pie(Totales, labels=Productos, autopct='%1.1f%%',
        shadow=True, startangle=90)
        #señalamos la forma, en este caso 'equal' es para dar forma circular
        ax1.axis('equal')
        plt.title('REPORTE DE VENTAS ' + titulo.upper())
        plt.legend()
        plt.savefig('grafica_pie.png')
        plt.show()

    #Grafica de lineas
    def graficaLineas(self):
        
       plt.plot(Productos, Totales)
        
       plt.title('REPORTE DE VENTAS ' + titulo.upper() )
       
       plt.plot(Totales, marker='x', linestyle=':', color='b')
       plt.savefig('grafica_linea.png')
       plt.show()

    #Grafica de lineas segundo intento xd
    '''
    def graficaLinea(self):
        plt.plot(Totales, marker='x', linestyle=':', color='b', label = Productos)
        plt.plot(Totales, marker='*', linestyle='-', color='g', label = Productos)
        plt.plot(Totales, marker='o', linestyle='--', color='r', label = Productos)
        plt.savefig('grafica_linea.png')
        plt.legend(loc="upper left")
        plt.show()
    '''

#REALIZANDO SEGUNDO ANALIZADOR 
