from math import factorial as f

n = int(input("Введите количество бросков: "))
m = int(input("Введите количесвтво раз: "))
s = int(input("Введите число: "))

def dice(N, M, S):
    p = (6 - S + 1) * (1/6)
    combination = f(N) / (f(N - M) * f(M))
    chance = combination * p**M * (1 - p)**(N - M)

    print(chance)


dice(n, m, s)
