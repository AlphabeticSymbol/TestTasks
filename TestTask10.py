def f(x):
    return 3 * x**3 + 4 * x**2 + 5 * x + 21

def find_minimum(a, b, epsilon):
    while abs(b - a) > epsilon:
        c = (a + b) / 2

        fa = f(a)
        fc = f(c)
        fb = f(b)

        if fc < fb:
            b = c
        else:
            a = c

    return [a, b]

a = -10
b = 10
epsilon = 0.01

min_interval = find_minimum(a, b, epsilon)
print("Минимум функции на интервале:", min_interval)