class Item:

    def __init__(self, name: str, itemType: str, balanceType: str):
        self.name = name
        self.itemType = None
        self.balance = [0, 0]
        self.balanceType = None

        if (itemType.lower() == "a" or itemType.lower() == "ativo"):
            self.itemType = "ativo"
        elif (itemType.lower() == "p" or itemType.lower() == "passivo"):
            self.itemType = "passivo"
        elif (itemType.lower() == "pl" or itemType.lower() == "patrimônio líquido"):
            self.itemType = "patrimônio líquido"

        if (balanceType.lower() == "d" or balanceType.lower() == "devedor"):
            self.balanceType = "devedor"
        elif (balanceType.lower() == "c" or balanceType.lower() == "credor"):
            self.balanceType = "credor"

    def setBalance(self, value: float, itemType: str) -> None:
        if (itemType.lower() == "c" or itemType.lower() == "credor"):
            self.balance[1] += value
        elif (itemType.lower() == "d" or itemType.lower() == "devedor"):
            self.balance[0] += value

    def __repr__(self) -> str:
        return f'nome: {self.name}, type:{self.itemType}'