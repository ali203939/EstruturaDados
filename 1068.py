while True:
    try:
        expressao = input()
        pilha = []
        correta = True

        for caracter in expressao:
            if caracter == "(":
                pilha.append(caracter)


            elif caracter == ")":

                if len(pilha) == 0:
                    correta = False
                    break
                pilha.pop()
        if correta and len(pilha) == 0:
            print("correct")
        else:
            print("incorrect")

    except EOFError:
        break