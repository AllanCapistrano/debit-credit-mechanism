from shell import init, options
from services.calculateBalance import CalculateBalance
from services.file import File

TRANSACTIONS_FILE = "transactions.txt"
BALANCE_SHEET = "balance_sheet.txt"

itens = []

if __name__ == "__main__":
    itens = init()

    file = File()

    # Creating files
    file.createFile(TRANSACTIONS_FILE)
    file.createFile(BALANCE_SHEET)

    calculateBalance = CalculateBalance()

    count = 0
    
    while (True):
        option = options()

        if (option == 3):
            print("\n> Até mais!")

            exit()
        elif (option == 1):
            print("\n> Digite o primeiro item da transação:")
            firstItemInput = input("$ ")

            print("Digite o tipo do saldo do primeiro item [(C)redor, (D)evedor]:")
            firstItemBalanceType = input("$ ")

            if (firstItemBalanceType == "d" or firstItemBalanceType == "devedor"):
                secondItemBalanceType = "credor"
            else:
                secondItemBalanceType = "devedor"

            print("> Digite o segundo item da transação:")
            secondItemInput = input("$ ")

            print("> Digite o valor da transação:")
            valueInput = input("$ R$")

            if (firstItemBalanceType == "c"):
                firstItemBalanceType = "credor"
            elif (firstItemBalanceType == "d"):
                firstItemBalanceType = "devedor"

            transaction = f"{count + 1}ª operação - {firstItemInput} saldo " + \
            f"{firstItemBalanceType} | {secondItemInput} saldo " +\
            f"{secondItemBalanceType} | valor R${valueInput}"

            # Write the transaction
            file.writeTransaction(TRANSACTIONS_FILE, transaction)

            for item in itens:
                if (firstItemInput == item.name):
                    item.setBalance(float(valueInput), firstItemBalanceType) 
                elif (secondItemInput == item.name):
                    item.setBalance(float(valueInput), secondItemBalanceType)

            count += 1

        elif (option == 2): # Temporary
            for item in itens:
                print(item.name)
                print(item.itemType)
                print(item.balance)
                print("\n")
            
            print(calculateBalance.accountingEquation(itens))

            file.writeTable(BALANCE_SHEET)

            exit()