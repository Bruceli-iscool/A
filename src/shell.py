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
            mode, name = interpret.functions_process(userinput)
            mode = mode
            if '{' in userinput:
                detect = True
                interpret.interpret(userinput, 1, name)
            elif '}' in userinput:
                detect = False
            elif detect:
                interpret.interpret(userinput, 1, name)
            else:
                interpret.interpret(userinput, 0, 0)

