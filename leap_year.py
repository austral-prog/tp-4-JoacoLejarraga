def leap_year():
    year = int(input("Ingrese un año: "))
    n = float(year / 4)
    if (year == 4 or year == -4) or n % 2 == 0: 
        print("El año", year, "es bisiesto")
    else: 
        print("El año", year, "no es bisiesto")
