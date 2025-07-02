import os
from menu_generator import write_menu, create_menu

menu = {
    'header' : "💰 SIG-Finance - Receitas",
    'options_menu' : [
        "[1] ➕ Adicionar Receita       ",
        "[2] ➖ Remover Receita         ",
        "[3] 📋 Listar Receitas         ",
        "[4] 🔍 Buscar por categoria    ",
        "[0] 🔙 Voltar ao menu principal"
    ]
}

def income_menu():
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