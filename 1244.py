casos = int(input())

for _ in range(casos):

    palavras = input().split()

    palavras.sort(key=len, reverse=True)

    print(" ".join(palavras))