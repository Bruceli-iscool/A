import interpret

def shell():
    while True:
        userinput = input(">>")
        if userinput == "exit()":
            break
        else:
            interpret.interpret(userinput)
