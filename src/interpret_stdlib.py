import statistics

def interpret_stdlib(line, varnames):
    """Interpret stdlib functions"""
    if line.startswith("math."):
        # math libary
        line = line.lstrip("math.")
        if line.startswith("println."):
            line = line.lstrip("println.")
            if line.startswith("solve("):
                line = line.replace("solve(", "")
                line = line.replace(")", "")
                line = line.replace(" ", "")
                for key, value in varnames.items():
                    line = line.replace(str(key), (value))
                if ';' not in line:
                    print("a: An error occured: Expected ';'")
                else:
                    print(eval(line))
            elif line.startswith("sum("):
                line = line.lstrip("sum(")
                line = line.replace(")", "")
                strline = line.replace(" ", "")
                for key, value in varnames.items():
                    strline = strline.replace(str(key), (value))
                if ';' not in line:
                    print("a: An error occured: Expected ';'")
                else:
                    strline = strline.replace(';', "")
                    if '+' in strline and '-' and '*' and '/' and '%' not in strline:
                        print(eval(strline))
                    else:
                        print("a: An error occured: Unsupported operation")
            elif line.startswith("sub("):
                line = line.lstrip("sum(")
                line = line.replace(")", "")
                line = line.replace(" ", "")
                for key, value in varnames.items():
                    line = line.replace(str(key), str(value))
                if ';' not in line:
                    print("a: An error occured: Expected ';'")
                else:
                    line = line.replace(';', "")
                    if '-' in line and '+' and '*' and '/' and '%' not in line:
                        print(eval(line))
                    else:
                        print("a: An error occured: Unsupported operation")
            elif line.startswith("product("):
                line = line.lstrip("product(")
                line = line.replace(")", "")
                line = line.replace(" ", "")
                for key, value in varnames.items():
                    line = line.replace(str(key), str(value))
                if ';' not in line:
                    print("a: An error occured: Expected ';'")
                else:
                    line = line.replace(';', "")
                    if '*' in line and '+' and '-' and '/' and '%' not in line:
                        print(eval(line))
                    else:
                        print("a: An error occured: Unsupported operation")
            elif line.startswith("quotient("):
                line = line.lstrip("quotient(")
                line = line.replace(")", "")
                line = line.replace(" ", "")
                for key, value in varnames.items():
                    line = line.replace(str(key), str(value))
                if ';' not in line:
                    print("a: An error occured: Expected ';'")
                else:
                    line = line.replace(';', "")
                    if '/' in line and '+' and '-' and '*' and '%' not in line:
                        print(eval(line))
                    else:
                        print("a: An error occured: Unsupported operation")

    elif line.startswith("string."):
        # string libary
        line = line.lstrip("string.")
        if line.startswith("newline()"):
            print('\n')
    elif line.startswith("statistics."):
        # statistics libary
        pass
    else:
        print("a: An error occured: Unknown Identifier")
