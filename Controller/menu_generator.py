# Escreve o menu na tela(Terminal)
def write_menu(menu):
    for line in menu:
        print(line)

# Criar um menu é retorna ele
def create_menu(header, options_menu, size, section_separator = " ", border = " ", recoil = 0):

    menu_header = [
        border + (section_separator * size) + border,
        border + header.center(size-recoil) + border,
        border + (section_separator * size) + border,
        border + (" " * size) + border,
    ]

    menu_content = []

    menu_footer = [
        border + (" " * size) + border,
        border + (section_separator * size) + border
    ]

    for option in options_menu:
        menu_content.append(border + option.center(size-recoil) + border)

    menu = menu_header + menu_content + menu_footer
    
    return menu

def create_menu_list(header, options_menu, footer, size, section_separator = " ", border = " "):
    string_header = ""
    for title in header:
        string_header += border + str(title).ljust(int(size/2))

    menu_header = [
        border + (section_separator * int(size/2)) + border + (section_separator * int(size/2)) + border,
        string_header + border,
        border + (section_separator * int(size/2)) + border + (section_separator * int(size/2)) + border,
    ]

    menu_content = []
    string_content = ""
    for key, item in options_menu.items():
        menu_content.append(border + key.ljust(int(size/2)) + border + str(item).ljust(int(size/2)) + border)

    string_footer = ""
    for title in footer:
        string_footer += border + str(title).ljust(int(size/2))

    menu_footer = [
        border + (section_separator * int(size/2)) + border + (section_separator * int(size/2)) + border,
        string_footer + border,
        border + (section_separator * int(size/2)) + border + (section_separator * int(size/2)) + border,
    ]

    menu = menu_header + menu_content + menu_footer
    
    return menu

    
menu = {
    "header" : ["Categoria", "Total"],
    "options_menu" : {
        "Salário" : 3000.00 ,
        "test" : 3000.00 ,
        },
    "footer" : ["Total", "520.50"],
}

write_menu(create_menu_list(menu["header"], menu["options_menu"], menu["footer"], 50, "-", "|"))

"""
    ===============================
    📊 RELATÓRIO POR CATEGORIA
    ===============================
    Tipo: Receita

    Categoria           | Total (R$)
    --------------------|------------
    Salário             | 3000.00
    Investimento        | 250.75
    --------------------|------------
    Total               | 3250.75

    Tipo: Despesa

    Categoria           | Total (R$)
    --------------------|------------
    Alimentação         | 440.50
    Transporte          | 80.00
    --------------------|------------
    Total               | 520.50
"""

"""
    ===============================
    📅 RELATÓRIO POR PERÍODO
    ===============================
    Tipo: Receita

    Período    | Total (R$)
    -----------|------------
    2025-07    | 3250.75

    Tipo: Despesa

    Período    | Total (R$)
    -----------|------------
    2025-07    | 520.50

"""