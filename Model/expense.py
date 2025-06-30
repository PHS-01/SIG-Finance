import os

def expense_menu():
    while True:
        # Limpa o terminal
        os.system('clear')

        # Menu inicial em texto
        print("|" + ("=" * 70) + "|")
        print("|" + "💰 SIG-Finance - Despesa".center(69) + "|")
        print("|" + ("=" * 70) + "|")
        print("|" + (" " * 70) + "|")
        print("|" + (" " * 20) + "Escolha uma das opções abaixo:" + (" " * 20) + "|")
        print("|" + (" " * 20) + "[1] ➖ Adicionar Despesa" + (" " * 26) + "|")
        print("|" + (" " * 20) + "[2] ➖ Remover Despesa" + (" " * 28) + "|")
        print("|" + (" " * 20) + "[3] 📋 Listar Despesas" + (" " * 28) + "|")
        print("|" + (" " * 20) + "[4] 🔍 Buscar por categoria" + (" " * 23) + "|")
        print("|" + (" " * 20) + "[0] 🔙 Voltar ao menu principal" + (" " * 19) + "|")
        print("|" + (" " * 70) + "|")
        print("|" + ("=" * 70) + "|")

        # Variável para guardar a resposta do usuário
        resp = input("\nDigite o número da opção desejada: ")
        
        # Limpa o terminal
        os.system('clear')

        match resp:
            case "1":
                print("\n[Despesa] A funcionalidade de adicionar despesa ainda será implementada.")
            case "2":
                print("\n[Despesa] A funcionalidade de remover despesa ainda será implementada.")
            case "3":
                print("\n[Despesa] A funcionalidade de listar despesas ainda será implementada.")
            case "4":
                print("\n[Despesa] A funcionalidade de busca por categoria ainda será implementada.")
            case "0":
                print("\nVoltando para o menu principal do sistema...")
                break
            case _:
                print("\n❌ Opção inválida. Tente novamente.")
                
        input("\nPressione Enter para continuar...")