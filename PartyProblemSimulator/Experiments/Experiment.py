from PartyProblemSimulator.BooleanEquation.Equation import Equation
from threading import Thread

class Experiment(Thread):
    """ An experiment to be run on the Party Problem Simulator. """

    def run(self):
        """ Should be implemented to execute the experiment and save results. """
        results = self._do_experiment()
        self._save_results(results)
    
    def _do_experiment(self):
        """ Execute the experiment and return results. """
        raise NotImplementedError("The do_experiment method of Experiment is not implemented.")
    
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

    def _load_test_cases(self, results):
        """ Loads or creates the test cases to be used. """
        raise NotImplementedError("The _load_test_cases method of Experiment is not implemented.")

    def _calculate_results(self, results):
        """ Calculates the SR (Success Rate) and AES (Average Evaluations per Solution) based on the results given."""
        sr = 0
        aes = 0
        for result in method_results:
            aes = aes + result['AES']
            sr = sr + result['SR']
        aes = aes / len(method_results)
        sr = sr / len(method_results)
        return {"AES": aes, "SR": sr}