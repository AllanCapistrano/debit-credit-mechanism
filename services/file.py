import os

from services.table import Table
from services.calculateBalance import CalculateBalance

DIRECTORY_NAME = "files"

class File:

    def __writer__(self, fileName: str, text: str) -> None:
        """ Write text in the file

        Parameters
        -----------
        fileName: :class:`str`
            File name.
        text: :class:`str`
            Text that will be written .
        """
        
        with open(f'{DIRECTORY_NAME}/{fileName}', "a") as f:
            f.write(text + "\n")
    
    def createFile(self, fileName: str) -> None:
        """ Create a file

        Parameters
        -----------
        fileName: :class:`str`
            File name.
        """
        
        # If file name does not have .txt
        if (fileName.lower().find(".txt") == -1):
            fileName += ".txt"

        # Create a directory if not exists.
        if(not os.path.isdir(DIRECTORY_NAME)):
            os.makedirs(f'{DIRECTORY_NAME}')

        f = open(f'{DIRECTORY_NAME}/{fileName}', 'w')

        f.close()

    def writeTransaction(self, fileName: str, transaction: str) -> None:
        """ Write the transaction in the file.

        Parameters
        -----------
        fileName: :class:`str`
            File name.
        transaction: :class:`str`
            Ongoing transaction.
        """

        self.__writer__(fileName, transaction)

    def writeTable(self, fileName: str, itens: list) -> None:
        """ Write the table in the file.

        Parameters
        -----------
        fileName: :class:`str`
            File name.
        itens: :class:`list`
            List of itens
        """
        
        self.__writeTableHeader__(fileName)
        self.__writeTableBody__(fileName, itens)

    def __writeTableHeader__(self, fileName: str) -> None:
        """ Write the table header in the file.

        Parameters
        -----------
        fileName: :class:`str`
            File name.
        """

        table = Table()

        self.__writer__(fileName, table.makeLine())
        self.__writer__(fileName, table.makeTitle())
        self.__writer__(fileName, table.makeLine())
        self.__writer__(fileName, table.makeFirstRow())
        self.__writer__(fileName, table.makeLine(1))
        self.__writer__(fileName, table.makeSecondRow())
        self.__writer__(fileName, table.makeLine(2))

    def __writeTableBody__(self, fileName: str, itens: list) -> None:
        """ Write the table body in the file.

        Parameters
        -----------
        fileName: :class:`str`
            File name.
        itens: :class:`list`
            List of itens
        """
        
        table = Table()
        calculateBalance = CalculateBalance()
        totalBalance = calculateBalance.totalBalance(itens)

        for item in itens:
            self.__writer__(fileName, table.makeBody(item))
            self.__writer__(fileName, table.makeLine(2))

        # Make the total row.
        self.__writer__(fileName, table.makeTotal(totalBalance))
        self.__writer__(fileName, table.makeLine())