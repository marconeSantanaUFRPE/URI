# -*- coding: utf-8 -*-

#Distancia entre dois pontos
from math import sqrt
def distanciaEclidiana(x1,y1,x2,y2):

    distancia = sqrt((x1 - x2)**2 + (y1-y2)**2)

    return  distancia


while True:
    try:
        r1,x1,y1,r2,x2,y2 = [int(x) for x in input().split()]

        distancia = distanciaEclidiana(x1,y1,x2,y2)

        if distancia+r2<= r1:
            print("RICO")
        else:
            print("MORTO")


    except EOFError:
        break
