import random

# QUITÉ ESTAS PRIMERAS LÍNEAS Y LAS PUSE DENTRO DEL MAIN, YA QUE AHÍ ES DONDE VERDADERAMENTE COMIENZA
# LA EJECUCIÓN DE TU PROGRAMA. ESTE ESPACIO DE ACÁ ARRIBA EN LÍNEAS GENERALES SOLO SE USA PARA
# IMPORTAR MÓDULOS Y DECLARAR FUNCIONES

def jugadores(eleccion):
    if (eleccion == 1):
        jugador_1= "Sandokan y sus amigos"
        jugador_2= "Armada británica"
    if (eleccion != 1):
        jugador_1= "Armada británica"
        jugador_2= "Sandokan y sus amigos"
    print("El jugador 1 será ", jugador_1, " y el jugador 2 será ", jugador_2)
    # QUITÉ EL RETURN, YA QUE ESOS VALORES NO LOS USABAS NUNCA

#coloca los establesimientos de sandokan
def poner_establecimientos_s(tablero):
    #Fuerte
    fuerte = 6
    maxPosicion = len(tablero) - 1
    filaAleatoria = random.randint(0, maxPosicion)
    columnaInicial = random.randint(0, maxPosicion-5)
    ak = 0
    j = columnaInicial
    while(ak < fuerte):
        tablero[filaAleatoria][j] = "F"
        j += 1
        ak += 1

    #Campamento de defensa, 3 celdas verticales
    campamento = 3
    maxPosicion =  len(tablero) - 1
    ok = 0
    while ok == 0:
        filaAleatoria = random.randint(0, maxPosicion-3)
        columnaInicial = random.randint(0, maxPosicion)
        if tablero[filaAleatoria][columnaInicial] == "O" and tablero[filaAleatoria + 1][columnaInicial] == "O" and tablero[filaAleatoria + 2][columnaInicial] == "O":
            ak = 0
            i = filaAleatoria
            while (ak < campamento):
                tablero[i][columnaInicial] = "C"
                i += 1
                ak += 1
                ok += 1

    #Depósito de armas, 2 celdas horizontales. 
    deposito= 2
    maxp = len(tablero) - 1
    ok = 0
    while (ok == 0):
        filA = random.randint(0, maxp)
        colA = random.randint(0, maxp-1)
        if(tablero[filA][colA] == "O") and (tablero[filA][colA + 1] == "O"):
            ak = 0
            j = colA
            while (ak < deposito):
                tablero[filA][j] = "A"
                j += 1
                ak += 1
                ok += 1
    
    #Defensa Norte, 2 celda verticales
    defensaN= 2
    maxp = len(tablero) - 1
    ok = 0
    while (ok == 0):
        filA = random.randint(0, maxp-1)
        colA = random.randint(0, maxp)
        if(tablero[filA][colA] == "O" and tablero[filA+1][colA] == "O"):
            ak = 0
            i = filA
            while (ak < defensaN):
                tablero[i][filA] = "N"
                i += 1
                ak += 1
                ok += 1
    
    # Defensa Sur, 1 celda
    defensaS= 1
    maxp = len(tablero) - 1
    ok = 0
    while (ok == 0):
        filA = random.randint(0, maxp)
        colA = random.randint(0, maxp)
        if(tablero[filA][colA] == "O"):
            ak = 0
            i = filA
            while (ak < defensaS):
                tablero[i][filA] = "S"
                i += 1
                ak += 1
                ok += 1
    
    return tablero

