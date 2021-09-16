from item import Item

class CalculateBalance:
    def total(self, item: Item) -> float:
        """ Calculate the total value of an item.

        Parameters
        -----------
        item: :class:`Item`
            Item to calculate the total.

        Returns
        -----------
        total: :class:`float`
        """

        if (item.itemType == "ativo"):
            return item.balance[0] - item.balance[1]
        
        return item.balance[1] - item.balance[0]

    def accountingEquation(self, itens: list) -> float:
        """ Calculation of Accounting Equation

        Assets = (Liabilities + Shareholder’s Equity)

        Parameters
        -----------
        itens: :class:`list`
            List of itens

        Returns
        -----------
        total: :class:`float`
        """
        
        asset = 0
        liability = 0
        shareholderEquity = 0

        for item in itens:
            if (item.itemType == "ativo"):
                asset += self.total(item)
            elif(item.itemType == "passivo"):
                liability += self.total(item)
            elif(item.itemType == "patrimônio líquido"):
                shareholderEquity += self.total(item)

        if (asset == liability + shareholderEquity):
            return asset

        return None