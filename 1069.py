while True:
        expressao = input()
        pilha = []
        diamante = 0

        for caracter in expressao:
            if caracter == "<":
                pilha.append(caracter)


            elif caracter == ">":
                print("Diamante encontrado")
                diamante += 1

