import os

from services.table import Table

DIRECTORY_NAME = "files"

class File:
    
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

    def writeTransaction(self, fileName: str, transation: str) -> None:
        """ Write the transaction in the file.

        Parameters
        -----------
        fileName: :class:`str`
            File name.
        transation: :class:`str`
            Transation... 
        """
        
        with open(f'{DIRECTORY_NAME}/{fileName}', "a") as f:
            f.write(transation)

    def writeTable(self, fileName: str) -> None:
        """ Write the table in the file.

        Parameters
        -----------
        fileName: :class:`str`
            File name.
        transation: :class:`str`
            Transation... 
        """
        
        table = Table()

        table.writeTableHeader(fileName)