while True: 
    comando = input("Digiter a palavra !")

    if comando.lower() == "sair" :
        print("Fim do programa")
        break
    if len(comando) < 2:
        print("Comando inválido")
        print("Tente digitar 'sair' para encerrar o programa")
        continue
