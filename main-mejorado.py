import random

# QUITÉ ESTAS PRIMERAS LÍNEAS Y LAS PUSE DENTRO DEL MAIN, YA QUE AHÍ ES DONDE VERDADERAMENTE COMIENZA
# LA EJECUCIÓN DE TU PROGRAMA. ESTE ESPACIO DE ACÁ ARRIBA EN LÍNEAS GENERALES SOLO SE USA PARA
# IMPORTAR MÓDULOS Y DECLARAR FUNCIONES

def jugadores(eleccion, jugador1, jugador2):
    # SE LE ASIGNAN A JUGADOR1 Y JUGADOR2 SUS RESPECTIVOS NOMBRES Y NOMBRES DE OBJETIVOS
    if (eleccion == 1):
        jugador1["nombre"] = "Sandokan y sus amigos"
        jugador1["objetivos"][0][1] = "Fuerte"
        jugador1["objetivos"][1][1] = "Campamento de defensa"
        jugador1["objetivos"][2][1] = "Depósito de armas"
        jugador1["objetivos"][3][1] = "Defensa Norte"
        jugador1["objetivos"][4][1] = "Defensa Sur"

        jugador2["nombre"] = "Armada británica"
        jugador2["objetivos"][0][1] = "Crucero pesado"
        jugador2["objetivos"][1][1] = "Galeón"
        jugador2["objetivos"][2][1] = "Cañonero"
        jugador2["objetivos"][3][1] = "Galera"
        jugador2["objetivos"][4][1] = "Barcaza"
    else:
        jugador1["nombre"] = "Armada británica"
        jugador1["objetivos"][0][1] = "Crucero pesado"
        jugador1["objetivos"][1][1] = "Galeón"
        jugador1["objetivos"][2][1] = "Cañonero"
        jugador1["objetivos"][3][1] = "Galera"
        jugador1["objetivos"][4][1] = "Barcaza"
        
        jugador2["nombre"] = "Sandokan y sus amigos"
        jugador2["objetivos"][0][1] = "Fuerte"
        jugador2["objetivos"][1][1] = "Campamento de defensa"
        jugador2["objetivos"][2][1] = "Depósito de armas"
        jugador2["objetivos"][3][1] = "Defensa Norte"
        jugador2["objetivos"][4][1] = "Defensa Sur"

    print("El jugador 1 será ", jugador1["nombre"], " y el jugador 2 será ", jugador2["nombre"])
    # QUITÉ EL RETURN, YA QUE ESOS VALORES NO LOS USABAS NUNCA

def poner_establecimientos(jugador):

    def generar_objetivo(tablero, fila_o_columna, longitud, objetivo):

        def hay_espacio(tablero, fila_o_columna, filaDesde, filaHasta, columnaDesde, columnaHasta):
            if fila_o_columna == "columna":
                j = columnaDesde
                while j <= columnaHasta:
                    j += 1
                    if tablero[filaDesde][j] != "O":
                        return False
            else: 
                i = filaDesde
                while i <= filaHasta:
                    i += 1
                    if tablero[i][columnaHasta] != "O":
                        return False    
            return True 

        lon = longitud - 1

        if fila_o_columna == "columna":
            fila = random.randint(0, maxPosicion)
            columna = random.randint(0, maxPosicion - lon)

            if longitud == 6:
                ak = 0
                j = columna
                while(ak < longitud):
                    tablero[fila][j] = objetivo
                    j += 1
                    ak += 1
            else 
                ok = 0
                while (ok == 0):
                    fila = random.randint(0, maxPosicion)
                    columna = random.randint(0, maxPosicion-lon)
                    if(hay_espacio(tablero, "columna", fila, 0, columna, columna + longitud)):
                        ak = 0
                        j = columna
                        while (ak < longitud):
                            tablero[fila][j] = objetivo
                            j += 1
                            ak += 1
                            ok += 1
        else: 
            fila = random.randint(0, maxPosicion - lon)
            columna = random.randint(0, maxPosicion)

            if longitud == 6:
                ak = 0
                i = fila
                while(ak < longitud):
                    tablero[i][columna] = objetivo
                    i += 1
                    ak += 1
            else 
                ok = 0
                while (ok == 0):
                    fila = random.randint(0, maxPosicion - lon)
                    columna = random.randint(0, maxPosicion)
                    if(hay_espacio(tablero, "fila", fila, fila + longitud, columna, 0)):
                        ak = 0
                        i = fila
                        while (ak < longitud):
                            tablero[i][columna] = objetivo
                            i += 1
                            ak += 1
                            ok += 1

    tablero = jugador["mapa"]
    maxPosicion = len(tablero) - 1

    if jugador["nombre"] == "Sandokan y sus amigos":
        # OBJETIVO DE LONGITUD 6
        generar_objetivo(tablero, "fila", 6, "6"):

        # OBJETIVO DE LONGITUD 3
        generar_objetivo(tablero, "columna", 3, "3"):
        
        # PRIMER OBJETIVO DE LONGITUD 2
        generar_objetivo(tablero, "fila", 2, "2.1"):
        
        # SEGUNDO OBJETIVO DE LONGITUD 2
        generar_objetivo(tablero, "columna", 2, "2.2"):
        
        # OBJETIVO DE LONGITUD 1
        generar_objetivo(tablero, "fila", 1, "1"):
    
    else:
        generar_objetivo(tablero, "columna", 6, "6"):
        generar_objetivo(tablero, "fila", 3, "3"):
        generar_objetivo(tablero, "columna", 2, "2.1"):
        generar_objetivo(tablero, "fila", 2, "2.2"):
        generar_objetivo(tablero, "columna", 1, "1"):
    
    return tablero

