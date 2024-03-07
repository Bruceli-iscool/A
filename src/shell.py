import interpret


def shell():
    print(
        "Welcome to the interactive interpreter.\nType a command to see the result instantly."
    )
    while True:
        userinput = input(">>")
        if userinput == "exit()":
            break
        elif len(userinput) < 1:
            pass
        else:
            interpret.interpret(userinput)
