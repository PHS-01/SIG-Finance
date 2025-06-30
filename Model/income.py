import os

def income_menu():
    while True:
        # Limpa o terminal
        os.system('clear')

        # Menu inicial em texto
        print("|" + ("=" * 70) + "|")
        print("|" + "💰 SIG-Finance - Receitas".center(69) + "|")
        print("|" + ("=" * 70) + "|")
        print("|" + (" " * 70) + "|")
        print("|" + (" " * 20) + "Escolha uma das opções abaixo:" + (" " * 20) + "|")
        print("|" + (" " * 20) + "[1] ➕ Adicionar Receita" + (" " * 26) + "|")
        print("|" + (" " * 20) + "[2] ➖ Remover Receita " + (" " * 27) + "|")
        print("|" + (" " * 20) + "[3] 📋 Listar Receitas" + (" " * 28) + "|")
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
                print("\n[Receita] A funcionalidade de adicionar receita ainda será implementada.")
            case "2":
                print("\n[Receita] A funcionalidade de remover receita ainda será implementada.")
            case "3":
                print("\n[Receita] A funcionalidade de listar receitas ainda será implementada.")
            case "4":
                print("\n[Receita] A funcionalidade de busca por categoria ainda será implementada.")
            case "0":
                print("\nVoltando para o menu principal do sistema...")
                break
            case _:
                print("\n❌ Opção inválida. Tente novamente.")
                
        input("\nPressione Enter para continuar...")