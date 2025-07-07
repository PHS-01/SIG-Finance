import os
from Controller.menu_generator import write_menu, create_menu
from Controller.CRUD import create, read, update, delete

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

def create_category(data_category):
    print("[Adicionar Categoria]")
    try:
        id = max(data_category.keys(), default=0) + 1
        name = input("Nome: ")
        new_data = {
            "name": name
        }
        create(data_category, new_data, id)
        print("\n✅ Categoria adicionada com sucesso.")
    except Exception as e:
        print(f"\n❌ Erro ao adicionar: {e}")

def list_category(data_category, query=None):
    print("[Listar Categoria]")

    data = read(data_category, query)

    if not query:
        for id, item in data.items():
            print(f"- ID {id} : {item['name']}")
    else:
        print(f"- ID {query} : {data['name']}")

def update_category(data_category):
    print("[Atualizar Categoria]")
    try:
        id = int(input(f"ID da Categoria a atualizar: "))
        list_category(data_category, id)
        print(f"Informe os novos dados da Categoria {id}:")
        name = input("Nome: ")
        data_updates = {
            "name": name
        }
        update(data_updates, data_category, query=id)
        print("\n✅ Categoria atualizada com sucesso.")
    except Exception as e:
        print(f"\n❌ Erro ao atualizar: {e}")

def delete_category(data_category):
    print("[Remover Categoria]")
    try:
        id = int(input("ID da Categoriaa remover: "))
        delete(data_category, query=id)
        print(f"\n✅ Categoria removida com sucesso.")

    except Exception as e:
        print(f"\n❌ Erro ao remover: {e}")

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
                create_category(categories)
            case "2":
                delete_category(categories)
            case "3":
                update_category(categories)
            case "4":
                list_category(categories)
            case "0":
                print("\nVoltando para o menu principal do sistema...")
                break
            case _:
                print("\n❌ Opção inválida. Tente novamente.")
                
        input("\nPressione Enter para continuar...")