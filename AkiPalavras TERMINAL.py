from time import sleep

print("Bem-vindo ao AkiPalavras!")
print("""Para começar, pense em uma dessas dez palavras:
Abacaxi
Melancia
Girassol
Computador
Avião
Chocolate
Caneta
Montanha
Livro
Trompeta
Celular
Piano
Bateria
Tambor""")
sleep(3)
print("Pensou? Vamos começar!")
lista1 = ["Abacaxi", "Melancia", "Girassol", "Computador", "Avião", "Chocolate", "Caneta", "Montanha", "Livro", "Piano",
          "Trompeta", "Celular", "Bateria", "Tambor" ]

perg1 = input("A palavra escolhida tem algo relacionado à natureza? [Sim - Não] ").strip().upper().replace(" ", "")
if perg1 != "SIM":
    lista1.remove("Abacaxi")
    lista1.remove("Melancia")
    lista1.remove("Chocolate")
    lista1.remove("Girassol")
    lista1.remove("Montanha")

    perg6 = input("Possui algo relacionado a tecnologia? [Sim - Não] ").strip().upper().replace(" ", "")
    if perg6 != "SIM":
        lista1.remove("Computador")
        lista1.remove("Avião")
        lista1.remove("Celular")

        perg7 = input("A sua palavra possui característica de gerar alguma melodia? [Sim - Não] ").strip().upper().replace(" ", "")

        if perg7 == "SIM":
            lista1.remove("Caneta")
            lista1.remove("Livro")
            perg10 = input("Sua escolha e um instrumento de sopro? [Sim - Não] ").strip().upper().replace(" ", "")
            if perg10 == "SIM":
                lista1.remove("Piano")
                lista1.remove("Bateria")
                lista1.remove("Tambor")
                print(f"A sua palavra é {', '.join(lista1)}?")

            else:
                lista1.remove("Trompeta")
                pergbaqueta = input("Seu instrumento é tocado por baquetas? [Sim - Não] ").strip().upper().replace(" ",                                                                                                                   "")
                if pergbaqueta == "SIM":
                    lista1.remove("Piano")
                    pergpratos = input("Seu instrumento possui pratos? [Sim - Não] ").strip().upper().replace(" ", "")
                    if pergpratos == "SIM":
                        lista1.remove("Tambor")
                        print(f"A sua palavra é {', '.join(lista1)}?")
                    else:
                        lista1.remove("Bateria")
                        print(f"A sua palavra é {', '.join(lista1)}?")
                else:
                    lista1.remove("Tambor")
                    lista1.remove("Bateria")
                    print(f"A sua palavra é {', '.join(lista1)}?")

        else:
            lista1.remove("Piano")
            lista1.remove("Trompeta")
            lista1.remove("Bateria")
            lista1.remove("Tambor")
            perg8 = input("Pode ser usado para escrever? [Sim - Não] ").strip().upper().replace(" ", "")
            if perg8 == "SIM":
                lista1.remove("Livro")
                print(f"A sua palavra é {', '.join(lista1)}?")
            else:
                lista1.remove("Caneta")
                print(f"A sua palavra é {', '.join(lista1)}?")
    else:
        lista1.remove("Caneta")
        lista1.remove("Livro")
        lista1.remove("Piano")
        lista1.remove("Trompeta")
        perg9 = input("A palavra pode ser usada como um transporte? [Sim - Não] ").strip().upper().replace(" ", "")
        if perg9 == "SIM":
            lista1.remove("Computador")
            lista1.remove("Celular")
            print(f"A sua palavra é {', '.join(lista1)}?")
        else:
            lista1.remove("Avião")
            perg11 = input("Sua escolha cabe no bolso? [Sim - Não] ").strip().upper().replace(" ", "")
            if perg11 == "SIM":
                lista1.remove("Computador")
                print(f"A sua palavra é {', '.join(lista1)}?")
            else:
                lista1.remove("Celular")
                print(f"A sua palavra é {', '.join(lista1)}?")
else:
    lista1.remove("Caneta")
    lista1.remove("Livro")
    lista1.remove("Avião")
    lista1.remove("Piano")
    lista1.remove("Computador")
    lista1.remove("Trompeta")
    lista1.remove("Celular")
    lista1.remove("Tambor")
    lista1.remove("Bateria")

    perg2 = input("Se trata de uma fruta? [Sim - Não] ").strip().upper().replace(" ", "")
    if perg2 == "SIM":
        lista1.remove("Chocolate")
        lista1.remove("Girassol")
        lista1.remove("Montanha")

        perg3 = input("A fruta possui interior vermelho? [Sim - Não] ").strip().upper().replace(" ", "")
        if perg3 == "SIM":
            lista1.remove("Abacaxi")
            lista1.remove("Tambor")
            lista1.remove("Bateria")
            print(f"A sua palavra é {', '.join(lista1)}?")
        else:
            lista1.remove("Melancia")
            print(f"A sua palavra é {', '.join(lista1)}?")
    else:
        lista1.remove("Abacaxi")
        lista1.remove("Melancia")

        perg4 = input("É um alimento? [Sim - Não] ").strip().upper().replace(" ", "")
        if perg4 == "SIM":
            lista1.remove("Girassol")
            lista1.remove("Montanha")
            print(f"A sua palavra é {', '.join(lista1)}?")
        else:
            lista1.remove("Chocolate")
            perg5 = input("Sua escolha pode ser escalada? [Sim - Não] ").strip().upper().replace(" ", "")
            if perg5 == "SIM":
                lista1.remove("Girassol")
                print(f"A sua palavra é {', '.join(lista1)}?")
            else:
                lista1.remove("Montanha")
                print(f"A sua palavra é {', '.join(lista1)}?")