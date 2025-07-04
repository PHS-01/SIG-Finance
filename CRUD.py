# Função Create
def create(data_list, item):
    # Adiciona um novo item à lista de dados.
    data_list.append(item)
    return data_list

# Função Read
def read(data_list, query = None):
    # Retorna todos os itens que correspondem aos critérios de busca (query).
    if not query:
        return data_list
    else:
        for item in data_list:
            if item['ID'] == query:
                return item
            else:
                continue

# Função Update
def update(data_updates, data_list, query):
    # Atualiza os itens que correspondem à query com os valores em updates.
    for item in data_list:
        if item['ID'] == query:
            item.update(data_updates)
        else:
            continue
    return data_list

# Função Delete
def delete(data_list, query = None):
    # Remove itens que correspondem à query da lista de dados.
    if not query:
        data_list.clear()
        return data_list
    else:
        for item in data_list:
            if item['id'] == query:
                data_list.pop(query-1)
            else:
                continue

    return data_list