import interpret
import sys

def shell():
    print(
        "Welcome to the interactive interpreter.\nType a command to see the result instantly.\nexit() to exit the .test shell, q() to leave the A interpreter."
    )
    while True:
        userinput = input(">>")
        if userinput == "exit()":
            break
        elif userinput == "q()":
            sys.exit()
        elif len(userinput) < 1:
            pass
        else:
            interpret.interpret(userinput)
