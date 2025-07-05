import os
from datetime import datetime
from menu_generator import write_menu, create_menu
from CRUD import create, read, update, delete

categories = [
    {"id": 1, "name": "Alimentação"},
    {"id": 2, "name": "Transporte"},
    {"id": 3, "name": "Salário"},
    {"id": 4, "name": "Investimento"}
]

incomes = {
    1 : {"description": "Salário Mensal", "value": 3000.00, "date": "2025-07-01", "category_id": 3},
    2 : {"description": "Dividendos de Ações", "value": 250.75, "date": "2025-07-03", "category_id": 4}
}

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

def create_income():
    print("[Adicionar Receita]")
    try:
        id = max(incomes.keys())+1
        description = input("Descrição: ")
        value = float(input("Valor: "))
        date = datetime.now().strftime("%Y-%m-%d")
        category_id = int(input("ID da Categoria: "))
        new_income = {
            "id": id,
            "description": description,
            "value": value,
            "date": date,
            "category_id": category_id
        }
        create(incomes, new_income, id)
        print("\n✅ Receita adicionada com sucesso.")
    except Exception as e:
        print(f"\n❌ Erro ao adicionar: {e}")

def list_incomes(query = None):
    print("[Listar Receitas]")
    data = read(incomes, query)
    if not data:
        print("Nenhuma receita cadastrada.")
    elif not query:
        for id, item in data.items():
            print(f"- ID {id} : {item['description']} - R$ {item['value']} em {item['date']} (Categoria {item['category_id']})")
    else:
        print(f"- ID {query} : {data['description']} - R$ {data['value']} em {data['date']} (Categoria {data['category_id']})")

def delete_income():
    print("[Remover Receita]")
    try:
        id = int(input("ID da Receita a remover: "))
        delete(incomes, query=id)
        print("\n✅ Receita removida com sucesso.")
    except Exception as e:
        print(f"\n❌ Erro ao remover: {e}")

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
                create_income()
            case "2":
                delete_income()
            case "3":
                list_incomes()
            case "4":
                print("\n[Receita] A funcionalidade de busca por categoria ainda será implementada.")
            case "0":
                print("\nVoltando para o menu principal do sistema...")
                break
            case _:
                print("\n❌ Opção inválida. Tente novamente.")
                
        input("\nPressione Enter para continuar...")