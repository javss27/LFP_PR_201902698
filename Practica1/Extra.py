from Analizador import AnalizadorLexico
from tkinter.filedialog import askopenfilename
from pagina import  asd

#Funcion para leer el archivo en memoria 

def leerArchivo(ruta):
        archivo = open(ruta, 'r')
        contenido = archivo.read()
        return contenido

def iniciarAnalisis():
        global ruta
        ruta = askopenfilename()
         
        
def iniciar():  
        a = AnalizadorLexico()
        
        contenido=leerArchivo(ruta)
        #a.analizar(contenido)
        a.analizar(contenido)
        print("Seleccione la grafica deseada: ")
        print("1-Grafica de Lineas. ")
        print("2-Grafica de Pie. ")
        print("3-Grafica de Barras. ")
        seleccion = int(input())
        if seleccion == 1:
                a.graficaLineas()
        elif seleccion == 2:
                a.graficaPie()
        elif seleccion == 3:
                a.graficaDeBarras()

        print("Analisis Exitoso")

def reporte():
        contenido = leerArchivo(ruta)
        a = AnalizadorLexico()
        b= asd
        #a.analizar(contenido)
        a.analizar(contenido)
        tokens, errs = a.analizar(contenido)
        b.process_file(tokens, errs)


