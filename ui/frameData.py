# Frame data module, used in the main file to update the display
class frameData:
    def __init__(self, title, lines):
        self.lines = lines
        self.title = title

    def changeTitle(self, title):
        self.title = title

    def changeLine(self, lineNum, data):
        self.lines[lineNum] = data

    def getTitle(self):
        return self.title

    def getLines(self):
        return self.lines