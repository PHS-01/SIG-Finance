import os
from menu_generator import write_menu, create_menu
from transaction_controller import list_transactions

menu = {
    'header' : "💰 SIG-Finance - Relatórios",
    'options_menu' : [
        "[1] 📊 Relatório por Categoria ",
        "[2] 📅 Relatório por Período   ",
        "[3] 📋 Listar Receitas         ",
        "[4] 📋 Listar Despesas         ",
        "[5] 💵 Saldo Geral             ",
        "[0] 🔙 Voltar ao menu principal"
    ]
}

def report_menu(transactions):
    while True:
        # Limpa o terminal
        os.system('clear')

        # Menu inicial em texto
        write_menu(create_menu(menu["header"], menu["options_menu"], size = 70, section_separator = "=", border = "|", recoil = 1))

        # Variável para guardar a resposta do usuário
        resp = input("\nDigite o número da opção desejada: ")
        
        # Limpa o terminal
        os.system('clear')

        match resp:
            case "1":
                print()
            case "2":
                print()
            case "3":
                list_transactions(transactions, "income")
            case "4":
                list_transactions(transactions, "expense")
            case "5":
                print()
            case "0":
                print("\nVoltando para o menu principal do sistema...")
                break
            case _:
                print("\n❌ Opção inválida. Tente novamente.")
                
        input("\nPressione Enter para continuar...")