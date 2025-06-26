import os
        
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
        print("|" + (" " * 20) + "[1] ➕ Adicionar receita" + (" " * 26) + "|")
        print("|" + (" " * 20) + "[2] ➖ Adicionar despesa" + (" " * 26) + "|")
        print("|" + (" " * 20) + "[3] 📊 Exibir relatório" + (" " * 27) + "|")
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
                print("\n[Receita] A função para adicionar receita ainda será implementada.")
            case "2":
                print("\n[Despesa] A função para adicionar despesa ainda será implementada.")
            case "3":
                print("\n[Relatório] A função para exibir o relatório ainda será implementada.")
            case "4":
                print("\n[Saldo] A função para exibir o saldo ainda será implementada.")
            case "0":
                print("\nSaindo do sistema... Até logo!")
                break
            case _:
                print("\n❌ Opção inválida. Tente novamente.")
                
        input("\nPressione Enter para continuar...")

main()