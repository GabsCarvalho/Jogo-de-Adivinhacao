import time
import random

def jogar(dificuldade):
    limite = 0
    if dificuldade == "normal":
        limite = 10
    elif dificuldade == "medio":
        limite = 50
    else:
        limite = 100
    aleatorio = random.randint(1,limite)
    acertou = False

    print(f"\nVamos começar, beleza? Vocês está no modo {dificuldade.upper()}! Tente adivinhar o número de 1 a {limite}.\n")


    while not acertou:
        try:
            chute = int(input(f"Insira um valor de 1 a {limite}: "))

            if chute < 1 or chute > limite:
                print(f"Por favor, digite um número de 1 a {limite}.")
                time.sleep(1)
                continue

            if chute > aleatorio:
                print("\nO chute foi maior que o número gerado.\n")
                time.sleep(1)
            elif chute < aleatorio:
                print("\nO chute foi menor que o número gerado.\n")
                time.sleep(1)
            else:
                print("\nVocê acertou!\n")
                time.sleep(2)
                acertou = True
            
                while True:
                    if dificuldade == "normal":
                        resposta = input(
                            "Gostaria de continuar? Escolha:\n"
                            "1 - Manter no modo atual\n"
                            "2 - Aumentar para o modo médio\n"
                            "3 - Aumentar para o modo dificil\n"
                            "4 - Sair do jogo\n"
                            "Digite o número da sua escolha: "
                        ).strip()
                    elif dificuldade == "medio":
                        resposta = input(
                            "Gostaria de continuar? Escolha:\n"
                            "1 - Manter no modo atual\n"
                            "2 - Diminuir para o modo normal\n"
                            "3 - Aumentar para o modo dificil\n"
                            "4 - Sair do jogo\n"
                            "Digite o número da sua escolha: "
                        ).strip()
                        
                    else:
                        resposta = input(
                            "Gostaria de continuar? Escolha:\n"
                            "1 - Manter no modo atual\n"
                            "2 - Diminuir para o modo normal\n"
                            "3 - Diminuir para o modo médio\n"
                            "4 - Sair do jogo\n"
                            "Digite o número da sua escolha: "
                        ).strip()

                    if resposta == "1":
                        jogar(dificuldade) 
                        return
                    elif resposta == "2":
                        if dificuldade == "normal":
                            jogar("medio")  
                        elif dificuldade == "medio":
                            jogar("normal")  
                        else:
                            jogar("normal")  
                        return

                    elif resposta == "3":
                        if dificuldade == "normal":
                            jogar("dificil") 
                        elif dificuldade == "medio":
                            jogar("dificil")  
                        else:
                            jogar("medio")  
                        return
                    
                    elif resposta == "4":
                        print("Foi um prazer jogar com você! Até a próxima.")
                        exit()
                    else:
                        print("Opção inválida! Por favor, escolha entre 1, 2, 3 ou 4.")

        except ValueError:
            print("Valor inválido! Por favor, digite um número inteiro.")


## Boas vindas
while True:
    print("\nBem-vindo ao jogo de adivinhação!"
        "\nVamos começar escolhendo o modo de jogo:"
        "\n1- Normal (1 a 10)"
        "\n2- Médio (1 a 50)"
        "\n3 - Dificil (1 a 100)"
        "\n4 - Sair do jogo")

    try:

        escolha = int(input("\nDigite o número da sua escolha: "))

        if escolha == 1:
            jogar("normal")
            time.sleep(0.5)
        elif escolha == 2:
            jogar("medio")
            time.sleep(0.5)
        elif escolha == 3:
            jogar("dificil")
            time.sleep(0.5)
        elif escolha == 4:
            print("Obrigado por jogar! Até a próxima.")
            time.sleep(1)
            exit()
        else:
            print("Opção inválida! Por favor, escolha entre 1, 2 ou 3.")
            time.sleep(0.5)

    except ValueError:
        print("Valor inválido! Por favor, digite um número válido.")
        time.sleep(1)