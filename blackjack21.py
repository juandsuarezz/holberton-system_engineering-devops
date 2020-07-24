#!/usr/bin/python3

import os
import random

partidas = 0
juego = 0
tokens = 1000
play = 1

print("\nBlackJack21")

while(play == 1):

    if tokens == 0:
        print("\n---YA NO TIENES MONEDAS---")
        break

    print("\nTienes ${:d} monedas".format(tokens))
    apuesta = int(input("Cuantas monedas quieres apostar?\n\n$"))

    if apuesta > tokens:
        print("\n---NO TIENES MONEDAS SUFICIENTES---")
    if apuesta <= tokens:
        tokens = tokens - apuesta
        print("\nTe quedan ${:d} monedas".format(tokens))
        jugar = int(input("Enter 1 -> Comenzar | Enter 2 -> Apostar otro valor\n\n"))

        if jugar != 1:
            tokens = tokens + apuesta

        if jugar == 1:

            juego = 0
            mesa = []
            total = 0
            count = 0

            while(total <= 21 and juego == 0):

                cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "AS"] * 4

                for i in range(2):
                    random.shuffle(cartas)
                    carta = cartas.pop()
                    mesa.append(carta)

                while (count < 2):

                    if mesa[count] == "J" or mesa[count] == "Q" or mesa[count] == "K":
                        total = total + 10
                    elif mesa[count] == "AS":
                        if total >= 11:
                            total = total + 1
                        else:
                            total = total + 11
                    else:
                        total = total + mesa[count]
                    count = count + 1

                print("\n===========================================")

                print("\nTus Cartas: {} = {:d}".format(mesa, total))

                count = count + 1

                if total < 21:
                    juego = int(input("\nEnter 1 -> Tomar carta | Enter 2 -> Quedarse | "))
                else:
                    juego = 2


            count = 2

            while(total <= 21 and juego == 1):

                cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "AS"] * 4

                random.shuffle(cartas)
                carta = cartas.pop()
                mesa.append(carta)

                if mesa[count] == "J" or mesa[count] == "Q" or mesa[count] == "K":
                        total = total + 10
                elif mesa[count] == "AS":
                    if total >= 11:
                        total = total + 1
                    else:
                        total = total + 11
                else:
                    total = total + mesa[count]

                print("\nTus Cartas: {} = {:d}".format(mesa, total))

                count = count + 1
                if total < 21:
                    juego = int(input("\nEnter 1 -> Tomar carta | Enter 2 -> Quedarse | "))
                else:
                    juego = 2

            mesa2 = []
            total2 = 0
            count = 0

            while(total2 <= 21 and juego == 2):

                cartas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "AS"] * 4

                random.shuffle(cartas)
                carta = cartas.pop()
                mesa2.append(carta)

                if mesa2[count] == "J" or mesa2[count] == "Q" or mesa2[count] == "K":
                        total2 = total2 + 10
                elif mesa2[count] == "AS":
                    if total2 >= 11:
                        total2 = total2 + 1
                    else:
                        total2 = total2 + 11
                else:
                    total2 = total2 + mesa2[count]

                if total2 >= 17:
                    print("\nCartas del Dealer: {} = {:d}".format(mesa2, total2))
                    
                    juego = 3

                else:
                    count = count + 1


    while (juego == 3):

        if total == total2:
            print("\nEMPATE!")
            juego = 4
            tokens = tokens + apuesta
    
        elif total > 21 and total2 > 21:
            print("\nEMPATE!")
            juego = 4
            tokens = tokens + apuesta

        elif total <= 21 and total2 > 21:
            print("\nGANASTE!")
            juego = 4
            tokens = tokens + (apuesta * 2)

        elif total <= 21 and total2 <= 21:
            if total > total2:
                print("\nGANASTE!")
                juego = 4
                tokens = tokens + apuesta * 2
            else:
                print("\nPERDISTE!")
                juego = 4

        elif total > 21 and total2 <= 21:
            print("\nPERDISTE!")
            juego = 4


        if total == 21 and total2 != 21 and len(mesa) == 2:
            print("---Felicidades, has hecho un BlackJack21---")

        elif total != 21 and total2 == 21 and len(mesa2) == 2:
            print("---El Dealer ha hecho un BlackJack21---")

        elif total == 21 and total2 == 21 and len(mesa) == 2 and len(mesa2) == 2:
            print("---WOW!!! El Dealer y tú, hicisteís BlackJack21!!!---")

        print("\n===========================================")

        partidas = partidas + 1

        if tokens == 0:
            break

        play = int(input("\nQuieres jugar de nuevo??\nEnter 1 -> (SI) | Enter 2 -> (NO)\n\n"))


while (juego == 4):

    print("\nMonedas totales = ${}".format(tokens))
    print("Partidas jugadas: {}".format(partidas))
    print("Gracias por jugar! :D\n")

    juego = 5
