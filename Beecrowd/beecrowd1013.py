
A , B , C = input().split(" ")


A = int(A)
B = int(B)
C = int(C)

MaiorAB = (A + B + abs(A-B))/2
MaiorC = (MaiorAB + C + abs(MaiorAB - C))/2

print("%.0f eh o maior"%MaiorC)
