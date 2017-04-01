from PartyProblemSimulator.Experiments.SatComparison import SatComparison
from os.path import isfile
from colorama import Fore, Style, init

def print_coloured(colour, text):
    """ Prints text in colour. """
    print(colour + text + Style.RESET_ALL + Fore.RESET)

if __name__ == '__main__':
    init() # Allow coloured text
    selection_valid = False # Work out which experiment to run
    selection = -1
    print("=======================")
    print_coloured(Style.BRIGHT, "WELCOME TO EXPERIMENTS")
    print("=======================")
    print_coloured(Fore.GREEN, "Select an experiment from the list below:")
    print("0 - SAT Solution finding")
    print("")
    print_coloured(Fore.CYAN, "For full descriptions of the experiments please refer to GitHub README.")
    while selection_valid is False:     # Get selection from user
        selection = input("Option Number -> ")
        print("")
        try:
            selection = int(selection)  # Validation of selection
            if (selection < 0) or (selection > 0):
                raise ValueError()
            else:
                selection_valid = True
        except ValueError:
            print_coloured(Fore.YELLOW, "Please enter a number from the list of experiments.")    # Error message
            print("")
    

    if selection == 0:
        print_coloured(Fore.GREEN, "Running the SAT Solution Finding experiment.")
        default_datafile = "PartyProblemSimulator\Experiments\Data\CBS_k3_n100_m449_b90_{}.cnf"    # Check all data files exist
        count = 0
        data_available = True
        while count < 100:
            if not isfile(default_datafile.format(count)):
                print(Fore.YELLOW, "Data file is missing. File name: {}".format(default_datafile.format(count)))
                data_available = False
                break
            count = count + 1
        if data_available is not True:  # Is there data missing?
            print_coloured(Fore.RED, "Please ensure you have the correct data files. For more information please refer to the GitHub Wiki.")
        else:
            exp = SatComparison()
            exp.start()