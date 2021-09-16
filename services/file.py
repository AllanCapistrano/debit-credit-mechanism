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

        f = open(fileName, "w")

        f.close()

    def writeTransations(self, fileName: str, transation: str) -> None:
        """ Write the transation in the file.

        Parameters
        -----------
        fileName: :class:`str`
            File name.
        transation: :class:`str`
            Transation... 
        """
        
        with open(fileName, "a") as f:
            f.write(transation)