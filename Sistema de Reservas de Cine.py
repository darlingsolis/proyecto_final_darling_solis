##Sistema de Reservas de Cine

##Funcion para deplegar el menu principal
def menu_inicial():
    print("\n===== CineMax - Sistema de Reservas =====\n")
    print("1. Ver cartelera de un día")
    print("2. Mostrar asientos de una función")
    print("3. Reservar asiento")
    print("4. Cancelar reserva")
    print("5. Ver disponibilidad")
    print("6. Salir\n")

##Funcion para deplegar el menu de los 7 de las semana acompañado 
##por delante de un indice del 1 - 7
def menu_semanal():
    for i, clave in enumerate(cartelera, start=1):
            print(i, clave)

##Funcion para mostrar un indice de las 5 salas del cine
def sala():
    for i, clave in enumerate(cartelera[elecion], start=1):
        print(f"{i} Sala {clave['sala']}")

##Funcion para mostrar los asientos de manera entendible para el usuario
def mostrar_asientos(pelicula):
    matriz = pelicula["asientos"]

    letras_filas = ["Fila 1", "Fila 2", "Fila 3", "Fila 4", "Fila 5"]

    print("         As 1  As 2  As 3  As 4  As 5  As 6")

    for i, fila in enumerate(matriz):
        print(letras_filas[i], end="   ")

        for asiento in fila:
            print(asiento, end="   ")

        print()
        
##Dicionario que contiene gran parte del codigo que se utilizar en el while que esta mas abajo    
cartelera = {
    "Lunes": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 1, "horario": "2:00 pm", "formato": "Normal", "asientos" : []},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 2, "horario": "4:30 pm", "formato": "3D", "asientos" : []},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 3, "horario": "6:00 pm", "formato": "4DX", "asientos" : []},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 4, "horario": "5:30 pm", "formato": "Normal", "asientos" : []},
        {"pelicula": "El Final", "sala": 5, "horario": "8:00 pm", "formato": "CXC", "asientos" : []},
    ],
    "Martes": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 3, "horario": "5:00 pm", "formato": "4DX", "asientos" : []},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 1, "horario": "7:00 pm", "formato": "Normal", "asientos" : []},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 2, "horario": "3:00 pm", "formato": "Normal", "asientos" : []},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 5, "horario": "6:30 pm", "formato": "3D", "asientos" : []},
        {"pelicula": "El Final", "sala": 4, "horario": "9:00 pm", "formato": "Normal", "asientos" : []},
    ],
    "Miércoles": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 4, "horario": "4:00 pm", "formato": "Normal", "asientos" : []},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 5, "horario": "2:30 pm", "formato": "CXC", "asientos" : []},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 1, "horario": "7:30 pm", "formato": "3D", "asientos" : []},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 2, "horario": "5:00 pm", "formato": "Normal", "asientos" : []},
        {"pelicula": "El Final", "sala": 3, "horario": "8:30 pm", "formato": "4DX", "asientos" : []},
    ],
    "Jueves": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 2, "horario": "6:30 pm", "formato": "3D", "asientos" : []},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 3, "horario": "3:30 pm", "formato": "Normal", "asientos" : []},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 4, "horario": "8:00 pm", "formato": "Normal", "asientos" : []},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 1, "horario": "2:00 pm", "formato": "4DX", "asientos" : []},
        {"pelicula": "El Final", "sala": 5, "horario": "5:30 pm", "formato": "CXC", "asientos" : []},
    ],
    "Viernes": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 5, "horario": "4:00 pm", "formato": "Normal", "asientos" : []},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 4, "horario": "7:00 pm", "formato": "3D", "asientos" : []},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 1, "horario": "5:30 pm", "formato": "CXC", "asientos" : []},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 3, "horario": "9:00 pm", "formato": "Normal", "asientos" : []},
        {"pelicula": "El Final", "sala": 2, "horario": "2:30 pm", "formato": "4DX", "asientos" : []},
    ],
    "Sábado": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 1, "horario": "3:00 pm", "formato": "Normal", "asientos" : []},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 2, "horario": "6:00 pm", "formato": "4DX", "asientos" : []},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 5, "horario": "8:30 pm", "formato": "3D", "asientos" : []},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 4, "horario": "4:30 pm", "formato": "Normal", "asientos" : []},
        {"pelicula": "El Final", "sala": 3, "horario": "7:30 pm", "formato": "CXC", "asientos" : []},
    ],
    "Domingo": [
        {"pelicula": "Resident Evil: Noche Cero", "sala": 3, "horario": "2:30 pm", "formato": "3D", "asientos" : []},
        {"pelicula": "Avengers: Endgame (reestreno)", "sala": 5, "horario": "5:00 pm", "formato": "Normal", "asientos" : []},
        {"pelicula": "Los Juegos del Hambre: Sinsajo Pt. 2", "sala": 2, "horario": "7:00 pm", "formato": "CXC", "asientos" : []},
        {"pelicula": "Rápido y Furioso (reestreno)", "sala": 1, "horario": "8:30 pm", "formato": "4DX", "asientos" : []},
        {"pelicula": "El Final", "sala": 4, "horario": "4:00 pm", "formato": "Normal", "asientos" : []},
    ],
}

