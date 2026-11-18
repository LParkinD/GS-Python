from assistente import Assistente

assistente = Assistente()

status = 1

while status != 0:
    print("[1] Identificar problema")
    print("[2] Precisa de ajuda em alguma categoria?")
    print("[3] Informações de documentos")
    print("[4] Orientação")
    print("[0] Sair")

    status = int(input("Selecione a seguinte opção: "))

    match status:
        case 1:
            assistente.navegar()

        case 2:
            assistente.perguntar()

        case 3:
            assistente.registrar()

        case 4:
            print("")

        case 0:
            break

        case _:
            print("Opção inválida")
