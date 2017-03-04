from equation.BoolTree import Equation
from solvers.FlipGA import FlipGA
from solvers.EvoSAP import EvoSAP
from solvers.BlindGA import BlindGA
from collections import Counter
from pprint import PrettyPrinter
from threading import Thread
from solvers.experimental.FlipGA import FlipGA_1, FlipGA_2, FlipGA_3
from solvers.experimental.EvoSAP import EvoSAP_1, EvoSAP_2, EvoSAP_3
from solvers.experimental.BlindGA import BlindGA_1, BlindGA_2, BlindGA_3
import examples.interpreter as interpreter

NO_TRIALS = 10

def run_test(file_name, results, cl_ga):
    """ Runs a test on the given file name. """
    print("Collecting file - {}".format(file_name))
    contents = interpreter.interpret_file(file_name)
    equation_string = contents[0]
    variables = contents[1]

    print("Generating Equation")
    eq = Equation(equation_string)

    print("Generating & starting algorithm instances")
    print("(This is done on seperate threads.)")
    instances = []
    threads = []
    cnt = 0
    while cnt < NO_TRIALS:
        instances.append(cl_ga(eq, variables))
        threads.append(Thread(target=instances[cnt].run))
        threads[cnt].start()
        cnt = cnt + 1
    
    cnt = 0
    while cnt < NO_TRIALS:  # Wait for all threads to finish.
        threads[cnt].join()
        cnt = cnt + 1
    print("All trials are complete with algorithm {}".format(cl_ga))
    
    print("Calculating Results")    # Total results
    trial_results = {'SR': 0, 'AES': 0}
    for i in instances:
        if i.get_best_org()['fitness'] >= len(i._EQUATION._clauses):  # Did the algorithm solve it?
            trial_results['SR'] = trial_results['SR'] + 1
        else:
            trial_results['SR'] = trial_results['SR'] + 0
        trial_results['AES'] = trial_results['AES'] + i._eval_count
    
    # Average scores accross instances
    results.append({'Test Case': file_name, 'AES': trial_results['AES']/NO_TRIALS, 'SR': trial_results['SR']/NO_TRIALS})


if __name__ == '__main__': # pragma : no cover   

    printer = PrettyPrinter(indent=4)   # Setup something which can print dictionaries
    cnt_min = 0
    cnt_max = 51
    results = []
    cnt = cnt_min
    while cnt < cnt_max: # Run for instances (Original Method)
        file_name  = "examples/data/CBS_k3_n100_m449_b70_" + str(cnt) + ".cnf"
        run_test(file_name, results, FlipGA)
        cnt = cnt + 1
    cnt = cnt_min
    with open('test_FlipGA.res', mode='w') as res_file: # Extract each clause from the 
        for r in results:
            res_file.write("{}\t\t\t{}\t\t\t{}\n".format(r['Test Case'], r['AES'], r['SR']))
            print("{}\t\t{}\t\t{}".format(r['Test Case'], r['AES'], r['SR']))