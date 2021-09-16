from item import Item

def init() -> list:
    """ Initialize the debit and credit mechanism

    Returns
    -----------
    itens: :class:`list`
        List of itens
    """
    
    itens = []
    
    print("\n> Bem vindo ao mecanismo de débito e crédito")
    print("\n> Primeiro é necessário indicar quais os itens serão utilizados:")
    print("> Para encerrar, basta enviar #")
    
    while(True):
        print("\n> Nome do item:")
        itemName = input("$ ")
        
        if (itemName == "#"):
            break
        
        print("> Tipo [(A)tivo, (P)assivo, (P)atrimônio (L)íquido]:")
        itemType = input("$ ")
        
        if (itemType == "#"):
            break

        itens.append(Item(itemName, itemType))

    return itens

    
def options() -> int:
    """ Options to shell menu
    Returns
    -----------
    option: :class:`int`
        Value of the selected option
    """
    print("> Escolha uma das opções:\n")
    print("> 1. Dar entrada nos valores")
    print("> 2. Gerar Balancete de Verificação")
    print("> 3. Sair")
    
    return int(input("$ "))