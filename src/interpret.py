import interpret_stdlib

var = {}


def interpret(line):
    # find tokens and execute them
    if line.startswith("#"):
        pass
    elif line.startswith("echo") and "#" not in line:
        line = line.lstrip("echo ")
        for key, value in var.items():
            line = line.replace(str(key), str(value))
        # eventually I will remove the '' and "" from input
        if ";" not in line:
            print("a: An error occured: missing a ';'")
        else:
            try:
                line = line.replace(";", "")
                print(eval(line))
            except Exception as e:
                line = line.replace(";", "")
                line = interpret_stdlib.interpret_stdlib(line, var, 2)
                print(line)
    elif "=" in line and "#" not in line:
        line = line.replace(" ", "")
        varname, value = line.split("=")
        if ";" not in line:
            print("a: An error occured: Expected ';'")
        else:
            value = value.replace(";", "")
            value = interpret_stdlib.interpret_stdlib(value, var, 2)
            var[varname] = value
    else:
        interpret_stdlib.interpret_stdlib(line, var, 1)
