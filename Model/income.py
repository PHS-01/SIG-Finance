import os
from menu_generator import write_menu, create_menu
from transaction_controller import create_transaction, list_transactions, update_transaction, delete_transaction

menu = {
    'header' : "💰 SIG-Finance - Receitas",
    'options_menu' : [
        "[1] ➕ Adicionar Receita       ",
        "[2] ➖ Remover Receita         ",
        "[3] 🔄 Atualizar Receita       ",
        "[4] 📋 Listar Receitas         ",
        "[5] 🔍 Buscar por categoria    ",
        "[0] 🔙 Voltar ao menu principal"
    ]
}

def income_menu(transactions):
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
                create_transaction(transactions, "income")
            case "2":
                delete_transaction(transactions,"income")
            case "3":
                update_transaction(transactions, "income")
            case "4":
                list_transactions(transactions, "income")
            case "5":
                print("\n[Receita] A funcionalidade de busca por categoria ainda será implementada.")
            case "0":
                print("\nVoltando para o menu principal do sistema...")
                break
            case _:
                print("\n❌ Opção inválida. Tente novamente.")
                
        input("\nPressione Enter para continuar...")