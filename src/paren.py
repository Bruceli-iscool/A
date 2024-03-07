def open_paren(userinput):
    if '(' in userinput:
        userinput = userinput.lstrip('(')
        userinput = userinput.rstrip(')')
        return eval(userinput)