def jugar(atacante, defensor):
    print("---------------------------------------------------------------------------")
    print("Ataque de ", atacante["nombre"])
    
    # EL IF QUE HABÍA ACÁ NO ES NECESARIO, YA QUE ESTA FUNCIÓN SIEMPRE VA A SER EJECUTADA CUANDO LA FLOTA
    # SEA MAYOR A 0. FIJATE QUE ESA ES TU CONDICIÓN DEL WHILE EN MAIN()

    fil = int(input("¿Qué fila desea atacar?  ")) - 1
    col = int(input("¿Qué columna atacara?  ")) - 1
    if defensor["mapa"][fil][col] != "O":
        if defensor["mapa"][fil][col] == "6":
            defensor["objetivos"][0][0] -= 1
            if defensor["objetivos"][0][0] == 0:
                print(defensor["objetivos"][0][1], " DESTRUIDO/A")

        # ACÁ REEMPLACÉ LOS IF POR ELIF, YA QUE SI DEJAS LOS IF VAS A 
        # ESTAR SIEMPRE VERIFICANDO POR TODAS LOS CARACTERES. EN CAMBIO SI
        # USAS ELIF, LA EJECUCIÓN DE ESTE BLOQUE SE TERMINA CUANDO ENCONTRAS
        # UNO DE LOS CARACTERES QUE ESTÁS BUSCANDO. 
        elif defensor["mapa"][fil][col] == "3":
            defensor["objetivos"][1][0] -= 1
            if defensor["objetivos"][1][0] == 0:
                print(defensor["objetivos"][1][1], " DESTRUIDO/A")
        elif defensor["mapa"][fil][col] == "2.1":
            defensor["objetivos"][2][0] -= 1
            if defensor["objetivos"][2][0] == 0:
                print(defensor["objetivos"][2][1], " DESTRUIDO/A")
        elif defensor["mapa"][fil][col] == "2.2":
            defensor["objetivos"][3][0] -= 1
            if defensor["objetivos"][3][0] == 0:
                print(defensor["objetivos"][3][1], " DESTRUIDO/A")
        elif defensor["mapa"][fil][col] == "1":
            defensor["objetivos"][4][0] -= 1
            if defensor["objetivos"][4][0] == 0:
                print(defensor["objetivos"][4][1], " DESTRUIDO/A")
        
        atacante["tablero"][fil][col] = "X"
        print ("IMPACTADO")
    else:
        print("Ha fallado!")
        atacante["tablero"][fil][col] = "#"

    print("Aún tiene ", objetivos_restantes(defensor), " objetivos por destruir")

    # EL RETURN QUE HABÍA ACÁ NO ES NECESARIO YA QUE NO LO USAS EN 
    # NINGUNA PARTE

# creamos el tablero
def crear_mapa(tamanio):
    tablero = []
    for i in range(tamanio):
        tablero.append([])
        for j in range(tamanio):
            tablero[i].append("O")
    return tablero

# definimos una funcion que nos muestre el tablero

