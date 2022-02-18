from Extra import iniciarAnalisis, iniciar, reporte
from pagina import asd  


# Array con las opciones del menu
menu_options = {
    1: "Cargar Data.",
    2: "Cargar Instrucciones",
    3: "Analizar.",
    4: "Crar Reporte",
    5: "Salir",
}

# For que imprime las opciones del menu
def print_menu():
    print("\n")
    for key in menu_options.keys():
        print(key, "--", menu_options[key])
    print("\n")

# Metodo main el cual tiene un ciclo while para imprimir el menu
if __name__ == "__main__":
    while True:
        print_menu()
        option = ""
        try:
            option = int(input("Ingrese un numero: "))
        except:
            print("Entrada incorrecta. Por favor ingrese un numero ...")
        if option == 1:
            print("Iniciando Analisis....")
            iniciarAnalisis()
        elif option == 2:
            print("Cargando Instrucciones...")
        elif option == 3:
            print("Analizando...")
            iniciar()
        elif option == 4:
            print("Generando reporte....")
            reporte()
        elif option == 5:
            print("Saliendo...")
            exit()
        else:
            print("Opcion invalida. Por favor ingresar un numero entre 1 y 5.")












































'''
#Función que limpia la pantalla y muestra nuevamente el menu
def menu():
	os.system('cls') # NOTA para windows tienes que cambiar clear por cls
	print ("***************Menu***************")
	print ("1.Cargar Data.")
	print ("2.Cargar Instrucciones.")
	print ("3.Analizar.")
	print ("4.Reportes.\n5.Salir.\n**********************************" )

#Bucle para que salga el menu 
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		print ("Hellooooo")
		
	elif opcionMenu=="2":
		print ("helllooo2222")
		
	elif opcionMenu=="3":
		print ("JOEL")
		
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
'''