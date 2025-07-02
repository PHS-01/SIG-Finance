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