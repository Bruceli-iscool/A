import interpret

def open_file(filename):
    with open(filename) as file:
        for line in file:
            interpret.interpret(line)
open_file('/workspaces/A/examples/add.a')