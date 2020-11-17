import random
print("BIENVENIDO AL JUEGO DE SANDOKAN Y SUS VALIENTES AMIGOS CONTRA LA ARMADA BRITANICA")
print("LOS ESTABLESIMIENTOS SERAN COLOCADOS DE MANERA ALEATOREA CADA VANDO TENDRA 5")
print("EL TAMAÑO RECOMENDADO DE TABLERO ES 10")
print("O ES EL AGUA, # ES EL TIRO ERRADO, X ES CUANDO SE LE PEGA AL OBJETIVO")
def jugadores(eleccion):
    if (eleccion == 1):
        jugador_1= "sadokan y sus amigos"
        jugador_2= "armada britanica"
    if (eleccion != 1):
        jugador_2= "sadokan y sus amigos"
        jugador_1= "armada britanica"
    print("el jugador n1 sera ", jugador_1, "el jugador n2 sera ", jugador_2)
    return jugador_1, jugador_2    
        
#coloca los establesimientos de sadokan
def poner_establecimientos_s(tablero):
    #Fuerte
    tablero
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
    tablero
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
    print("Ataque de la armada britanica")
    if flota_s > 0 :
        fil = int(input("¿Que fila desea atacar?  "))
        col = int(input("¿Que columna atacara?  "))
        if tablero[fil-1][col-1]!= "O":
            if tablero[fil-1][col-1] == "A":
               deposito -= 1
               if deposito == 0:
                   print("DESTRUIDO EL DEPOSITO DE ARMAS")
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
                    print("DESTRUIDO DEFENSA SUR")
                    flota_s -=1
            if tablero[fil-1][col-1] == "C":
                campamento -= 1
                if campamento == 0:
                    flota_s -= 1
                    print("DESTRUIDO EL CAMPAMENTO")
            tablero_A[fil-1][col-1] = "X"
            print ("IMPACTADO")
        else:
            print("ah fallado!")
            tablero_A[fil-1][col-1] = "#"
    print("aun tiene", flota_s, " establecimientos por hundir")
    return tablero    
#turno de sadokan
def turno_sadokan(tablero2, tablero_S, flota_a, barcaza, crucero, galeon, galera, cañonero):
    print("---------------------------------------------------------------------------")
    print("Ataque de Sadokan")
    if flota_a > 0 :
        fil = int(input("¿Que fila desea atacar?  "))
        col = int(input("¿Que columna atacara?  "))
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
                    print("DESTRUIDO EL GALEON")
            tablero_S[fil-1][col-1] = "X"
            print ("IMPACTADO")
        else:
            print("ah fallado!")
            tablero_S[fil-1][col-1] = "#"

    print("aun tiene", flota_a, " establecimientos por hundir")
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
    print("¿QUE JUGADOR DESEA SER?")
    eleccion= int(input("sadokan y sus valientes amigos precione 1 0 la armada britanica precione 2  "))
    jugadores(eleccion)
    tamanio = int(input("elija el tamaño del tablero: "))
    #tablero donde tengo los barcos de sadokan:
    tablero = crear_mapa(tamanio)
    #tablero donde tengo los barcos de la armada:
    tablero2 = crear_mapa(tamanio)
    #tablero que vera la armada
    tablero_A= crear_mapa(tamanio)
    #tablero que vera sadokan
    tablero_S = crear_mapa(tamanio)
    tablero_visible = mostrar_mapa(tablero)
    tablero_sadokan= poner_establecimientos_s(tablero)
    tablero_armada= poner_establecimientos_a(tablero2)
    #tablero_invisible1 = mostrar_mapa(tablero_sadokan)
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
        ataque_a= turno_armada(tablero, tablero_A, campamento, flota_s, defensaS, fuerte, deposito, defensaN)
        tablero_visible_para_la_armada = mostrar_mapa(tablero_A)
        ataque_s= turno_sadokan(tablero2, tablero_S, flota_a, barcaza, crucero, galeon, galera, cañonero)
        tablero_visible_para_sadokan = mostrar_mapa(tablero_S)
main()