##En esta lista se guarda los datos del cliente que reservo el asiento y se guarda en forma de dicionario
reservaciones = []

##En este segmento del codigo creamos la matrices que representaran los asientos en nuestro programa
##en total son 30 asientos 5 filas de 6 asientos
for dia, peliculas in cartelera.items():

    for pelicula in peliculas:

        asientos = []

        for fila in range(5):
            fila_asientos = []

            for asiento in range(6):
                fila_asientos.append("(.)")

            asientos.append(fila_asientos)

        pelicula["asientos"] = asientos




dia_elegido = {"1":"Lunes",
               "2":"Martes",
               "3":"Miércoles",
               "4":"Jueves",
               "5":"Viernes",
               "6":"Sábado",
               "7":"Domingo",}


opcion = ""


##Bucle que nos ayudara hacer un menu interativo con el usuario          
while opcion != "6":
    menu_inicial()
    opcion = input("Seleccione una opción: ")
    print("")

    if opcion == "1":
        menu_semanal()
        dia_elegir = input("\nElige el dia que deseas visualizar la cartelera: ")
        if dia_elegir not in dia_elegido:
            print("Categoría no válida.")
            continue
        elecion = dia_elegido[dia_elegir]
        vizualizar = cartelera[elecion]

        print(f"\nCartelera del dia {elecion}\n")

##Este for nos jalará la cartelera del dia elegido por el usuario
        for datos in vizualizar:
            print(f"Pelicula: {datos['pelicula']}\nSala: {datos['sala']}\nHorario: {datos['horario']}\nFormato: {datos['formato']}\n")


    elif opcion == "2":

        menu_semanal()
        dia_elegir = input("\nElige el dia que deseas visualizar la cartelera: ")
        if dia_elegir not in dia_elegido:
            print("\nOpcion no válida.")
            continue
        
        elecion = dia_elegido[dia_elegir]

        sala()

##Aqui le colocamos -1 al input para que se pueda selecionar la opcion que eligio el usuario
##ya que las listas inician con idice en 0 y por ende se le debe restar 1 para jalar el dicionario
        sala_elegir = int(input("Elige la sala donde este la pelicula que deseas ver: ")) - 1
        
        if sala_elegir not in range (0,5):
            print("\nOpcion no válida.")
            continue
        print("\nNota:Son 5 filas de 6 asientos \nAs = Asiento\n")
        mostrar_asientos(cartelera[elecion][sala_elegir])

    elif opcion == "3":
        nombre = input("Digite su nombre: ")
        cedula = input("digite su numero de cedula (sin guiones): ")

        if 10 < len(cedula) < 12:
            print("\n")
        else:
            continue
        
        menu_semanal()
        dia_elegir = input("\nElige el dia que deseas agendar en la cartelera: ")
        if dia_elegir not in dia_elegido:
            print("\nOpcion no válida.")
            continue

        elecion = dia_elegido[dia_elegir]
        sala()
        sala_elegir = int(input("Elige la sala donde este la pelicula que deseas ver: ")) - 1
        
        if sala_elegir not in range (0,5):
            print("\nOpcion no válida.")
            continue
        print()

        mostrar_asientos(cartelera[elecion][sala_elegir])
        print("\nNota:Son 5 filas de 6 asientos \nAs = Asiento\n")
        elegir_fila = int(input("Elige la fila donde desees estar: ")) - 1
        if elegir_fila not in range(0,5):
            print("\nOpcion no válida.")
            continue
        elegir_asiento = int(input("Elige el asiento donde desees sentarte: ")) - 1
        if elegir_asiento not in range(0,7):
            print("\nOpcion no válida.")
            continue
        print("\n")
