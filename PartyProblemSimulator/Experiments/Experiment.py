from threading import Thread

class Experiment(Thread):
    """ An experiment to be run on the Party Problem Simulator. """

    def run(self):
        """ Should be implemented to execute the experiment and save results. """
        results = self.do_experiment()
        self.save_results(results)
    
    def do_experiment(self):
        """ Execute the experiment and return results. """
        raise NotImplementedError("The do_experiment method of Experiment is not implemented.")
    
    def save_results(self, results):
        """ Saves the results of this experiment to disk. """
        raise NotImplementedError("The save_results method of Experiment is not implemented.")