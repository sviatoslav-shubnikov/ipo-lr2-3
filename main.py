import math

X=float(input("Введите объем шара в куб. ед.: "))
radius = ((3*X)/(4*math.pi)) ** (1/3)

print (f"Радиус шара: {radius}")