def mostrar_mapa(tablero):
    abecedario = "ABCDEFGHIJKLMNOPQRST"
    for i in range(len(tablero)):
        letra = abecedario[i]
        print(f"   {(letra)}", end=" ")
    print()
    for fila in range(len(tablero)):
        print(f"{fila+1} {tablero[fila]}")

def quedan_objetivos(jugador):
    for i in range(5):
        if jugador["objetivos"][i][0] != 0:
            return True
        
    return False

def objetivos_restantes(jugador):
    objetivos = 5
    for i in range(5):
        if jugador["objetivos"][i][0] == 0:
            objetivos -= 1
    return objetivos

def main():
    print("BIENVENIDO AL JUEGO DE SANDOKAN Y SUS VALIENTES AMIGOS CONTRA LA ARMADA BRITÁNICA")
    print("LOS OBJETIVOS SERÁN COLOCADOS DE MANERA ALEATORIA. CADA BANDO TENDRÁ 5")
    print("EL TAMAÑO RECOMENDADO DE TABLERO ES 10")
    print("O ES EL AGUA, # ES EL TIRO ERRADO, X ES CUANDO SE LE PEGA AL OBJETIVO")

    print("¿QUE JUGADOR DESEA SER?")

    jugador1 = {
        "nombre": "",
        # EL MAPA CONTIENTE LA INFORMACIÖN
        "mapa": [],
        # EL TABLERO ES LO QUE SE MUESTRA EN PANTALLA AL JUGADOR
        "tablero": [],
        # OBJETIVOS REEMPLAZA LO QUE VOS HABÍAS LLAMADO 'FLOTA'. PREFIERO USAR LA PALABRA OBJETIVOS 
        # YA QUE FLOTA HACE REFERENCIA A BARCOS, PERO SANDOKAN LO QUE TIENE SON EDIFICIOS. LA PALABRA
        # OBJETIVOS PUEDE USARSE INDISTINTAMENTE, Y SINTÁCTICAMENTE ES MÁS FÁCIL PARA LEER.
        # USÉ UN ARRAY PORQUE SI TE FIJAS EN LA CONSIGNA TE DICE QUE AMBOS JUGADORES TIENEN 5 OBJETIVOS,
        # CADA UNO CON LAS MISMAS LONGITUDES DE 6, 3, 2, 2 Y 1 UNIDADES. ESTE ARRAY SE COMPONE DE DUPLAS.
        # EL PRIMER VALOR ES LA LONGITUD DEL OBJETIVO Y EL SEGUNDO ES EL NOMBRE
        "objetivos": [
            [6, ""],
            [3, ""],
            [2, ""],
            [2, ""],
            [1, ""]
        ]
    }

    jugador2 = {
        "nombre": "",
        "mapa": [],
        "tablero": [],
        "objetivos": [
            [6, ""],
            [3, ""],
            [2, ""],
            [2, ""],
            [1, ""]
        ]
    }

    eleccion= int(input("Sandokan y sus valientes amigos? presione 1 / La Armada británica? presione 2 : "))
    jugadores(eleccion, jugador1, jugador2)

    tamanio = int(input("Elija el tamaño del tablero: "))

    jugador1["mapa"] = crear_mapa(tamanio)
    jugador2["mapa"] = crear_mapa(tamanio)
    jugador1["tablero"] = crear_mapa(tamanio)
    jugador1["tablero"] = crear_mapa(tamanio)

    jugador1["mapa"] = poner_establecimientos(jugador1)
    jugador2["mapa"] = poner_establecimientos(jugador2)

    # QUITÉ LAS DECLARACIONES DE VARIABLES QUE NO SERVÍAN

    #tablero_invisible1 = mostrar_mapa(tablero_sandokan)
    #tablero_invisible2 = mostrar_mapa(tablero_armada)

    while (quedan_objetivos(jugador1) and quedan_objetivos(jugador2)):
        # COMO ESTABA ESCRITO TU CÓDIGO, DA LO MISMO QUIÉN SEA EL JUGADOR 1 PORQUE SIEMPRE ATACA PRIMERO LA ARMADA BRITÁNICA
        # LO DEJO HECHO PARA QUE EL JUGADOR 1 SEA EL QUE ATAQUE PRIMERO, ADEMÁS QUITÉ LAS VARIABLES QUE NO SE USABAN

        jugar(jugador1, jugador2)
        mostrar_mapa(jugador1["tablero"])

        jugar(jugador2, jugador1)
        mostrar_mapa(jugador2["tablero"])

main()