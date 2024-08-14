
A , B , C = input().split()


A = float(A)
B = float(B)
C = float(C)
pi = 3.14159
a = (A * C)/2
b = pi * C**2
c = ((A+B)*C)/2
d = B * B
e = A * B


print("TRIANGULO: %.3f"%a)
print("CIRCULO: %.3f"%b)
print("TRAPEZIO: %.3f"%c)
print("QUADRADO: %.3f"%d)
print("RETANGULO: %.3f"%e)