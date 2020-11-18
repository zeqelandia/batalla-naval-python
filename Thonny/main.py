import random

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

def poner_establecimientos(jugador):

    def generar_objetivo(tablero, fila_o_columna, longitud, objetivo):

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

        lon = longitud - 1

        if fila_o_columna == "fila":
            ok = 0
            while (ok == 0):
                fila = random.randint(0, maxPosicion)
                columna = random.randint(0, maxPosicion-lon)
                if(hay_espacio(tablero, "fila", fila, 0, columna, columna + lon)):
                    ak = 0
                    j = columna
                    while (ak < longitud):
                        tablero[fila][j] = objetivo
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
                        tablero[i][columna] = objetivo
                        i += 1
                        ak += 1
                        ok += 1

    tablero = jugador["mapa"]
    maxPosicion = len(tablero) - 1

    if jugador["nombre"] == "Sandokan y sus amigos":
        generar_objetivo(tablero, "fila", 6, "6")
        generar_objetivo(tablero, "columna", 3, "3")
        generar_objetivo(tablero, "fila", 2, "2")
        generar_objetivo(tablero, "columna", 2, "7")
        generar_objetivo(tablero, "fila", 1, "1")  
    else:
        generar_objetivo(tablero, "columna", 6, "6")
        generar_objetivo(tablero, "fila", 3, "3")
        generar_objetivo(tablero, "columna", 2, "2")
        generar_objetivo(tablero, "fila", 2, "7")
        generar_objetivo(tablero, "columna", 1, "1")
    
    return tablero

def jugar(atacante, defensor):
    print("---------------------------------------------------------------------------")
    print("Ataque de ", atacante["nombre"])

    fil = int(input("¿Qué fila desea atacar?  ")) - 1
    col = int(input("¿Qué columna atacara?  ")) - 1
 
    if defensor["mapa"][fil][col] != "O":
        if defensor["mapa"][fil][col] == "6":
            defensor["objetivos"][0][0] -= 1
            if defensor["objetivos"][0][0] == 0:
                print(defensor["objetivos"][0][1], " DESTRUIDO/A")
        elif defensor["mapa"][fil][col] == "3":
            defensor["objetivos"][1][0] -= 1
            if defensor["objetivos"][1][0] == 0:
                print(defensor["objetivos"][1][1], " DESTRUIDO/A")
        elif defensor["mapa"][fil][col] == "2":
            defensor["objetivos"][2][0] -= 1
            if defensor["objetivos"][2][0] == 0:
                print(defensor["objetivos"][2][1], " DESTRUIDO/A")
        elif defensor["mapa"][fil][col] == "7":
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

# Creamos el tablero
def crear_mapa(tamanio):
    tablero = []
    for i in range(tamanio):
        tablero.append([])
        j = 0
        while j < tamanio:
            tablero[i].append("O")
            j += 1
    return tablero

# Definimos una funcion que nos muestre el tablero
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
        "mapa": [],
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
    jugador2["tablero"] = crear_mapa(tamanio)

    jugador1["mapa"] = poner_establecimientos(jugador1)
    jugador2["mapa"] = poner_establecimientos(jugador2)



    while (quedan_objetivos(jugador1) and quedan_objetivos(jugador2)):
        
        jugar(jugador1, jugador2)
        mostrar_mapa(jugador1["tablero"])

        if not quedan_objetivos(jugador2):
            break

        jugar(jugador2, jugador1)
        mostrar_mapa(jugador2["tablero"])
    
    if quedan_objetivos(jugador1):
        print("Ganó el Jugador 1: ", jugador1["nombre"])
    else:
        print("Ganó el Jugador 2: ", jugador2["nombre"])

main()