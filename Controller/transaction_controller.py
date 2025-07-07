from datetime import datetime
from Controller.CRUD import create, read, update, delete

# Função para traduzir os tipos para português
def translate_type(type):
    return {
        "income": "receita",
        "expense": "despesa"
    }.get(type, type)

def create_transaction(data_transaction, type):
    translated_type = translate_type(type)
    print(f"[Adicionar {translated_type.capitalize()}]")
    try:
        id = max(data_transaction.keys(), default=0) + 1
        description = input("Descrição: ")
        value = float(input("Valor: "))
        date = datetime.now().strftime("%Y-%m-%d")
        category_id = int(input("ID da Categoria: "))
        new_data = {
            "type": type,
            "description": description,
            "value": value,
            "date": date,
            "category_id": category_id
        }
        create(data_transaction, new_data, id)
        print(f"\n✅ {translated_type.capitalize()} adicionada com sucesso.")
    except Exception as e:
        print(f"\n❌ Erro ao adicionar: {e}")

def list_transactions(data_transaction, type, query=None):
    translated_type = translate_type(type)
    print(f"[Listar {translated_type.capitalize()}]")
    data = read(data_transaction, query)

    if query:
        if data and data.get("type") == type:
            print(f"- ID {query} : {data['description']} - R$ {data['value']} em {data['date']} (Categoria {data['category_id']})")
        else:
            print(f"❗ Nenhuma {translated_type} com ID {query} foi encontrada.")
    else:
        found = False
        for id, item in data.items():
            if item.get("type") == type:
                found = True
                print(f"- ID {id} : {item['description']} - R$ {item['value']} em {item['date']} (Categoria {item['category_id']})")
        if not found:
            print(f"❗ Nenhuma {translated_type} foi cadastrada ainda.")

def update_transaction(data_transaction, type):
    translated_type = translate_type(type)
    print(f"[Atualizar {translated_type.capitalize()}]")
    try:
        id = int(input(f"ID da {translated_type} a atualizar: "))
        if data_transaction.get(id, {}).get("type") != type:
            print(f"❗ O ID {id} não corresponde a uma {translated_type}.")
            return
        list_transactions(data_transaction, type, id)
        print(f"Informe os novos dados da {translated_type}:")
        description = input("Descrição: ")
        value = float(input("Valor: "))
        date = datetime.now().strftime("%Y-%m-%d")
        category_id = int(input("ID da Categoria: "))
        data_updates = {
            "type": type,
            "description": description,
            "value": value,
            "date": date,
            "category_id": category_id
        }
        update(data_updates, data_transaction, query=id)
        print(f"\n✅ {translated_type.capitalize()} atualizada com sucesso.")
    except Exception as e:
        print(f"\n❌ Erro ao atualizar: {e}")

def delete_transaction(data_transaction, type):
    translated_type = translate_type(type)
    print(f"[Remover {translated_type.capitalize()}]")
    try:
        id = int(input(f"ID da {translated_type} a remover: "))
        if data_transaction.get(id, {}).get("type") != type:
            print(f"❗ O ID {id} não corresponde a uma {translated_type}.")
            return
        delete(data_transaction, query=id)
        print(f"\n✅ {translated_type.capitalize()} removida com sucesso.")
    except Exception as e:
        print(f"\n❌ Erro ao remover: {e}")
