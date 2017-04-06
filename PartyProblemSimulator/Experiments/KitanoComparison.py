from PartyProblemSimulator.Graphing.ConnectedGraph import ConnectedGraph
from PartyProblemSimulator.Experiments.Experiment import Experiment
from PartyProblemSimulator.BooleanEquation.Equation import Equation
from PartyProblemSimulator.Solvers.BlindGA import BlindGA
from PartyProblemSimulator.Solvers.BlindKitanoGA import BlindKitanoGA
from datetime import datetime
from random import randint
from itertools import combinations

class KitanoComparison(Experiment):
    """ An experiment to compare the effectiveness of different encoding methods for Ramsey theory. """
    
    def _do_experiment(self):
        """ Tries both FlipGA and EvoSAP with different mutation methods. """
        no_trials = 2
        test_cases = self._load_test_cases()    # Get all test cases
        results = []

        method = BlindGA # Use blindga first with no modification
        temp_res = {"Method": "BlindGA - Original"}
        temp_res["CaseResults"] = self._test_method(method, no_trials, test_cases)  # Test the method
        temp_res["Overall"] = self._calculate_results(temp_res["CaseResults"])
        results.append(temp_res)

        method = BlindKitanoGA
        temp_res = {"Method": "BlindGA - Morphogenetic"}
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
    
    def _save_results(self, results):
        """ Saves the results of this experiment to disk. """
        for res in results:
            with open('PartyProblemSimulator\Experiments\Results\{}.res'.format(res['Method']), 'w') as file:   # Open file with name of method used
                file.write("METHOD NAME: {}\n".format(res['Method'])) # Output the goodies
                file.write("AES: {}\n".format(res['Overall']['AES']))
                file.write("SR: {}\n".format(res['Overall']['SR']))
                file.write("--------------------------\n")
                for case_res in res['CaseResults']:
                    file.write("Case AES: {}\t\tCase SR: {}\n".format(case_res['AES'], case_res['SR']))

    def _load_test_cases(self):
        """ Loads first 100 test cases from data if available. """
        test_cases = []
        possible_cases = [(3, 6), (4, 18)]
        for poss_case in possible_cases:    # For each case
            count = poss_case[0]
            while count < poss_case[1]:    # Have graph sizes up to the ramsey number
               response = self._get_case(count, poss_case[0])
               test_cases.append({     # Add details to test cases
                   "Equation": response[0],
                   "NumVars": response[1]
               })
               count = count + 1
               break
            break
        return test_cases

    def _test_method(self, method, no_trials, test_cases):
        """ Tests the given method with x trials on all test cases provided. """
        results = []
        for test_case in test_cases:
            test_case_aes = 0
            test_case_sr = 0
            trial_count = 0
            while trial_count < no_trials:
                trial_res = self._do_trial(method(), Equation(test_case['Equation']), test_case['NumVars'])   # Do the trial
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
    
    def _get_case(self, graph_size, clique_size):
        """ Generates a boolean equation and variable set based on the parameters. """
        graph = ConnectedGraph(graph_size)
        # Generate string equivalent
        bln_eq_str = ""
        var_set = []
        vertex_combinations = combinations(graph.get_vertices(), clique_size)    # Get all combinations of vertices
        for combination in vertex_combinations:
            # Generate clause and inverse clause
            clause_one = ""
            clause_two = ""
            for edge in graph.get_edges():  # Get all edges in this combination
                if (edge.get_origin() in combination) and (edge.get_target() in combination):
                    edge_id = str(edge.get_id())    # Found an edge in this combination
                    var_id = "{" + edge_id + "}"
                    clause_one = clause_one + "+¬" + var_id + ""
                    clause_two = clause_two + "+" + var_id + ""
                    
            # Format clause
            clause_one = "(" + clause_one[1:] + ")" # The substring removes the first redundant "AND" symbol
            clause_two = "(" + clause_two[1:] + ")"
            # Add clause to equation
            bln_eq_str = bln_eq_str + "." + clause_one + "." + clause_two
        # Generate variables list
        for edge in graph.get_edges():
            var_id = "{" + str(edge.get_id()) + "}"
            var_set.append(var_id)
        # Format Equation
        bln_eq_str = bln_eq_str[1:] # Removes redundant AND symbol
        # Generate equation object
        return (bln_eq_str, len(var_set))