# import random

# Criar um array vazio
# numeros = []                # tipo primitivo (int)
# objetos = []                # tipo objeto (classe Foo)

# # Exemplo de classe para objetos
# class Foo:
#     def __init__(self, nome):
#         self.nome = nome

# Criar um array preenchido já com valores
# numeros = [1, 2, 3, 4, 5]
# objetos = [Foo("Ana"), Foo("Bruno"), Foo("Carla")]

# Obter o tamanho do array
# print("Tamanho:", len(numeros))

# Adicionar e remover elementos ao final
# numeros.append(6)       # adiciona no final
# print("Após append:", numeros)
# numeros.pop()           # remove do final
# print("Após pop final:", numeros)

# Adicionar e remover elementos no início
# numeros.insert(0, 0)    # adiciona no início (posição 0)
# print("Após insert início:", numeros)
# numeros.pop(0)          # remove do início
# print("Após remover início:", numeros)

# Adicionar e remover elementos em uma posição específica
# numeros.insert(2, 99)   # insere na posição 2
# print("Após insert pos 2:", numeros)
# numeros.pop(2)          # remove o elemento na posição 2
# print("Após pop pos 2:", numeros)

# Impressão formatada usando join
# # join só funciona com strings
# frutas = ["maçã", "banana", "laranja"]
# print("Frutas:", ", ".join(frutas))

# Criar um array com elementos em sequência de 0 a n
# n = 10
# sequencia = list(range(n + 1))  # [0, 1, 2, ..., 10]
# print("Sequência:", sequencia)

# Criar um array com valores aleatórios
# aleatorios = [random.randint(1, 100) for _ in range(5)]
# print("Aleatórios:", aleatorios)

# Acessar elementos por índice
# print("Primeiro elemento:", numeros[0])
# print("Último elemento:", numeros[-1])

# Percorrer elementos (for-range)
# print("Percorrendo com for direto:")
# for num in numeros:
#     print(num, end=" ")
# print()

# Percorrer elementos (for indexado)
# print("Percorrendo com for indexado:")
# for i in range(len(numeros)):
#     print(f"Index {i}: {numeros[i]}")

# Procurar um elemento X usando laço
# x = 3
# encontrado = False
# for num in numeros:
#     if num == x:
#         encontrado = True
#         break
# print(f"Elemento {x} encontrado (for):", encontrado)

# Procurar um elemento X usando função nativa
# print(f"Elemento {x} encontrado (in):", x in numeros)

# Criar novo array com elementos filtrados (pares)
# pares = [num for num in numeros if num % 2 == 0]
# print("Elementos pares:", pares)

# Criar novo array com elementos transformados (ao quadrado)
# quadrados = [num ** 2 for num in numeros]
# print("Quadrados:", quadrados)

# Buscar e remover um elemento X (primeira ocorrência)
# x = 2
# if x in numeros:
#     numeros.remove(x)
# print("Após remover o 2:", numeros)

# Remover todos os elementos com valor X
# x = 3
# numeros = [num for num in numeros if num != x]
# print("Após remover todos os 3:", numeros)

# Verificar funções nativas úteis
# print("\nFunções nativas úteis:")
# print("- busca: 'in', 'index()'")
# print("- remoção: 'pop()', 'remove()', 'clear()'")
# print("- ordenação: 'sort()', 'sorted()'")
# print("- embaralhamento: random.shuffle(lista)")

# # Exemplo de embaralhar
# random.shuffle(sequencia)
# print("Sequência embaralhada:", sequencia)



