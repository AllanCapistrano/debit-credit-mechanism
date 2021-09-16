from shell import init, options
from services.calculateBalance import CalculateBalance
from services.file import File

TRANSATIONS_FILE = "transations.txt"
BALANCE_SHEET = "balance_sheet.txt"

itens = []

if __name__ == "__main__":
    itens = init()

    file = File()

    file.createFile(TRANSATIONS_FILE)
    file.createFile(BALANCE_SHEET)

    calculateBalance = CalculateBalance()
    
    while (True):
        option = options()

        if (option == 3):
            print("\n> Até mais!")

            exit()
        elif (option == 1):
            print("\n> Digite o primeiro item da transação:")
            firstItemInput = input("$ ")

            print("Digite o tipo do saldo do primeiro item [(C)redor/(D)evedor]:")
            firstItemBalanceType = input("$ ")

            if (firstItemBalanceType == "d" or firstItemBalanceType == "devedor"):
                secondItemBalanceType = "credor"
            else:
                secondItemBalanceType = "devedor"

            print("> Digite o segundo item da transação:")
            secondItemInput = input("$ ")

            print("> Digite o valor da transação:")
            valueInput = input("$ R$")

            for item in itens:
                if (firstItemInput == item.name):
                    item.setBalance(float(valueInput), firstItemBalanceType) 
                elif (secondItemInput == item.name):
                    item.setBalance(float(valueInput), secondItemBalanceType)                

        elif (option == 2): # Temporary
            for item in itens:
                print(item.name)
                print(item.itemType)
                print(item.balance)
                print("\n")
            
            print(calculateBalance.accountingEquation(itens))

            exit()