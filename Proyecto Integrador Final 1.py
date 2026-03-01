# ============================================================
# PROYECTO INTEGRADOR - LOGICA DE PROGRAMACION
# Nombre del proyecto: El impacto de las nuevas tecnologias
#                      en la sociedad: visualizacion del futuro
# Programa: Generador de Contrasenas Seguras MEJORADO
# Objetivo: Generar contrasenas seguras segun las preferencias
#           del usuario y guardar un historial de las mismas
# ============================================================

import random
import string


# Use tuplas porque estos valores no deben cambiar
LETRAS_MINUSCULAS = tuple(string.ascii_lowercase)
LETRAS_MAYUSCULAS = tuple(string.ascii_uppercase)
NUMEROS = tuple(string.digits)
SIMBOLOS = tuple("!@#$%&*?-_")

# este diccionario va a guardar el historial de contrasenas generadas
historial = {}
contador_contrasenas = 0

#MENU
def mostrar_menu():
    print("\n========================================")
    print("   GENERADOR DE CONTRASENAS SEGURAS")
    print("========================================")
    print("1. Generar una nueva contrasena")
    print("2. Ver historial de contrasenas")
    print("3. Salir")
    print("========================================")



# Aqui vlido que el usuario ingrese un numero valido
def pedir_longitud():
    longitud = 0

    # Unidad 3 Ciclo while para repetir hasta que ingrese bien
    while longitud < 8 or longitud > 30:
        try:
            longitud = int(input("Que longitud quieres para tu contrasena? (minimo 8, maximo 30): "))

            # Unidad 3 Condicional IF con operadores relacionales
            if longitud < 8:
                print("Muy corta! Una contrasena segura debe tener al menos 8 caracteres.")
            elif longitud > 30:
                print("Muy larga! El maximo permitido es 30 caracteres.")
        except:
            print("Eso no es un numero valido, intenta de nuevo.")
            longitud = 0

    return longitud



def pedir_opciones():
    print("\n-- Personaliza tu contrasena --")


    respuesta_mayus = input("Incluir MAYUSCULAS? (s/n): ")
    if respuesta_mayus == "s" or respuesta_mayus == "S":
        usar_mayusculas = True
    else:
        usar_mayusculas = False

    respuesta_nums = input("Incluir NUMEROS? (s/n): ")
    if respuesta_nums == "s" or respuesta_nums == "S":
        usar_numeros = True
    else:
        usar_numeros = False

    respuesta_simb = input("Incluir SIMBOLOS (!@#...)? (s/n): ")
    if respuesta_simb == "s" or respuesta_simb == "S":
        usar_simbolos = True
    else:
        usar_simbolos = False

    # Diccionario para guardar las opciones elegidas
    opciones = {
        "mayusculas": usar_mayusculas,
        "numeros": usar_numeros,
        "simbolos": usar_simbolos
    }

    return opciones


#  Funcion principal que genera la contrasena
# Esta funcion recibe parametros
def generar_contrasena(longitud, opciones):

    # Unidad 4 - Lista donde voy juntando los caracteres disponibles
    caracteres_disponibles = list(LETRAS_MINUSCULAS)  # siempre incluye minusculas


    if opciones["mayusculas"] == True:
        caracteres_disponibles = caracteres_disponibles + list(LETRAS_MAYUSCULAS)

    if opciones["numeros"] == True:
        caracteres_disponibles = caracteres_disponibles + list(NUMEROS)

    if opciones["simbolos"] == True:
        caracteres_disponibles = caracteres_disponibles + list(SIMBOLOS)

    # Si el usuario dijo no a todo, igual tiene minusculas (ya estan en la lista)
    print("\nGenerando tu contrasena...")

    # Lista para ir armando la contrasena caracter por caracter
    contrasena_lista = []


    for i in range(longitud):
        caracter_random = random.choice(caracteres_disponibles)
        contrasena_lista.append(caracter_random)


    contrasena_final = ""
    for letra in contrasena_lista:
        contrasena_final = contrasena_final + letra

    return contrasena_final


# Funion para evaluar que tan segura es la contrasena ----
def evaluar_seguridad(contrasena, opciones):
    puntaje = 0


    if len(contrasena) >= 12:
        puntaje = puntaje + 1
    if len(contrasena) >= 16:
        puntaje = puntaje + 1
    if opciones["mayusculas"] == True:
        puntaje = puntaje + 1
    if opciones["numeros"] == True:
        puntaje = puntaje + 1
    if opciones["simbolos"] == True:
        puntaje = puntaje + 1


    if puntaje <= 1:
        nivel = "DEBIL"
    elif puntaje == 2 or puntaje == 3:
        nivel = "MEDIA"
    else:
        nivel = "FUERTE"

    return nivel


# Funcion para guardar en el historial ----
def guardar_en_historial(contrasena, longitud, nivel):
    global contador_contrasenas
    contador_contrasenas = contador_contrasenas + 1

    # Guardar en diccionario con clave numerica
    historial[contador_contrasenas] = {
        "contrasena": contrasena,
        "longitud": longitud,
        "seguridad": nivel
    }

    print("Contrasena guardada en el historial con el numero:", contador_contrasenas)


# ---- UNIDAD 4: Funcion para mostrar el historial ----
def mostrar_historial():
    # Unidad 3 - Condicional para verificar si hay algo en el historial
    if len(historial) == 0:
        print("\nTodavia no has generado ninguna contrasena.")
    else:
        print("\n--- HISTORIAL DE CONTRASENAS ---")

        # Unidad 3 - Ciclo for para recorrer el diccionario
        for numero in historial:
            datos = historial[numero]
            print(f"  #{numero} | Contrasena: {datos['contrasena']} | Longitud: {datos['longitud']} | Seguridad: {datos['seguridad']}")

        print("--------------------------------")


#
# PROGRAMA PRINCIPAL
# El problema: las personas usan contrasenas debiles y sus
# cuentas quedan vulnerables. Este programa las ayuda a
# generar contrasenas seguras facilmete

print("Bienvenido al Generador de Contrasenas Seguras")
print("Este programa te ayuda a crear contrasenas mas seguras")
print("para proteger tus cuentas en internet.")

seguir = True


while seguir == True:

    mostrar_menu()

    opcion = input("\nElige una opcion (1, 2 o 3): ")

    #Condicionales para manejar el menu
    if opcion == "1":
        longitud = pedir_longitud()
        opciones = pedir_opciones()
        contrasena = generar_contrasena(longitud, opciones)
        nivel = evaluar_seguridad(contrasena, opciones)

        print("\n========================================")
        print("  Tu contrasena generada es:")
        print(" ", contrasena)
        print("  Nivel de seguridad:", nivel)
        print("========================================")

        guardar = input("\nQuieres guardar esta contrasena en el historial? (s/n): ")
        if guardar == "s" or guardar == "S":
            guardar_en_historial(contrasena, longitud, nivel)

    elif opcion == "2":
        mostrar_historial()

    elif opcion == "3":
        print("\nGracias por usar el generador de contrasenas. Hasta luego!")
        seguir = False  # Unidad 3 - Alterador de ciclo (cambia la condicion del while)

    else:
        print("Opcion no valida, por favor elige 1, 2 o 3.")