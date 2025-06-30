import os
from Model.income import income_menu
from Model.expense import expense_menu

def main():
    while True:
        # Limpa o terminal
        os.system('clear')

        # Menu inicial em texto
        print("|" + ("=" * 70) + "|")
        print("|" + "💰 SIG-Finance - Sistema de Controle de Finanças Domésticas".center(69) + "|")
        print("|" + ("=" * 70) + "|")
        print("|" + (" " * 70) + "|")
        print("|" + (" " * 20) + "Escolha uma das opções abaixo:" + (" " * 20) + "|")
        print("|" + (" " * 20) + "[1] 📥 Menu de Receitas" + (" " * 27) + "|")
        print("|" + (" " * 20) + "[2] 📤 Menu de Despesas" + (" " * 27) + "|")
        print("|" + (" " * 20) + "[3] 📈 Relatórios" + (" " * 33) + "|")
        print("|" + (" " * 20) + "[4] 💼 Ver saldo atual" + (" " * 28) + "|")
        print("|" + (" " * 20) + "[0] 🚪 Sair do sistema" + (" " * 28) + "|")
        print("|" + (" " * 70) + "|")
        print("|" + ("=" * 70) + "|")

        # Variável para guardar a resposta do usuário
        resp = input("\nDigite o número da opção desejada: ")
        
        # Limpa o terminal
        os.system('clear')

        match resp:
            case "1":
                print("\n➡️ Submenu de Receitas ainda será implementado.")
                income_menu()
            case "2":
                print("\n➡️ Submenu de Despesas ainda será implementado.")
                expense_menu()
            case "3":
                print("\n📊 Relatórios ainda serão implementados.")
            case "4":
                print("\n[Saldo] A função para exibir o saldo ainda será implementada.")
            case "0":
                print("\n👋 Saindo do sistema... Até logo!")
                break
            case _:
                print("\n❌ Opção inválida. Tente novamente.")
                
        input("\nPressione Enter para continuar...")

main()