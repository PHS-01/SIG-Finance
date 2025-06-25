import os

def display_header():
    print("=" * 70)
    print("💰 SIG-Finance - Sistema de Controle de Finanças Domésticas".center(70))
    print("=" * 70)

def display_menu():
    print("\nEscolha uma das opções abaixo:\n")
    print(" [1] ➕ Adicionar Receita")
    print(" [2] ➖ Adicionar Despesa")
    print(" [3] 📊 Exibir Relatório")
    print(" [4] 💼 Saldo Atual")
    print(" [0] 🚪 Sair")
    
    print()
    print("=" * 70)
        
def main():
    while True:
        os.system('clear')
        display_header()
        display_menu()
    
        resp = input("\nDigite o número da opção desejada: ")
        match resp:
            case "1":
                print("\n[Receita] Função de adicionar receita ainda será implementada.")
            case "2":
                print("\n[Despesa] Função de adicionar despesa ainda será implementada.")
            case "3":
                print("\n[Relatório] Função de exibir relatório ainda será implementada.")
            case "4":
                print("\n[Saldo] Função de exibir saldo ainda será implementada.")
            case "0":
                print("\nSaindo do sistema... Até logo!")
                break
            case _:
                print("\n❌ Opção inválida. Tente novamente.")
                
        input("\nPressione Enter para continuar...")

main()