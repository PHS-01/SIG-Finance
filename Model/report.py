import os
from Controller.menu_generator import write_menu, create_menu, create_menu_list
from Controller.transaction_controller import list_transactions
from Controller.report_controller import report_category, report_period, report_total_balance

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

def report_menu(transactions, categories):
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
                data_list = report_category(transactions, categories)
                menu_list = {
                    "header" : ["Categoria", "Total"],
                    "options_menu" : data_list["income"],
                    "footer" : ["Total", data_list["income"]["Total"]],
                }
                print("\nReceitas: \n")
                write_menu(create_menu_list(menu_list["header"], menu_list["options_menu"], menu_list["footer"], 50, "-", "|"))

                menu_list = {
                    "header" : ["Categoria", "Total"],
                    "options_menu" : data_list["expense"],
                    "footer" : ["Total", data_list["expense"]["Total"]],
                }
                print("\nDespesas: \n")
                write_menu(create_menu_list(menu_list["header"], menu_list["options_menu"], menu_list["footer"], 50, "-", "|"))
            case "2":
                data_list = report_period(transactions)
                menu_list = {
                    "header" : ["Período", "Total"],
                    "options_menu" : data_list["income"],
                    "footer" : ["Total", data_list["income"]["Total"]],
                }
                print("\nReceitas: \n")
                write_menu(create_menu_list(menu_list["header"], menu_list["options_menu"], menu_list["footer"], 50, "-", "|"))

                menu_list = {
                    "header" : ["Período", "Total"],
                    "options_menu" : data_list["expense"],
                    "footer" : ["Total", data_list["expense"]["Total"]],
                }
                print("\nDespesas: \n")
                write_menu(create_menu_list(menu_list["header"], menu_list["options_menu"], menu_list["footer"], 50, "-", "|"))
            case "3":
                list_transactions(transactions, "income", categories)
            case "4":
                list_transactions(transactions, "expense", categories)
            case "5":
                print(report_total_balance(transactions))
            case "0":
                print("\nVoltando para o menu principal do sistema...")
                break
            case _:
                print("\n❌ Opção inválida. Tente novamente.")
                
        input("\nPressione Enter para continuar...")