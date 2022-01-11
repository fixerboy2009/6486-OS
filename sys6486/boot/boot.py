print("[ 6486 OS: CLI ]: Loading CLI UI...")
CLIUIEnabled = False
print("[ 6486 OS: CLI ]: CLI UI is disabled, using CLI without UI")
import time
import requests
from flask import Flask
from libraries.fs import FileSystem

WELCOME_MSG = "Welcome traveler!\nYour here because you saw a random github repo, or you hacked my computer and downloaded my files.\nEither way, have fun! Documentation and how to write code is in readme.md\nGoodbye!"

# Program runners

def PROGRAM_GETTIME() -> float:
    return time.time()

def PROGRAM_NETWORKING_GETREQUEST(URL: str) -> requests.Request:
    return requests.get(str(URL))

def PROGRAM_NETWORKING_GERREQUESTSTATUSCODE(REQUEST: requests.Request) -> int:
    return REQUEST.status_code

def PROGRAM_NETWORKING_STARTFLASKFROMHTMLFILE(FILE: str):
    print("STARTING FLASK FROM HTML")
    app = Flask(__name__)
    @app.route("/")
    def CREATE_HOME():
        st = ""
        with open(FILE, 'r') as f:
            lines = f.readlines()
            for line in lines:
                st = st + line
        return st

def PROGRAM_PROGRAMMING_EXECUTESTRING(CODE: str):
    ProgramArgs = {
        "wait": time.sleep,
        "getTime": PROGRAM_GETTIME,
        "network_getrequest": PROGRAM_NETWORKING_GETREQUEST,
        "network_flask_startfromhtmlfile": PROGRAM_NETWORKING_STARTFLASKFROMHTMLFILE,
        "network_getstatuscode": PROGRAM_NETWORKING_GERREQUESTSTATUSCODE,
        "fileSystem": FileSystem,
        "loadcode": PROGRAM_PROGRAMMING_EXECUTESTRING,
        "programming_getglobalfunctions": PROGRAM_PROGRAMMING_GETGLOBALFUNCTIONS
    }
    exec(CODE, ProgramArgs)

def PROGRAM_PROGRAMMING_GETGLOBALFUNCTIONS():
    ProgramArgs = {
        "wait": time.sleep,
        "getTime": PROGRAM_GETTIME,
        "network_getrequest": PROGRAM_NETWORKING_GETREQUEST,
        "network_flask_startfromhtmlfile": PROGRAM_NETWORKING_STARTFLASKFROMHTMLFILE,
        "network_getstatuscode": PROGRAM_NETWORKING_GERREQUESTSTATUSCODE,
        "fileSystem": FileSystem,
        "loadcode": PROGRAM_PROGRAMMING_EXECUTESTRING,
        "programming_getglobalfunctions": PROGRAM_PROGRAMMING_GETGLOBALFUNCTIONS,
    }
    return ProgramArgs

ProgramArgs = {
    "wait": time.sleep,
    "getTime": PROGRAM_GETTIME,
    "network_getrequest": PROGRAM_NETWORKING_GETREQUEST,
    "network_flask_startfromhtmlfile": PROGRAM_NETWORKING_STARTFLASKFROMHTMLFILE,
    "network_getstatuscode": PROGRAM_NETWORKING_GERREQUESTSTATUSCODE,
    "fileSystem": FileSystem,
    "loadcode": PROGRAM_PROGRAMMING_EXECUTESTRING,
    "programming_getglobalfunctions": PROGRAM_PROGRAMMING_GETGLOBALFUNCTIONS,
}

def runFile(file: str):
    runner = "sys6486/runner.6486"
    with open(runner, 'r') as f:
        lines = f.readlines()
        st = ""
        for line in lines:
            st = st + line
        exec(st, {
            "FTR": file,
            "FTR_G": ProgramArgs
        })

print(WELCOME_MSG)
runFile("sys6486/shell.6486")