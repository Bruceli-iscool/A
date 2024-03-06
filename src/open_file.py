import interpret

def open_file(filename):
    with open(filename) as file:
        for line in file:
            interpret.interpret(line)