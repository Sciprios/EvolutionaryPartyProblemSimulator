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

Using a command line tool enter the PartyProblemSimulator repository.

```
C:\Users\Andy\Desktop>cd PartyProblemSimulator
```

Being the service by running the python script in this directory.

```
C:\Users\Andy\Desktop\PartyProblemSimulator>python run.py
```

## Running the tests

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
