import interpret_stdlib

var = {}
functions = {}

def interpret(line, mode, name):
    # find tokens and execute them
    if mode == 1:
        line = functions_process(line, 2)
        functions[name] = functions[name] + ":" + line
        if line.startswith("}"):
            mode = 2
            return mode
        else:
            return
    else:
        if line.startswith("#"):
            return
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
                try:
                    eval(value)
                except Exception as e:
                    pass
                var[varname] = value
        elif line.startswith("func"):
            functions_process(line)
        else:
            interpret_stdlib.interpret_stdlib(line, var, 1)

def functions_process(line):
        if line.startswith("func"):
            line = line.replace("func ", "")
            line = line.replace(" ", "")
            line= line.replace("{", "")
        return line


def unpack_function():
    pass
