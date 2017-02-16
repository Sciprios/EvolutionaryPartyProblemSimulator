
if __name__ == '__main__': # pragma : no cover
    from equation.BoolTree import Equation
    from solvers.FlipGA import FlipGA
    from solvers.EvoSAP import EvoSAP
    from solvers.BlindGA import BlindGA
    from pprint import PrettyPrinter
    import examples.interpreter as interpreter

    printer = PrettyPrinter(indent=4)   # Setup something which can print dictionaries

    # Load test set with 449 clauses to be made correct
    contents = interpreter.interpret_file("examples/CBS_k3_n100_m449_b70_238.cnf")
    equation_string = contents[0]
    variables = contents[1]
    
    print("Generating Equation")
    eq = Equation(equation_string)

    print("Instantiating Algorithm (BlindGA)")
    ga = BlindGA(eq, variables)
    ga.run()

    print("\n\n\n")

    print("Instantiating Algorithm (FlipGA)")
    ga = FlipGA(eq, variables)
    ga.run()
    
    print("\n\n\n")
    
    print("Instantiating Algorithm (EvoSAP)")
    ga = EvoSAP(eq, variables)
    ga.run()