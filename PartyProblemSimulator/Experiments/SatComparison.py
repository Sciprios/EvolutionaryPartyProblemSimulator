from PartyProblemSimulator.Experiments.Experiment import Experiment
from PartyProblemSimulator.Solvers.FlipGA import FlipGA, FlipGA_1, FlipGA_2
from PartyProblemSimulator.Solvers.EvoSAP import EvoSAP, EvoSAP_1, EvoSAP_2
from datetime import datetime
from random import randint

class SatComparison(Experiment):
    """ An experiment to compare the effectiveness of different mutation methods for sat solvers. """
    
    def _do_experiment(self):
        """ Tries both FlipGA and EvoSAP with different mutation methods. """
        no_trials = 20
        test_cases = self._load_test_cases()    # Get all test cases
        results = []

        method = FlipGA # Use flipga first with no modification
        temp_res = {"Method": "FlipGA - Original"}
        temp_res["CaseResults"] = self._test_method(method, no_trials, test_cases)  # Test the method
        temp_res["Overall"] = self._calculate_results(temp_res["CaseResults"])
        results.append(temp_res)

        method = FlipGA_1
        temp_res = {"Method": "FlipGA - Mutation 1"}
        temp_res["CaseResults"] = self._test_method(method, no_trials, test_cases)  # Test the method
        temp_res["Overall"] = self._calculate_results(temp_res["CaseResults"])
        results.append(temp_res)

        method = FlipGA_2
        temp_res = {"Method": "FlipGA - Mutation 2"}
        temp_res["CaseResults"] = self._test_method(method, no_trials, test_cases)  # Test the method
        temp_res["Overall"] = self._calculate_results(temp_res["CaseResults"])
        results.append(temp_res)

        method = EvoSAP # Use EvoSAP first with no modification
        temp_res = {"Method": "EvoSAP - Original"}
        temp_res["CaseResults"] = self._test_method(method, no_trials, test_cases)  # Test the method
        temp_res["Overall"] = self._calculate_results(temp_res["CaseResults"])
        results.append(temp_res)

        method = EvoSAP_1
        temp_res = {"Method": "EvoSAP - Mutation 1"}
        temp_res["CaseResults"] = self._test_method(method, no_trials, test_cases)  # Test the method
        temp_res["Overall"] = self._calculate_results(temp_res["CaseResults"])
        results.append(temp_res)

        method = EvoSAP_2
        temp_res = {"Method": "EvoSAP - Mutation 2"}
        temp_res["CaseResults"] = self._test_method(method, no_trials, test_cases)  # Test the method
        temp_res["Overall"] = self._calculate_results(temp_res["CaseResults"])
        results.append(temp_res)
        
        return results
        
    def _calculate_results(self, method_results):
        """ Calculates the SR (Success Rate) and AES (Average Evaluations per Solution) based on the results given."""
        sr = 0
        aes = 0
        for result in method_results:
            aes = aes + result['AES']
            sr = sr + result['SR']
        aes = aes / len(method_results)
        sr = sr / len(method_results)
        return {"AES": aes, "SR": sr}
    
    def _load_test_cases(self):
        """ Loads first 100 test cases from data if available. """
        test_cases = []
        default_filename = "PartyProblemSimulator\Experiments\Data\CBS_k3_n100_m449_b90_{}.cnf"
        counter = 0
        while counter < 100:
            filename = default_filename.format(counter) # Get the new file
            response = self._interpret_file(filename)
            test_cases.append({     # Add details to test cases
                "Equation": response[0],
                "NumVars": response[1]
            })
            counter = counter + 1
        return test_cases
    
    def _interpret_file(self, filename):
        """ Interprets a CBS datafile """
        clauses = []
        vars = []
        equation = ""
        with open(filename, mode='r') as cnf_file: # Extract each clause from the 
            for line in cnf_file:
                if line[0] == 'c':  # This is a comment
                    pass
                elif line[0] == 'p':    # This determines the number of variables and clauses.
                    contents = line.split(' ')
                    var_count = int(contents[2])
                else:
                    line = line.replace('-', '¬') # Replace all minuses with inversion operators
                    line = line[:-4]
                    line = line.replace('  ', '+') # Replace all spaces with OR operators
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
                    new_clause = new_str
                    clauses.append(new_clause)
                    
        # Now combine the clauses into a single formula
        i = 0
        for c in clauses:
            if i is 0:
                equation = "({})".format(c)
            else:
                equation = equation + ".({})".format(c)
            i = i + 1
        
        return (equation, var_count)