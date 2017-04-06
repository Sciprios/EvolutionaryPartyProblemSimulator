from PartyProblemSimulator.Experiments.Experiment import Experiment
from PartyProblemSimulator.Solvers.BlindGA import BlindGA
from PartyProblemSimulator.Solvers.BlindKitanoGA import BlindKitanoGA
from PartyProblemSimulator.BooleanEquation.Equation import Equation
from PartyProblemSimulator.Graphing.ConnectedGraph import ConnectedGraph
from datetime import datetime
from random import randint
from itertools import combinations

class MutRate(Experiment):
    """ An experiment to compare the effectiveness of a morphogenetic approach to finding SAT solutions. """
    
    def _do_experiment(self):
        """ Tries both FlipGA and EvoSAP with different mutation methods. """
        no_trials = 2
        test_cases = self._load_test_cases()    # Get all test cases
        results = []

        mut_rate = 0.05
        while (mut_rate < 1):
            method = BlindKitanoGA()
            temp_res = {"Method": "BlindKitanoGA - Morphogenetic Encoding"}
            temp_res["CaseResults"] = self._test_method(method, no_trials, test_cases)  # Test the method
            temp_res["Overall"] = self._calculate_results(temp_res["CaseResults"])
            temp_res["MutRate"] = mut_rate
            results.append(temp_res)
            mut_rate = mut_rate + 0.05
        
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
    
    def _save_results(self, results):
        """ Saves the results of this experiment to disk. """
        for res in results:
            with open('PartyProblemSimulator\Experiments\Results\{}.res'.format(res['Method']), 'a') as file:   # Open file with name of method used
                file.write("METHOD NAME: {}, MUTATION RATE: {}\n".format(res['Method'], res['MutRate'])) # Output the goodies
                file.write("AES: {}\n".format(res['Overall']['AES']))
                file.write("SR: {}\n".format(res['Overall']['SR']))
                file.write("--------------------------\n")
                for case_res in res['CaseResults']:
                    file.write("Case AES: {}\t\tCase SR: {}\n".format(case_res['AES'], case_res['SR']))

    def _load_test_cases(self):
        """ Loads first 100 test cases from data if available. """
        test_cases = []
        default_filename = "PartyProblemSimulator\Experiments\Data\CBS_k3_n100_m449_b90_{}.cnf"
        counter = 70
        while counter == 70: #< 100:
            filename = default_filename.format(counter) # Get the new file
            response = self._interpret_file(filename)
            test_cases.append({     # Add details to test cases
                "Equation": response[0],
                "NumVars": response[1]
            })
            counter = counter + 1
        return test_cases

    def _test_method(self, method, no_trials, test_cases):
        """ Tests the given method with x trials on all test cases provided. """
        results = []
        for test_case in test_cases:
            test_case_aes = 0
            test_case_sr = 0
            trial_count = 0
            while trial_count < no_trials:
                equation_instance = Equation(test_case['Equation'])   # Generate the equation
                trial_res = self._do_trial(method, equation_instance, test_case['NumVars'])   # Do the trial
                if trial_res['Success']:    # Only add information if it was successful
                    test_case_sr = test_case_sr + 1
                    test_case_aes = test_case_aes + trial_res['Evaluations']
                trial_count = trial_count + 1
            try:
                test_case_aes = test_case_aes / test_case_sr    # Divide by the number of successes
            except ZeroDivisionError:
                test_case_aes = 0
            
            test_case_sr = test_case_sr / no_trials         # No. Successful trials / percentage
            results.append({
                "AES": test_case_aes,
                "SR": test_case_sr
            })
        return results

    def _do_trial(self, method, equation, variable_count):
        """ Does a single trial of the algorithm provided. """
        method.run(equation, variable_count)
        results = {}    # Build response
        results['Evaluations'] = method.get_num_evaluations()
        if (method.get_best_genome() is None) or (method.get_best_genome().evaluate(equation) == 1):    # Did the method find a solution?
            results['Success'] = True
        else:
            results['Success'] = False
        return results
    
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