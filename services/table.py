DIRECTORY_NAME = "files"
NUMBER_OF_CHARACTERS = 80
TABLE_TITLE = "Balancete de verificação"
BARS_POSITIONS = [52, 64]
FIRST_ROW_COLUMS = ["Contas", "Saldos"]
FISRT_COLUMN_LENGTH = 52
SECOND_ROW_COLUMS = ["Devedor", "Credor"]
SECOND_COLUMN_LENGTH = [12, 12]

class Table:

    def makeLine(self, num: int = 0) -> str:
        """ Make table line.

        Parameters
        -----------
        fileName: :class:`str`
            File name.
        num: :class:`int`
            Number of vertical bars.

        Returns
        -----------
        line: :class:`str`
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

        return line

    def makeTitle(self) -> str:
        """ Make table title.

        Parameters
        -----------
        fileName: :class:`str`
            File name.
        num: :class:`int`
            Number of vertical bars.

        Returns
        -----------
        title: :class:`str`
        """

        title = f"|{TABLE_TITLE}"

        for x in range((NUMBER_OF_CHARACTERS - 2) - (len(TABLE_TITLE))):
            title += " "
        
        title += "|"

        return title

    def makeFirstRow(self) -> str:
        """ Make table first row.

        Parameters
        -----------
        fileName: :class:`str`
            File name.
        num: :class:`int`
            Number of vertical bars.

        Returns
        -----------
        firstRow: :class:`str`
        """

        if (
            FISRT_COLUMN_LENGTH > len(FIRST_ROW_COLUMS[0]) and 
            (SECOND_COLUMN_LENGTH[0] + SECOND_COLUMN_LENGTH[1] + 1) > 
            len(FIRST_ROW_COLUMS[1])
        ):
            firstRow = f"|{FIRST_ROW_COLUMS[0]}"

            for x in range(FISRT_COLUMN_LENGTH - len(FIRST_ROW_COLUMS[0])):
                firstRow += " "

            firstRow += f"|{FIRST_ROW_COLUMS[1]}"

            for x in range(
                (SECOND_COLUMN_LENGTH[0] + SECOND_COLUMN_LENGTH[1] + 1) - 
                len(FIRST_ROW_COLUMS[1])
                ):
                firstRow += " "

            firstRow += "|"

            return firstRow
        else:
            print("Erro ao definir FIRST_ROW_COLUMS!")
            exit()

    def makeSecondRow(self) -> str:
        """ Make table second row.

        Parameters
        -----------
        fileName: :class:`str`
            File name.
        num: :class:`int`
            Number of vertical bars.

        Returns
        -----------
        secondRow: :class:`str`
        """

        if (
            SECOND_COLUMN_LENGTH[0] >= len(SECOND_ROW_COLUMS[0]) and 
            SECOND_COLUMN_LENGTH[1] >= len(SECOND_ROW_COLUMS[1])
        ):
            secondRow = "|"

            for x in range(FISRT_COLUMN_LENGTH):
                secondRow += " "

            secondRow += f"|{SECOND_ROW_COLUMS[0]}"

            for x in range(SECOND_COLUMN_LENGTH[0] - len(SECOND_ROW_COLUMS[0])):
                secondRow += " "

            secondRow += f"|{SECOND_ROW_COLUMS[1]}"

            for x in range(SECOND_COLUMN_LENGTH[1] - len(SECOND_ROW_COLUMS[1])):
                secondRow += " "

            secondRow += "|"

            return secondRow
        else:
            print("Erro ao definir SECOND_ROW_COLUMS!")
            exit()