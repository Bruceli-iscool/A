import interpret

def shell():
    while True:
        userinput = input(">>")
        if userinput == "exit()":
            break
        elif len(userinput) < 1:
            pass
        else:
            interpret.interpret(userinput)
