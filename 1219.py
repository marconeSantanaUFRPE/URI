
#triangulos e circulos

from math import sqrt

def areaCirculo(raio):
    
    pi = 3.1415926535897
    area = (raio*raio)*pi
    
    return area
    
while True:
    
    try:

        a,b,c = [int(x) for x in input().split()]
        
        
        halfperimetro = (a+b+c)/2
        
        areaTriagulo =  sqrt(halfperimetro*( halfperimetro - a )*( halfperimetro - b )*( halfperimetro - c))
        
        raioCirculoG =   (a*b*c) /  (sqrt((a+b+c)*(a+b-c)*(a+c-b)*(b+c-a) ))
        
        #print(raioCirculoG)
        
        raioCirculoP = areaTriagulo/halfperimetro
        
        areaCG = areaCirculo(raioCirculoG)
        areaCP = areaCirculo(raioCirculoP)
        
        #print(areaTriagulo)
        
        
        print("%.4f %.4f %.4f" % ((areaCG - areaTriagulo),(areaTriagulo - areaCP),(areaCP)))
    except EOFError:
        break
        