##Con esta linea evitamos que el usuario sobrescriba un asiento ya tomado, y tenga por obligacio
##tomar un registro diferente
        
        if cartelera[elecion][sala_elegir]["asientos"][elegir_fila][elegir_asiento] == "(X)":
            print("Este asiento esta ocupado")
            continue
##Si el usuario toma un registro diferente a la matrix que seleciono, se le agrega la X de asiento ocupado
        else:
            cartelera[elecion][sala_elegir]["asientos"][elegir_fila][elegir_asiento] = "(X)"
            mostrar_asientos(cartelera[elecion][sala_elegir])

            vizualizar = cartelera[elecion][sala_elegir]
            print(f"\nHas elegido:\nSala {vizualizar['sala']} \nPelicula: {vizualizar['pelicula']}\nHora: {vizualizar['horario']}\nFormato: {vizualizar['formato']}")
            reservacion = cartelera[elecion][sala_elegir]

##Aqui guardamos los datos del cliente en la lista resevaciones para suposterior uso
            
            datos_cliente = {
                "nombre": nombre,
                "cedula": cedula,
                "pelicula": vizualizar["pelicula"],
                "sala": vizualizar["sala"],
                "horario": vizualizar["horario"],
                "fila": elegir_fila,
                "asiento": elegir_asiento}
            
            reservaciones.append(datos_cliente)
            



    elif opcion == "4":

##Para llevar un control coherente el usario debera de validar con su numero de cedula
## si registro un asiento y tedra que repetir el proceso por cada asiento que tomó
        
        cedula_buscar = input("Digita su numero de cedula (sin guiones): ").strip()
        
        if 10 < len(cedula_buscar) < 12:
            print("\n")
        else:
            print("Cedula no valida")
            continue
        
        encontrado = False

        for reservacion in reservaciones:
            if reservacion['cedula'] == cedula_buscar:
                print(f"\nReserva encontrada para: {reservacion['nombre']}")
                print(f"Película: {reservacion['pelicula']}")
                print(f"Sala: {reservacion['sala']}")
                print(f"Horario: {reservacion['horario']}")

                fila = reservacion['fila']
                asiento = reservacion['asiento']

                 # Buscar la película/sala en la cartelera
                for pelicula in cartelera.values():
                    for funcion in pelicula:

                        if (funcion["pelicula"] == reservacion["pelicula"]
                                and funcion["sala"] == reservacion["sala"]
                                and funcion["horario"] == reservacion["horario"]):

                            funcion["asientos"][fila][asiento] = "(.)"

                            break
                reservaciones.remove(reservacion)

                print("\nReserva cancelada correctamente.")
                encontrado = True
                break


        if not encontrado:
            print("Codigo no encontrado")
            
    elif opcion == "5":

        menu_semanal()
        dia_elegir = input("\nElige el dia que deseas visualizar la cartelera: ")
        if dia_elegir not in dia_elegido:
            print("\nOpcion no válida.")
            continue
        
        elecion = dia_elegido[dia_elegir]

        sala()
        
        sala_elegir = int(input("Elige la sala donde este la pelicula que deseas ver: ")) - 1
        
        if sala_elegir not in range (0,5):
            print("\nOpcion no válida.")
            continue
        matriz = cartelera[elecion][sala_elegir]["asientos"]

        disponibles = 0
        ocupados = 0

        for fila in matriz:
            for asiento in fila:

                if asiento == "(.)":
                    disponibles += 1
                else:
                    ocupados += 1

        print(f"\nAsientos disponibles: {disponibles}")
        print(f"Asientos ocupados: {ocupados}")
        
    elif opcion == "6":
        print("\nHaz salido del programa\n")
        break

    else:
        print("Opcion invalida")
    