#coloca los establesimientos de la armada britanica
def poner_establecimientos_a(tablero):
    #Crucero pesado, 6 celdas verticales
    crucero = 6
    maxPosicion = len(tablero) - 1
    filaAleatoria = random.randint(0, maxPosicion-5)
    columnaInicial = random.randint(0, maxPosicion)
    ak = 0
    i = filaAleatoria
    while(ak < crucero):
        tablero[i][columnaInicial] = "P"
        i += 1
        ak += 1

    #Galeón, 3 celdas horizontal 
    galeon = 3
    maxPosicion =  len(tablero) - 1
    ok = 0
    while ok == 0:
        filaAleatoria = random.randint(0, maxPosicion)
        columnaInicial = random.randint(0, maxPosicion-2)
        if tablero[filaAleatoria][columnaInicial] == "O" and tablero[filaAleatoria][columnaInicial + 1] == "O" and tablero[filaAleatoria][columnaInicial + 2] == "O":
            ak = 0
            j = columnaInicial
            while (ak < galeon):
                tablero[filaAleatoria][j] = "G"
                j += 1
                ak += 1
                ok += 1
    
    #Galera, 2 celdas horizontales 
    galera= 2
    maxp = len(tablero) - 1
    ok = 0
    while (ok == 0):
        filA = random.randint(0, maxp)
        colA = random.randint(0, maxp-1)
        if(tablero[filA][colA] == "O") and (tablero[filA][colA + 1] == "O"):
            ak = 0
            j = colA
            while (ak < galera):
                tablero[filA][j] = "A"
                j += 1
                ak += 1
                ok += 1
    
    # Cañonero, 2 celdas verticales 
    cañonero= 2
    maxp = len(tablero) - 1
    ok = 0
    while (ok == 0):
        filA = random.randint(0, maxp-1)
        colA = random.randint(0, maxp)
        if(tablero[filA][colA] == "O" and tablero[filA+1][colA] == "O"):
            ak = 0
            i = filA
            while (ak < cañonero):
                tablero[i][filA] = "C"
                i += 1
                ak += 1
                ok += 1
    # Barcaza, 1 celda
    barcaza= 1
    maxp = len(tablero) - 1
    ok = 0
    while (ok == 0):
        filA = random.randint(0, maxp)
        colA = random.randint(0, maxp)
        if(tablero[filA][colA] == "O"):
            ak = 0
            i = filA
            while (ak < barcaza):
                tablero[i][filA] = "B"
                i += 1
                ak += 1
                ok += 1
    
    return tablero

#funcion para hundir establecimientos
def turno_armada(tablero, tablero_A, campamento, flota_s, defensaS, fuerte, deposito, defensaN):
    print("---------------------------------------------------------------------------")
    print("Ataque de la Armada británica")
    if flota_s > 0 :
        fil = int(input("¿Qué fila desea atacar?  "))
        col = int(input("¿Qué columna atacará?  "))
        if tablero[fil-1][col-1]!= "O":
            if tablero[fil-1][col-1] == "A":
                deposito -= 1
                if deposito == 0:
                    print("DESTRUIDO EL DEPÓSITO DE ARMAS")
                    flota_s -= 1
            if tablero[fil-1][col-1] == "F":
                fuerte -= 1
                if fuerte == 0:
                    print("DESTRUIDO EL FUERTE")
                    flota_s -= 1
            if tablero[fil-1][col-1] == "N":
                defensaN -= 1
                if defensaN == 0:
                    print("DESTRUIDA LA DEFENSA NORTE")
                    flota_s -= 1
            if tablero[fil-1][col-1] == "S":
                defensaS -= 1
                if defensaS == 0:
                    print("DESTRUIDA LA DEFENSA SUR")
                    flota_s -=1
            if tablero[fil-1][col-1] == "C":
                campamento -= 1
                if campamento == 0:
                    flota_s -= 1
                    print("DESTRUIDO EL CAMPAMENTO")
            tablero_A[fil-1][col-1] = "X"
            print ("IMPACTADO")
        else:
            print("Ha fallado!")
            tablero_A[fil-1][col-1] = "#"
    print("Aún tiene ", flota_s, " establecimientos por hundir")
    return tablero   

