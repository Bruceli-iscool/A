import statistics
import paren


def interpret(line):
    # find tokens and execute them
    if line.startswith("return"):
        line = line.lstrip('return ')
        if ';' not in line:
            print("a: An error occured: missing a ';'")
        line = line.rstrip(';')
interpret('return 5')