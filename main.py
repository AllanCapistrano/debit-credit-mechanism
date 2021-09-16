from shell import init, options

itens = []

if __name__ == "__main__":
    itens = init()
    
    while (True):
        option = options()

        if (option == 3):
            print("\n> Até mais!")

            exit()
        elif (option == 1):
            print("\n> Digite o primeiro item e o seu tipo de saldo [(C)redor/(D)evedor]:")
            firstItemInput = input("$ ")

            print("> Digite o segundo item e o seu tipo de saldo [(C)redor/(D)evedor]:")
            secondItemInput = input("$ ")

            print("> Digite o valor do item:")
            valueInput = input("$ R$")

            temp = firstItemInput.lower().split(" ")
            temp1 = secondItemInput.lower().split(" ")

            for item in itens:
                if (temp[0] == item.name):                    
                    item.setBalance(float(valueInput), temp[1]) 
                elif (temp1[0] == item.name):                    
                    item.setBalance(float(valueInput), temp1[1])                

        elif (option == 2): # Temporary
            for item in itens:
                print(item.name)
                print(item.itemType)
                print(item.balance)

            exit()