#turno de sandokan
def turno_sandokan(tablero2, tablero_S, flota_a, barcaza, crucero, galeon, galera, cañonero):
    print("---------------------------------------------------------------------------")
    print("Ataque de Sandokan")
    if flota_a > 0 :
        fil = int(input("¿Qué fila desea atacar?  "))
        col = int(input("¿Qué columna atacara?  "))
        if tablero2[fil-1][col-1]!= "O":
            if tablero2[fil-1][col-1] == "A":
                galera -= 1
                if galera == 0:
                    print("DESTRUIDO LA GALERA")
                    flota_a -= 1
            if tablero2[fil-1][col-1] == "P":
                crucero -= 1
                if crucero == 0:
                    print("DESTRUIDO EL CRUCERO PESADO")
                    flota_a -= 1
            if tablero2[fil-1][col-1] == "C":
                cañonero -= 1
                if cañonero == 0:
                    print("DESTRUIDO EL CAÑONERO")
                    flota_a -= 1
            if tablero2[fil-1][col-1] == "B":
                barcaza -= 1
                if barcaza == 0:
                    print("DESTRUIDO LA BALCARZA")
                    flota_a -=1
            if tablero2[fil-1][col-1] == "G":
                galeon -= 1
                if galeon == 0:
                    flota_a -= 1
                    print("DESTRUIDO EL GALEÓN")
            tablero_S[fil-1][col-1] = "X"
            print ("IMPACTADO")
        else:
            print("Ha fallado!")
            tablero_S[fil-1][col-1] = "#"

    print("Aún tiene ", flota_a, " establecimientos por hundir")
    return tablero2 

# creamos el tablero
def crear_mapa(tamanio):
    tablero = []
    for i in range(tamanio):
        fila = []
        tablero.append(fila)
        for j in range(tamanio):
            fila.append("O")
    return  tablero

# definimos una funcion que nos muestre el tablero

def mostrar_mapa(tablero):
    abecedario = "ABCDEFGHIJKLMNOPQRST"
    for i in range(len(tablero)):
        letra = abecedario[i]
        print(f"   {(letra)}", end=" ")
    print()
    for fila in range(len(tablero)):
        print(f"{fila+1} {tablero[fila]}")

def main():
    print("BIENVENIDO AL JUEGO DE SANDOKAN Y SUS VALIENTES AMIGOS CONTRA LA ARMADA BRITÁNICA")
    print("LOS OBJETIVOS SERÁN COLOCADOS DE MANERA ALEATORIA. CADA BANDO TENDRÁ 5")
    print("EL TAMAÑO RECOMENDADO DE TABLERO ES 10")
    print("O ES EL AGUA, # ES EL TIRO ERRADO, X ES CUANDO SE LE PEGA AL OBJETIVO")

    print("¿QUE JUGADOR DESEA SER?")
    eleccion= int(input("Sandokan y sus valientes amigos? presione 1 / La Armada británica? presione 2 : "))
    jugadores(eleccion)

    tamanio = int(input("Elija el tamaño del tablero: "))

    #tablero donde tengo los barcos de sandokan:
    tablero = crear_mapa(tamanio)
    #tablero donde tengo los barcos de la armada:
    tablero2 = crear_mapa(tamanio)
    #tablero que vera la armada
    tablero_A= crear_mapa(tamanio)
    #tablero que vera sandokan
    tablero_S = crear_mapa(tamanio)

    # QUITÉ LAS DECLARACIONES DE VARIABLES QUE NO SERVÍAN
    mostrar_mapa(tablero)
    poner_establecimientos_s(tablero)
    poner_establecimientos_a(tablero2)

    #tablero_invisible1 = mostrar_mapa(tablero_sandokan)
    #tablero_invisible2 = mostrar_mapa(tablero_armada)

    flota_a = 5
    flota_s = 5
    defensaS = 1
    fuerte = 6 
    deposito= 2
    defensaN= 2
    campamento = 3
    barcaza = 1
    crucero = 6
    galeon = 3
    galera= 2
    cañonero= 2
    while (flota_a != 0 or flota_s != 0):
        # CÓMO ESTABA ESCRITO TU CÓDIGO, DA LO MISMO QUIÉN SEA EL JUGADOR 1 PORQUE SIEMPRE ATACA PRIMERO LA ARMADA BRITÁNICA
        # LO DEJO HECHO PARA QUE EL JUGADOR 1 SEA EL QUE ATAQUE PRIMERO, ADEMÁS QUITÉ LAS VARIABLES QUE NO SE USABAN


        turno_armada(tablero, tablero_A, campamento, flota_s, defensaS, fuerte, deposito, defensaN)
        mostrar_mapa(tablero_A)

        turno_sandokan(tablero2, tablero_S, flota_a, barcaza, crucero, galeon, galera, cañonero)
        mostrar_mapa(tablero_S)
main()