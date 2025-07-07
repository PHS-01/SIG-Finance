# Função Create
def create(data_list, item, id):
    # Adiciona um novo item à lista de dados.
    data_list[id] = (item)
    return data_list

# Função Read
def read(data_list, query = None):
    # Retorna todos os itens que correspondem aos critérios de busca (query).
    if not query:
        return data_list
    else:
        return data_list[query]

# Função Update
def update(data_updates, data_list, query):
    # Atualiza os itens que correspondem à query com os valores em updates.
    data_list.update({query : data_updates})
    return data_list

# Função Delete
def delete(data_list, query = None):
    # Remove itens que correspondem à query da lista de dados.
    if not query:
        data_list.clear()
        return data_list
    else:
        del data_list[query]

    return data_list