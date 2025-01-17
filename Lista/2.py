def fibonacci(n):
    f1,f2 = 0,1
    l = [f1,f2]
    for numeros in range(2, n + 1):
        proximo = f1 + f2
        l.append(proximo)
        f1,f2 = f2,proximo
    return l

