import os
from menu_generator import write_menu, create_menu

menu = {
    'header' : "💰 SIG-Finance - Categorias",
    'options_menu' : [
        "[1] ➕ Adicionar Categoria     ",
        "[2] ➖ Remover Categoria       ",
        "[3] 🔄 Atualizar Categoria     ",
        "[4] 📋 Listar Categoria        ",
        "[0] 🔙 Voltar ao menu principal"
    ]
}

def category_menu(categories):
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
                print()
            case "4":
                print()
            case "0":
                print("\nVoltando para o menu principal do sistema...")
                break
            case _:
                print("\n❌ Opção inválida. Tente novamente.")
                
        input("\nPressione Enter para continuar...")