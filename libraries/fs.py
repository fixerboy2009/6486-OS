class FileSystem:
    def __init__(self) -> None:
        pass

    def newFile(self, filePath: str, data: str, name: str):
        with open(f"{filePath}/{name}", 'w') as f:
            f.writelines(data)
            f.close()