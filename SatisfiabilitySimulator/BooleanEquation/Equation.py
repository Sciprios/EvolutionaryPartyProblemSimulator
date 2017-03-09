from BooleanNode import BooleanNode

class Equation(BooleanNode):
    """ Used to analyse an equation. """
    
    def __init__(self, input_string):
        """ Initialises an eqaution by interpreting the input string. """
        self._unparsed_equation = None
        self._clauses = []
        self._set_unparsed_equation(input_string)
        self.generate_clauses()

    
    def _validate_string(self, eq_str):
        """ Validates the input string for this equation. """
        valid = True
        brack_count = 0
        in_var = False
        i = 0
        # Only brackets and operators allowed not in a clause
        for symbol in eq_str:
            if symbol is '{': # Start of a variable
                if in_var:
                    valid = False
                    break
                if brack_count is 0:
                    valid = False
                    break
                if i > 0:
                    if eq_str[i-1] not in ['.', '+', '(', '¬']: # Check the previous symbol is good to be next to.
                        valid = False
                        break
                in_var = True
            elif symbol is '}': # End of variable
                if not in_var:
                    valid = False
                    break
                if i < (len(eq_str) - 1):
                    if eq_str[i+1] not in ['.', '+', ')']: # Check the next symbol is good to be next to.
                        valid = False
                        break
                in_var = False
            elif symbol in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                if not in_var:
                    valid = False
                    break
            elif symbol is ')':     # Brackets must be balanced
                if in_var:
                    valid = False
                    break
                if brack_count is 0:
                    valid = False
                    break
                else:
                    brack_count = brack_count - 1
            elif symbol is '(':
                if in_var:
                    valid = False
                    break
                brack_count = brack_count + 1
            elif symbol in ['+', '.']:  # Must have either a clause or variable next to it.
                if in_var:
                    valid = False
                    break
                if i is (len(eq_str) - 1):   # Is it the last character
                    valid = False
                    break
                elif i is 0:    # An operator cannot be the first item
                    valid = False
                    break
                if (eq_str[i+1] is not '{') and (eq_str[i+1] not in ['(', '¬']):
                    valid = False
                    break
                elif (eq_str[i-1] is not '}') and (eq_str[i-1] not in [')']):
                    valid = False
                    break
                if brack_count is 0:    # Cannot combine clauses using OR
                    if symbol is '+':
                        valid = False
                        break
            elif symbol is '¬':
                if in_var:
                    valid = False
                    break
                if i is (len(eq_str) - 1):  # Cannot be the last item
                    valid = False
                    break
                if eq_str[i+1] is not '{':
                    valid = False
                    break
            i = i + 1
        
        if brack_count is not 0:
            valid = False

        return valid
    
    def generate_clauses(self):
        """ Creates a clause array from the _unparsed_equation attribute. """
        bracket_index = 0
        bracket_count = 0
        i = 0
        for symbol in self._unparsed_equation:
            if symbol is '(':
                if bracket_count is 0:
                    bracket_index = i   # We have found a new clause.
                bracket_count = bracket_count + 1
            elif symbol is ')':
                bracket_count = bracket_count - 1
                if bracket_count is 0:  # Have we found the end to a clause?
                    new_clause = self._generate_clause(self._unparsed_equation[bracket_index+1:i])  # Only want to parse string not including brackets.
                    self._clauses.append(new_clause)
            i = i + 1
    
    def _generate_clause(self, clause):
        """ Generates an initial node for a clause. This method assumes "clause" is validated. """
        node = None
        #print(clause)
        if clause[0] is '{':  # First items a VariableNode
            cnt = 0
            while cnt < len(clause):    # Get the end of the variable
                if clause[cnt] is '}':
                    break
                cnt = cnt + 1
            nde = VariableNode(clause[0:cnt + 1])
            if len(clause) is not cnt + 1:
                if clause[cnt + 1] in ['.', '+']: # If there's more to this clause deal with it
                    rhs = self._generate_clause(clause[cnt + 2:]) # Generate the rhs
                    if clause[cnt + 1] is '.':
                        return AndNode(nde, rhs)    # It's an AND combination
                    else:
                        return OrNode(nde, rhs)     # It's an OR combination
            else:
                return nde  # This is just a variable
        elif clause[0] is '¬':  # Found an inversion
            i = 0
            while i < len(clause) - 1:
                if clause[i+1] in ['.', '+']:
                    lhs = InversionNode(self._generate_clause(clause[1:i+1]))   # Inverted part
                    rhs = self._generate_clause(clause[i+2:])   # Bit after inversion
                    if clause[i+1] is '.':
                        return AndNode(lhs, rhs)
                    else:
                        return OrNode(lhs, rhs)
                i = i + 1
            # Haven't found an operator so we will assume its a single clause
            return InversionNode(self._generate_clause(clause[1:]))
                
    def evaluate(self, input_vector):
        """ Evaluates the CNF equation through AND'ing the clauses. """
        if False in self.get_clause_evaluation(input_vector):
            return False
        else:
            return True
    
    def get_clause_evaluation(self, input_vector):
        """ Returns an array with the clause evaluations. """
        result = []
        for i in self._clauses:
            result.append(i.evaluate(input_vector))
        return result


    def _set_unparsed_equation(self, eq_str):
        """ Verifies and sets the unparsed equation attribute. """
        if self._validate_string(eq_str):
            self._unparsed_equation = eq_str
        else:
            raise AttributeError("The input string does not satisfy the validation requirements.")