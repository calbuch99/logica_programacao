while True:
  print("Minha lâmpada está queimada ?")
  opcao = input("Digite Sim ou Não para opção :")

  if opcao == "sim":
    print("Sim está queimada")
    break
  elif opcao == "não":
    print("Não está queimada, verificar o bulbo !")


  bulbo = input("O Bulbo está queimado ?")

  if bulbo == "sim" :
    print("Trocar o bulbo !")
    break
  elif bulbo == "não":
    print("Problema não está o bulbo ! ")
    break