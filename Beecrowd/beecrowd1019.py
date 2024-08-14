T = int(input())

def tempo(T):
    horas = 0
    while T >= 3600:
        T -= 3600
        horas += 1
    minutos = 0
    while T >= 60:
        T -= 60
        minutos += 1
    segundos = 0
    while T >= 1:
        T -= 1
        segundos += 1
    print("{:1}:{:1}:{:1}".format(horas,minutos,segundos))


tempo(T)