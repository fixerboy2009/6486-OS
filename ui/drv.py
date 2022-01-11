# GPU thing idk
path = "../DRIVER"
import os.path

def getDriver(dr):
    if os.path.exists(f"{path}/{str(dr)}") == True:
        return f"{path}/{str(dr)}"
    else:
        return False

class drv:
    def __init__(self, drvType) -> None:
        if getDriver(drvType) != False:
            return getDriver(drvType)