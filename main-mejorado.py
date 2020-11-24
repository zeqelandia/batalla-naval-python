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

def hay_espacio(tablero, fila_o_columna, filaDesde, filaHasta, columnaDesde, columnaHasta):
    if fila_o_columna == "fila":
        j = columnaDesde
        while j <= columnaHasta:
            #print(j, " ", filaDesde)
            if tablero[filaDesde][j] != "O":
                return False
            j += 1
    else: 
        i = filaDesde
        while i <= filaHasta:
            #print(i, " ", columnaHasta)
            if tablero[i][columnaDesde] != "O":
                return False
            i += 1
    return True

def generar_objetivo(jugador, fila_o_columna, longitud, indice_de_objetivo): 
    tablero = jugador["mapa"]
    caracter = "D"
    maxPosicion = len(tablero) - 1
    lon = longitud - 1
    fila = 0
    columna = 0
    filas = []
    columnas = []

    if fila_o_columna == "fila":
        ok = 0
        while (ok == 0):
            fila = random.randint(0, maxPosicion)
            columna = random.randint(0, maxPosicion-lon)
            if(hay_espacio(tablero, "fila", fila, 0, columna, columna + lon)):
                ak = 0
                j = columna
                while (ak < longitud):
                    tablero[fila][j] = caracter
                    filas.append(fila)
                    columnas.append(j)
                    j += 1
                    ak += 1
                    ok += 1 
    else: 
        ok = 0
        while (ok == 0):
            fila = random.randint(0, maxPosicion - lon)
            columna = random.randint(0, maxPosicion)
            if(hay_espacio(tablero, "columna", fila, fila + lon, columna, 0)):
                ak = 0
                i = fila
                while (ak < longitud):
                    tablero[i][columna] = caracter
                    filas.append(i)
                    columnas.append(columna)
                    i += 1
                    ak += 1
                    ok += 1

    # SE AGREGA LA UBICACION DE CADA CELDA QUE COMPONE EL OBJETIVO ACTUAL AL ARREGLO "UBICACIONES"
    # DEL JUGADOR
    for i in range(jugador["objetivos"][indice_de_objetivo][0]):
        ubicacion_del_objetivo = [filas[i], columnas[i]]
        jugador["ubicaciones"][indice_de_objetivo].append(ubicacion_del_objetivo)

def poner_establecimientos(jugador): 
    if jugador["nombre"] == "Sandokan y sus amigos":
        # OBJETIVO DE LONGITUD 6
        generar_objetivo(jugador, "fila", 6, 0)

        # OBJETIVO DE LONGITUD 3
        generar_objetivo(jugador, "columna", 3, 1)
        
        # PRIMER OBJETIVO DE LONGITUD 2
        generar_objetivo(jugador, "fila", 2, 2)
        
        # SEGUNDO OBJETIVO DE LONGITUD 2 
        generar_objetivo(jugador, "columna", 2, 3)
        
        # OBJETIVO DE LONGITUD 1
        generar_objetivo(jugador, "fila", 1, 4)
    
    else:
        generar_objetivo(jugador, "columna", 6, 0)
        generar_objetivo(jugador, "fila", 3, 1)
        generar_objetivo(jugador, "columna", 2, 2)
        generar_objetivo(jugador, "fila", 2, 3)
        generar_objetivo(jugador, "columna", 1, 4)
    
    return jugador["mapa"]

def jugar(atacante, defensor):
    print("---------------------------------------------------------------------------")
    print("Ataque de ", atacante["nombre"])
    print()

    impacto = False
    ubicaciones = defensor["ubicaciones"]
    fil = int(input("¿Qué fila desea atacar?  ")) - 1
    col = int(input("¿Qué columna atacara?  ")) - 1
    print()

    for i in range(len(ubicaciones)):
        for j in range(len(ubicaciones[i])):
            fila_de_ubicacion = ubicaciones[i][j][0]
            columna_de_ubicacion = ubicaciones[i][j][1]

            if fil == fila_de_ubicacion and col == columna_de_ubicacion:
                if (atacante["tablero"][fil][col] != "X") and (atacante["tablero"][fil][col] != "#"):
                    impacto = True
                    atacante["tablero"][fil][col] = "X"
                    defensor["objetivos"][i][0] -= 1
                    print("IMPACTADO")
                    if defensor["objetivos"][i][0] == 0:
                        print(defensor["objetivos"][i][1], " DESTRUIDO/A")
                    print("Aún tiene ", objetivos_restantes(defensor), " objetivos por destruir")
                    print()
    
    if not impacto:
        atacante["tablero"][fil][col] = "#"
        print("Ha fallado")
        print("Aún tiene ", objetivos_restantes(defensor), " objetivos por destruir")
        print()


# creamos el tablero
def crear_mapa(tamanio):
    tablero = []
    for i in range(tamanio):
        tablero.append([])
        j = 0
        while j < tamanio:
            tablero[i].append("O")
            j += 1
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
    for i in range(len(jugador["objetivos"])):
        if jugador["objetivos"][i][0] != 0:
            return True
        
    return False

def objetivos_restantes(jugador):
    objetivos = len(jugador["objetivos"])
    for i in range(objetivos):
        if jugador["objetivos"][i][0] == 0:
            objetivos -= 1
    return objetivos

