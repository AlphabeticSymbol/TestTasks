from math import sqrt as s, fsum

a1 = [1, 3, 6, 7, 8]
a2 = [45, -89, -92, 26, 5]

def cosine_similarity(v1, v2):
    if len(v1) == len(v2):
        dot = 0
        norm_v1 = 0
        norm_v2 = 0
        for i in range(len(v1)):
            dot += v1[i] * v2[i]
            norm_v1 += v1[i]**2
            norm_v2 += v2[i]**2
        print(dot / (s(norm_v1) * s(norm_v2)))
    elif len(v1) == 0:
        print("Вектор 1 равен нулю")
    elif len(v2) == 0:
        print("Вектор 2 равен 0")
    elif len(v1) != len(v2):
        print('Разная длина векторов')

cosine_similarity(a1,a2)