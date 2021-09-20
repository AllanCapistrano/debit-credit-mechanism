DIRECTORY_NAME = "files"
NUMBER_OF_CHARACTERS = 80
TABLE_TITLE = "Balancete de verificação"
BARS_POSITIONS = [52, 64]

class Table:

    def writeTableHeader(self, fileName: str) -> None:
        """ Write the table header in the file.

        Parameters
        -----------
        fileName: :class:`str`
            File name.
        """
        
        self.__writeLine__(fileName)
        self.__writeTitle__(fileName)
        self.__writeLine__(fileName)
        self.__writeFirstRow__(fileName)
        self.__writeLine__(fileName, 1)
        self.__writeSecondRow__(fileName)
        self.__writeLine__(fileName, 2)

    def __writeLine__(self, fileName: str, num: int = 0) -> None:
        """ Write the table line in the file.

        Parameters
        -----------
        fileName: :class:`str`
            File name.
        num: :class:`int`
            Number of vertical bars.
        """

        line = "+"
            
        if (num == 0):
            for x in range(NUMBER_OF_CHARACTERS - 2):
                line += "-"

        elif (num == 1):
            line = "+"

            for x in range(NUMBER_OF_CHARACTERS - 3):
                if (x == BARS_POSITIONS[0]):
                    line += "|"

                line += "-"
            
        elif (num == 2):
            line = "+"

            for x in range(NUMBER_OF_CHARACTERS - 4):
                if (x == BARS_POSITIONS[0] or x == BARS_POSITIONS[1]):
                    line += "|"

                line += "-"
            
        line += "+"
        
        with open(f'{DIRECTORY_NAME}/{fileName}', "a") as f:
            f.write(line)
            f.write("\n")

    def __writeTitle__(self, fileName: str) -> None:
        """ Write the table title in the file.

        Parameters
        -----------
        fileName: :class:`str`
            File name.
        """

        line = f"|{TABLE_TITLE}"

        for x in range((NUMBER_OF_CHARACTERS - 2) - (len(TABLE_TITLE))):
            line += " "
        
        line += "|"

        with open(f'{DIRECTORY_NAME}/{fileName}', "a") as f:
            f.write(line)
            f.write("\n")

    def __writeFirstRow__(self, fileName: str) -> None:
        """ Write the table first row in the file.

        Parameters
        -----------
        fileName: :class:`str`
            File name.
        """
        
        with open(f'{DIRECTORY_NAME}/{fileName}', "a") as f:
            f.write("|Contas                                              |Saldos                   |")
            f.write("\n")

    def __writeSecondRow__(self, fileName: str) -> None:
        """ Write the table second row in the file.

        Parameters
        -----------
        fileName: :class:`str`
            File name.
        """

        with open(f'{DIRECTORY_NAME}/{fileName}', "a") as f:
            f.write("|                                                    |Devedor     |Credor      |")
            f.write("\n")