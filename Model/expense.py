import os
from menu_generator import write_menu, create_menu

menu = {
    'header' : "💰 SIG-Finance - Despesa",
    'options_menu' : [
        "[1] ➕ Adicionar Despesa       ",
        "[2] ➖ Remover Despesa         ",
        "[3] 📋 Listar Despesas         ",
        "[4] 🔍 Buscar por categoria    ",
        "[0] 🔙 Voltar ao menu principal"
    ]
}

def expense_menu():
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