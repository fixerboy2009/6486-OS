# 6486-OS

## About
A messy, CLI based *os (not really)* program, writtin in python.

## Writing code
ATM there is no way to write code while IN the CLI, you have to write it outside of the CLI
### Functions given
1. wait(sec: int) -> None
2. getTime() -> float
3. network_getrequest(url: str) -> Request
4. network_getstatuscode(request: Request) -> int

## Running programs and games
In the shell (UI disabled), theres a command that gives you the ability to run programs in the home directory, no need to put in the ".6486" extension while inputting the file name
### Games
List of built in games:
1. Number guesser (games/randomNumber)
#### Running them
To run a game, type "games/[gamename]" in runProgram and bam!
