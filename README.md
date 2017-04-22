# Evolutionary Party Problem Simulator

This simulator allows a user to attempt to find solutions to classic 2-clique party problems of a defined size within a connected graph. The simulator utilizes evolutionary computation and has been used in modern research into the effectiveness of mutation methods.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

What things you need to install the software and how to install them

* Python 3.4 <=
* Tkinter (Python Package)
* pygubu (Python Package)

If you wish to execute the unittests you will also need:

* pytest (Python Package)
* pytest-cov (Python Package)

To run experiments you will need:

* colorama (Python Package)

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

#### Prerequisites

Before being able to run any experiments you will need to ensure the Data folder is populated with the data set available [Here](http://www.cs.ubc.ca/~hoos/SATLIB/Benchmarks/SAT/CBS/CBS_k3_n100_m435_b70.tar.gz).
Simply extract the file to the Data folder (which is within the Experiments package), you can then use as much data as you'd like. The experiments carried out for this project used the first 100 instances.

To run the experiments first enter the relevant directory for this project via a command line utility; for example:

```
C:\Users\Andy\Desktop>cd EvolutionaryPartyProblemSimulator
```

Execute the run experiments script as follows:

```
C:\Users\Andy\Desktop\EvolutionaryPartyProblemSimulator>python run_experiments.py
```

You will then be prompted to select an experiment to run, see below for the options available to you:

| Option  | Title | Description | Output Format |
| ------------- | ------------- | ------------- | ------------- |
| 0  | SAT Solution Finding  | Tests 2 different mutation methods with both FlipGA and EvoSAP along with the original methods.  | An overview result will appear at the top of the results file with results for each test underneath.  |
| 1  | Morphogenetic encoding for clique problems  | Tests two different encoding methods for the finding of graphs with no such cliques as demanded by the test cases.  | An overview result will appear at the top of the results file with results for each test underneath.  |

Enter the relevant option number and the experiment shall begin; results from the experiment shall be saved in a results file in the directory below:

```
EvolutionaryPartyProblemSimulator\PartyProblemSimulator\Experiments\Results
```

Please note some experiments will require some extra data to be downloaded and extracted; for more information on this please refer to the wiki presented [here](https://github.com/Sciprios/EvolutionaryPartyProblemSimulator/wiki/Experiments). 

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
