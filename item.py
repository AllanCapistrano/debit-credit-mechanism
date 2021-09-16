class Item:

    def __init__(self, name: str, iType: str):
        self.name = name
        self.balance = [0, 0]
        self.iType = None

        if (iType.lower() == "a" or iType.lower() == "ativo"):
            self.iType = "ativo"
        elif (iType.lower() == "p" or iType.lower() == "passivo"):
            self.iType = "passivo"
        elif (iType.lower() == "pl" or iType.lower() == "patrimônio líquido"):
            self.iType = "patrimônio líquido"

    def setBalance(self, value: float, balanceType: str) -> None:
        if (balanceType.lower() == "c" or balanceType.lower() == "credor"):
            self.balance[1] += value
        elif (balanceType.lower() == "d" or balanceType.lower() == "devedor"):
            self.balance[0] += value

    def __repr__(self) -> str:
        return f'nome: {self.name}, type:{self.iType}'