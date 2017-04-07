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
        """ Assess a single instance. """
        raise NotImplementedError("The do_trial method of Experiment is not implemented.")

    def _do_trial(self, method, equation, variable_count):
        """ Assess a single instance. """
        raise NotImplementedError("The do_trial method of Experiment is not implemented.")

    def _save_results(self, results):
        """ Saves the results of this experiment to disk. """
        raise NotImplementedError("The save_results method of Experiment is not implemented.")

    def _load_test_cases(self, results):
        """ Loads or creates the test cases to be used. """
        raise NotImplementedError("The _load_test_cases method of Experiment is not implemented.")

    def _test_method(self, method, no_trials, test_cases):
        """ Tests the given method with x trials on all test cases provided. """
        raise NotImplementedError("The _test_method method of Experiment is not implemented.")

    def _do_trial(self, method, equation, variable_count):
        """ Does a single trial of the algorithm provided. """
        raise NotImplementedError("The _do_trial method of Experiment is not implemented.")

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