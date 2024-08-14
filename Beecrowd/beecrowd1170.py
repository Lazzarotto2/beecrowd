
def blobs():
    n = int(input())
    for _ in range(n):
        dias = 0
        c = float(input())
        while c > 1:
            c = c / 2
            dias += 1
        print(dias, "dias")


blobs()
