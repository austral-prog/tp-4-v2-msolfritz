def line():
    A=float(input("Ingrese el coeficiente A: "))
    B=float(input("Ingrese el coeficiente B: "))
    X1=float(input("Ingrese el coeficiente X1: "))
    X2=float(input("Ingrese el coeficiente X2: "))
    print(f"El coeficiente A de su ecuación de la recta es: {A}")
    print(f"El coeficiente B de su ecuación de la recta es: {B}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {X1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {X2}")
    print("")
    Y1= A*X1+B
    Y2=A*X2+B
    print(f"Para la siguiente ecuación:\n\tY = {A}X + {B}") 
    print("")
    print(f"Dados los siguientes puntos:\n\tP1 ({X1}, {Y1})\n\tP2 ({X2}, {Y2})")
    print("")
    x1, y1= X1, Y1
    x2, y2= X2, Y2
    distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    print(f"La distancia entre ellos es: {distancia}")
