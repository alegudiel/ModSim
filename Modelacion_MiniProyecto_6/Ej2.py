from cProfile import label
import random
import matplotlib.pyplot as plt
import numpy as np

def instrucciones():
    print("""
    \n------------------------------
    \nBienvenido al juego de la caja
    \n------------------------------
    1. Los tokens están numerados de 1 a 100 en la caja
    2. Los jugadores pueden apostar por un número par o impar que saldrá al tomar el tokenGame de la caja
    3. En este juego, 10 y 11 son números especiales. 
        Si se apuesta por un número par, entonces 10 será considerado un número impar; 
        si se apuesta por un número impar, entonces 11 será considerado como un número par.
    4. Si se apuesta por un número par y se obtiene 10 entonces se pierde.
    5. Si se apuesta por un número impar y se obtiene 11 entonces se pierde
    """)

def mainGame():

    optUser = 0
    menu = False

    while menu != True:
        print("""
        \n¡Bienvenido! \n¿Qué desea hacer?
            1. Jugar
            2. Instrucciones del juego
            3. Salir
        """)
        optUser = int(input("Ingrese una opción: "))
        if optUser == 1:
            cantGames = int(input("\nIngrese la cantidad de veces que desea jugar: "))

            money = 0
            for game in range(cantGames):
                bet = int(input("Ingrese la apuesta $" ))
                bettingTo = int(input("¿Qué desea apostar? \n1) Par \n2) Impar \nSu opción: "))
                print("\n\nEl juego ha comenzado...")
                tokenGame = random.randint(1, 100)
                print("El número que salió para esta ronda es: ", tokenGame, "\n")

                if bettingTo == 1:
                    if((tokenGame %2 == 0 or tokenGame == 11 and tokenGame != 10)):
                        money += bet
                        print("Ganaste! Dinero actual $", money)
                    else:
                        money -= bet
                        print("Perdiste! Dinero actual $", money)

                elif bettingTo == 2:
                    if((tokenGame %2 != 1 or tokenGame == 10 and tokenGame != 11)):
                        money += bet
                        print("Ganaste! Dinero actual $", money)
                    else:
                        money -= bet
                        print("Perdiste! Dinero actual $", money)

            print("El dinero que tienes es de $", money)
            print("Partidas jugadas: ", cantGames)

        elif optUser == 2:
            instrucciones()

        elif optUser == 3:
            print("Gracias por jugar!")
            break


def simGame():
    # ------> Simulación usando
    # 50 juegos, con 10 iteraciones
    # 50 juegos, con 1,000 iteraciones
    # 10,000 juegos, con 10 iteraciones

    cantGames = 10000
    cantIter = 10
    resultados = []
    money = 0
    bet = 1000

    for game in range(cantGames):
        # xVal = list(range(1, cantIter+1))
        for iter in range(cantIter):
            number = random.randint(0, 1)
            tokenGame = random.randint(1, 100)
            if(number == 0):
                if((tokenGame %2 == 0 or tokenGame == 11 and tokenGame != 10)):
                    money += bet
                else:
                    money -= bet
            elif(number == 1):
                if((tokenGame %2 != 1 or tokenGame == 10 and tokenGame != 11)):
                    money += bet
                else:
                    money -= bet
        resultados.append(money)

    # print("El dinero que tienes es de $", money)
    # print("Partidas jugadas: ", cantGames)
    
    plt.plot(list(range(cantGames)) ,resultados, label="10000 juegos, 10 iteraciones")
    plt.xlabel("Cantidad de juegos")
    plt.ylabel("Dinero de cada juego")
    plt.legend()
    plt.show()

# mainGame()
simGame()
