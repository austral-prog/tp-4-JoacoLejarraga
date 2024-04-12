def line():
    
    coefA = float(input("Ingrese el coeficiente A: "))
    coefB = float(input("Ingrese el coeficiente B: "))
    coefX1 = float(input("Ingrese el coeficiente X1: "))
    coefX2 = float(input("Ingrese el coeficiente X2: "))
    
    print(f"El coeficiente A de su ecuación de la recta es: {coefA}")
    print(f"El coeficiente B de su ecuación de la recta es: {coefB}")
    print(f"El coeficiente X1 de su ecuación de la recta es: {coefX1}")
    print(f"El coeficiente X2 de su ecuación de la recta es: {coefX2}")
    print("")
    print("Para la siguiente ecuación:")
    print(f"\tY = {coefA}X + {coefB}")
    Y1 = float(coefA * coefX1 + coefB)
    Y2 = float(coefA * coefX2 + coefB)
    print("")
    print("Dados los siguientes puntos:")
    print(f"\tP1 ({coefX1}, {Y1})")
    print(f"\tP2 ({coefX2}, {Y2})")

    dist = float(((coefX2 - coefX1) ** 2 + (Y2 - Y1) ** 2) ** 0.5)
    print("")
    print(f"La distancia entre ellos es: {dist}")
