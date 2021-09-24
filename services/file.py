import os

from services.table import Table

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
            Transation... 
        """

        self.__writer__(fileName, transaction)

    def writeTable(self, fileName: str) -> None:
        """ Write the table in the file.

        Parameters
        -----------
        fileName: :class:`str`
            File name.
        transation: :class:`str`
            Transation... 
        """
        
        self.__writeTableHeader__(fileName)


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

