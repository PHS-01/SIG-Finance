import os
from Controller.menu_generator import write_menu, create_menu
from Controller.transaction_controller import create_transaction, list_transactions, update_transaction, delete_transaction

menu = {
    'header' : "💰 SIG-Finance - Despesa",
    'options_menu' : [
        "[1] ➕ Adicionar Despesa       ",
        "[2] ➖ Remover Despesa         ",
        "[3] 🔄 Atualizar Despesa       ",
        "[4] 📋 Listar Despesas         ",
        "[5] 🔍 Buscar por categoria    ",
        "[0] 🔙 Voltar ao menu principal"
    ]
}

def expense_menu(transactions, categories):
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
                create_transaction(transactions, "expense")
            case "2":
                delete_transaction(transactions, "expense")
            case "3":
                update_transaction(transactions, "expense")
            case "4":
                list_transactions(transactions, "expense", categories)
            case "5":
                print("\n[Despesa] A funcionalidade de busca por categoria ainda será implementada.")
            case "0":
                print("\nVoltando para o menu principal do sistema...")
                break
            case _:
                print("\n❌ Opção inválida. Tente novamente.")
                
        input("\nPressione Enter para continuar...")