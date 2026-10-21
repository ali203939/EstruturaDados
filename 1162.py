casos = int(input())

for _ in range(casos):
    total_vagoes = int(input())

    vagoes = list(map(int, input().split()))

    trocas = 0

    for inversao in range(1, total_vagoes):
        J = inversao

# vagoes [j-1] inverte a minha lista
        while J > 0 and vagoes[J] < vagoes[J - 1]:
            vagoes[J], vagoes[J-1] = vagoes[J-1], vagoes[J]

            trocas += 1
            J -= 1

    print(f"Optimal train swapping takes {trocas} swaps(s).")