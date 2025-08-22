# Fatorial iterativo
def fatorial(n):
    resultado = 1
    for i in range(1, n+1): # n+1 para incluir o n; ex: n=5, range(1, 6)
        resultado *= i
    return resultado
    
n=5
print(f"Fatorial de {n}: {fatorial(n)}") # 120