""" Contains methods for converting a string to a tree. """
from BoolTree import SimpleNode, InverseNode, AndNode, OrNode

VARIABLES = ['A', 'B', 'C', 'D', 'E']
OPERATORS = ['.', '+']
INVERSE = '¬'

def validate_string(input_string):
    """ Determines whether a given string is in a convertable format. """
    valid = True    # Innocent until proven guilty
    brack_count = 0 # Number of open brackets
    has_var = False # Determine whether expression has a variable

    try:
        i = 0
        while i < len(input_string):
            # print("Last Valid Symbol was {} - At position {}".format(input_string[i], i))
            if input_string[i] is '(':          # Validate Brackets
                brack_count = brack_count + 1
            elif input_string[i] is ')':
                if brack_count == 0:
                    # No starting brackets
                    valid = False
                    break
                else:
                    brack_count = brack_count - 1
            elif input_string[i] is INVERSE:    # Validate Inverse
                if input_string[i+1] in ([INVERSE, ')'] + OPERATORS):
                    # Inverse has nothing after it.
                    valid = False
                    break
            elif input_string[i] in OPERATORS:  # Validate Operators
                if (i is 0) or (i is (len(input_string) -1)):
                    # Nothing before an operator
                    valid = False
                    break
                elif input_string[i-1] not in ([')'] + VARIABLES):  
                    # Invalid symbol before operator
                    valid = False
                    break
                elif input_string[i+1] not in (['(', INVERSE] + VARIABLES):
                    # Invalid symbol following operator
                    valid = False
                    break
            elif (input_string[i] in VARIABLES):   # Validate variables
                has_var = True
                if len(input_string) is not 1:
                    # This is not the only symbol in the string
                    if (i is 0) or (i < len(input_string) - 2):
                        # This is the first symbol or a symbol in the middle so check RHS
                        if input_string[i + 1] in (['(', INVERSE] + VARIABLES):
                            # Followed by an invalid symbol
                            valid = False
                            break
                    if (i is (len(input_string) - 1)) or (i > 0):
                        # This is at the end or in the middle so check LHS
                        if input_string[i - 1] in ([')'] + VARIABLES):
                            # Preceeded by an invalid symbol
                            valid = False
                            break
            i = i + 1
    except Exception:   # Unknown exception
        valid = False
    
    if brack_count != 0:
        # Brackets are unbalanced.
        valid = False;
    elif not has_var:
        # No variables
        valid = False
    
    return valid

def convert_clause(clause):
    """ Identifies next nodes to be generated. Assumes clause has been validated."""
    node = None
    if clause[0] in VARIABLES:   # Is it a variable?
        if len(clause) == 1:        # Is it just a variable?
            node = SimpleNode(clause[0])
        else:                
            # What's next?
            if clause[1] is '.':  # It's an AND
                rhs_node = convert_clause(clause[2:])    # Get the right hand side node of this AND
                node = AndNode(SimpleNode(clause[0]), rhs_node)
            elif clause[1] is '+':  # It's an OR
                rhs_node = convert_clause(clause[2:])    # Get the right hand side node of this OR
                node = OrNode(SimpleNode(clause[0]), rhs_node)
    elif clause[0] is INVERSE:                  # Inverse operation
        # Find end of next statement
        i = 1
        if len(clause) > 2:     # Is the LHS of a clause.
            open_cnt = 0
            while i < len(clause):
                if clause[i] is '(':
                    open_cnt = open_cnt + 1
                elif clause[i] is ')':
                    open_cnt = open_cnt - 1
                elif (clause[i] in OPERATORS) and (open_cnt == 0):
                    lhs_node = InverseNode(convert_clause(clause[1:i]))
                    # What's next?
                    if clause[1] is '.':  # It's an AND
                        rhs_node = convert_clause(clause[i+1:])    # Get the right hand side node of this AND
                        node = AndNode(lhs_node, rhs_node)
                        break
                    elif clause[1] is '+':  # It's an OR
                        rhs_node = convert_clause(clause[i+1:])    # Get the right hand side node of this OR
                        node = OrNode(lhs_node, rhs_node)
                        break
                i = i + 1
            node = InverseNode(convert_clause(clause[1:i]))
        else:                   # Inverse of a variable.
            node = InverseNode(SimpleNode(clause[1]))
    elif clause[0] is '(':       # Brackets
        i = 1
        open_cnt = 0
        while i < len(clause):
            if clause[i] == '(':
                open_cnt = open_cnt + 1
            elif clause[i] == ')':
                if open_cnt > 0:
                    open_cnt = open_cnt - 1
                
                if open_cnt == 0:       # Found the end
                    # Get LHS
                    lhs_node = convert_clause(clause[1:i])

                    # Now the rest
                    if i + 1 == len(clause):                            # The bracket is the end of the clause.
                        node = lhs_node                    
                    elif clause[i+1] is '.':  # It's an AND
                        rhs_node = convert_clause(clause[i+2:])     # Get the right hand side node of this AND
                        node = AndNode(lhs_node, rhs_node)
                    elif clause[i+1] is '+':  # It's an OR
                        rhs_node = convert_clause(clause[i+2:])     # Get the right hand side node of this OR
                        node = OrNode(lhs_node, rhs_node)
                    break
            i = i + 1
    return node


#test = '(A.B)+(C.A)'
#print("Is the string valid? {}".format(validate_string(test)))

#nde = convert_clause(test)
#inp = {
#    'A': True,
#    'B': False,
#    'C': False
#}
#print("Is the string true given {}? {}".format(inp, nde.evaluate(inp)))