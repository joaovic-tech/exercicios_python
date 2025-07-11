def evenOrOdd(num):
    if num % 2 == 0:
        return f"O número {num} é par"
    return f"O número {num} é impar"


num = int(input("Digite um número: "))

print(evenOrOdd(num))
