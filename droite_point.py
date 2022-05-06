#coding:utf-8
#By CT-7568

def signe(n):
    if n < 0:
        if n == -1:
            return "-"
        else:
            return n
    elif n > 0:
        if n == 1:
            return ""
        else:
            n="+" + str(n)
            return n
    else:
        return ""

def equation_cartesienne(xV, yV, xI, yI):
    nature_vecteur= int(input("Vecteur normal (0)\nVecteur directeur (1)\nRéponse : "))
    if nature_vecteur == 0:
        a=xV
        b=yV
        c=-a*xI-b*yI
        a=signe(a)
        b=signe(b)
        c=signe(c)
        return (print("Equation:", a,"x", b,"y", c,"= 0"))
    elif nature_vecteur == 1:
        a = yV
        b = -xV
        c = -a * xI - b * yI
        return (print("Equation:", a, "x +", b, "y +", c,"= 0"))



def main():
    print("Coordonnés vecteur :")
    xV=float(input("x = "))
    yV=float(input("y = "))
    print("Coordonnés point :")
    xI=float(input("x = "))
    yI=float(input("y = "))
    equation_cartesienne(xV, yV, xI, yI)

if __name__ == '__main__':
    main()