def encontrarMenorObjetivo(jugador):
    menorObjetivo = 6
    menorIndice = len(jugador["objetivos"]) - 1
    for i in range(len(jugador["objetivos"])):
        if jugador["objetivos"][i][0] < menorObjetivo:
            menorObjetivo = jugador["objetivos"][i][0]
            menorIndice = i 
    return menorIndice

def actualizarMapa(jugador, objetivo):
    ubicaciones = jugador["ubicaciones"][objetivo]
    for i in range(len(ubicaciones)):
        fila = ubicaciones[i][0]
        columna = ubicaciones[i][1]
        jugador["mapa"][fila][columna] = "O"

def ganarDefensa(atacante, defensor, probabilidad):
    rand = random.randint(0, 101)

    if rand < probabilidad:
        # ENCONTRAR EL MENOR OBJETIVO DEL DEFENSOR
        menorObjetivo = encontrarMenorObjetivo(defensor)
        
        # AGREGAR ESE OBJETIVO AL ATACANTE. HAGO EL IF PARA VER SI AL ATACANTE LE AGREGO UNA FILA O UNA COLUMNA
        # LO CUAL ES MERAMENTE PARA DARLE VARIEDAD AL JUEGO
        atacante["objetivos"].append(defensor["objetivos"][menorObjetivo])
        atacante["ubicaciones"].append([])
        indice = len(atacante["objetivos"]) - 1

        if atacante["nombre"] == "Sandokan y sus amigos":
            generar_objetivo(atacante, "fila", defensor["objetivos"][menorObjetivo][0], indice)
        else:
            generar_objetivo(atacante, "columna", defensor["objetivos"][menorObjetivo][0], indice)
        
        # INFORMAR AL JUGADOR
        print("El jugador ", atacante["nombre"], " ha tomado posesión de el/la ", defensor["objetivos"][menorObjetivo][1], "que pertenecía a ", defensor["nombre"])
        
        # QUITARLE EL MENOR OBJETIVO AL DEFENSOR
        actualizarMapa(defensor, menorObjetivo)
        defensor["objetivos"].pop(menorObjetivo)
        defensor["ubicaciones"].pop(menorObjetivo)

def main():
    print("BIENVENIDO AL JUEGO DE SANDOKAN Y SUS VALIENTES AMIGOS CONTRA LA ARMADA BRITÁNICA")
    print("LOS OBJETIVOS SERÁN COLOCADOS DE MANERA ALEATORIA. CADA BANDO TENDRÁ 5")
    print("EL TAMAÑO RECOMENDADO DE TABLERO ES 10")
    print("O ES EL AGUA, # ES EL TIRO ERRADO, X ES CUANDO SE LE PEGA AL OBJETIVO")
    print()
    print("¿QUE JUGADOR DESEA SER?")
    print()

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
        ],
        # UBICACIONES ES UN ARRAY DE ARRAYS QUE CONTIENEN LA FILA Y COLUMNA DONDE SE ENCUENTRA CADA OBJETIVO DENTRO
        # DEL MAPA
        "ubicaciones": [
            [], [], [], [], []
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
        ],
        "ubicaciones": [
            [], [], [], [], []
        ]
    }

    eleccion= int(input("Sandokan y sus valientes amigos? presione 1 / La Armada británica? presione 2 : "))
    jugadores(eleccion, jugador1, jugador2)
    print()

    tamanio = int(input("Elija el tamaño del tablero: "))
    print()

    jugador1["mapa"] = crear_mapa(tamanio)
    jugador2["mapa"] = crear_mapa(tamanio)
    jugador1["tablero"] = crear_mapa(tamanio)
    jugador2["tablero"] = crear_mapa(tamanio)

    jugador1["mapa"] = poner_establecimientos(jugador1)
    jugador2["mapa"] = poner_establecimientos(jugador2)

    # QUITÉ LAS DECLARACIONES DE VARIABLES QUE NO SERVÍAN

    #tablero_invisible1 = mostrar_mapa(tablero_sandokan)
    #tablero_invisible2 = mostrar_mapa(tablero_armada)

    probabilidad = int(input("Cuál será la probabilidad de ganar una defensa del adversario? (0 - 99): "))
    print()

    while quedan_objetivos(jugador1) and quedan_objetivos(jugador2):
        # COMO ESTABA ESCRITO TU CÓDIGO, DA LO MISMO QUIÉN SEA EL JUGADOR 1 PORQUE SIEMPRE ATACA PRIMERO LA ARMADA BRITÁNICA
        # LO DEJO HECHO PARA QUE EL JUGADOR 1 SEA EL QUE ATAQUE PRIMERO, ADEMÁS QUITÉ LAS VARIABLES QUE NO SE USABAN

        mostrar_mapa(jugador1["tablero"])
        jugar(jugador1, jugador2)
        print()
        ganarDefensa(jugador1, jugador2, probabilidad)
        print()

        if quedan_objetivos(jugador2):
            mostrar_mapa(jugador2["tablero"])
            jugar(jugador2, jugador1)
            print()
            ganarDefensa(jugador2, jugador1, probabilidad)
            print()

    if quedan_objetivos(jugador1):
        print("Ganó el Jugador 1: ", jugador1["nombre"])
    else:
        print("Ganó el Jugador 2: ", jugador2["nombre"])

main()
