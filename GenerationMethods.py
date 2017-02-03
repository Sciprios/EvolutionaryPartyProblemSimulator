""" Contains methods for converting a string to a tree. """
from BoolTree import SimpleNode, InverseNode, AndNode, OrNode

def convert_clause(clause):
    """ Identifies next nodes to be generated. Assumes clause has been validated."""
    node = None
    print(clause)
    if clause[0] in ['A', 'B', 'C', 'D', 'E']:   # Is it a variable?
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
    elif clause[0] is '¬':                  # Inverse operation
        rhs_node = convert_clause(clause[1:])
        node = InverseSimple(rhs_node)
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
                    break;
            i = i + 1
    return node

test = '(A.B)+(C.A)+(B.B)'
nde = convert_clause(test)
print(nde.evaluate({'A': False, 'B': True, 'C': False}))