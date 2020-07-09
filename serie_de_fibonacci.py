print("Serie de Fibonacci")

num = int(input("Num: "))
array_num = []

# Recursividad
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return (fibonacci(n-2) + fibonacci(n-1))

# Iteración para mostrar todos los números de la serie de Fibonacci
for i in range(0, num):
    array_num.append(fibonacci(num))
    num = num - 1

# Método sort() para ordenarlos de menor a mayor
array_num.sort()
print(array_num)