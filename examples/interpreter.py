""" Contains methods for interpreting .cnf files. """
def _convert_line(line):
    """ Converts the given line into a clause. """
    line = line.replace('-', '¬') # Replace all minuses with inversion operators
    line = line[:-3]
    line = line.replace(' ', '+') # Replace all spaces with OR operators
    # Ensure variables are wrapped in curlies
    prev_num = False
    new_str = ""
    cnt = 0
    for c in line:
        if c.isdigit():
            if not prev_num:    # Need the opening to a variable.
                new_str = new_str + "{" + str(c)
                prev_num = True
            else:
                new_str = new_str + c # Add digit
        else:
            if prev_num:
                new_str = new_str + "}" + c # Close off variable
            else:
                new_str = new_str + c
            prev_num = False
        cnt = cnt + 1

    # All strings end on a number
    new_str = new_str + "}"
    return new_str


def _get_variables(max):
    """ Returns an array of available variables. """
    vars = []
    v = 1
    while v <= max:
        vars.append("{" + str(v) + "}") # Variables are strings
        v = v + 1
    return vars

def interpret_file(file_name):
    """ Interprets the file into a single formula along with the variables present. """
    clauses = []
    vars = []
    equation = ""
    with open(file_name, mode='r') as cnf_file: # Extract each clause from the 
        for line in cnf_file:
            if line[0] == 'c':  # This is a comment
                pass
            elif line[0] == 'p':    # This determines the number of variables and clauses.
                contents = line.split(' ')
                vars = _get_variables(int(contents[2]))  # Variables are numbers up to the max.
            else:
                new_clause = _convert_line(line)
                # DEBUG: print("Extracted Clause: {}".format(new_clause))
                clauses.append(new_clause)
                
    # Now combine the clauses into a single formula
    i = 0
    for c in clauses:
        if i is 0:
            equation = "({})".format(c)
        else:
            equation = equation + ".({})".format(c)
        i = i + 1

    return (equation, vars)