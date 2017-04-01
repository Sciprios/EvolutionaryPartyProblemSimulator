# Evolutionary Party Problem Simulator

This simulator allows a user to attempt to find solutions to classic 2-clique party problems of a defined size within a connected graph. The simulator utilizes evolutionary computation and has been used in modern research into the effectiveness of mutation methods.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

What things you need to install the software and how to install them

* Python 3.4 <
* Tkinter (Python Package)
* pygubu (Python Package)

If you wish to execute the unittests you will also need:

* pytest-cov (Python Package)

### Installing

A step by step series of examples that tell you have to get the simulator running.

Download or clone this repository into a directory of your choosing.

Using a command line tool enter the EvolutionaryPartyProblemSimulator repository.

```
C:\Users\Andy\Desktop>cd EvolutionaryPartyProblemSimulator
```

Begin the service by running the python script in this directory.

```
C:\Users\Andy\Desktop\EvolutionaryPartyProblemSimulator>python run.py
```

### Running Experiments

To run the experiments first enter the relevant directory for this project via a command line utility; for example:

```
C:\Users\Andy\Desktop>cd EvolutionaryPartyProblemSimulator
```

Execute the run experiments script as follows:

```
C:\Users\Andy\Desktop\EvolutionaryPartyProblemSimulator>python run_experiments.py
```

You will then be prompted to select an experiment to run, see below for the options available to you:

| Option  | Title | Description |
| ------------- | ------------- | ------------- |
| Content Cell  | Content Cell  | Content Cell  |
| Content Cell  | Content Cell  | Content Cell  |

Enter the relevant option number and the experiment shall begin; results from the experiment shall be saved in a results file in the directory below:

```
EvolutionaryPartyProblemSimulator\PartyProblemSimulator\Experiments\Results
```

### Running unittests

To execute the automated unittests with a basic coverage report use the following command:

```
py.test --cov=. --cov-config .coveragec
```

## Built With

* [Python 3.4](https://www.python.org/download/releases/3.4.0/) - Language of Implementation

## Authors

* **Andrew Barnes** - *Dissertation* - [Sciprios](https://github.com/Sciprios)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to my supervisor Angelo Cangelosi.
