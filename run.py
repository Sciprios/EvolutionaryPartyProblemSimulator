if __name__ == '__main__':
    #from PartyProblemSimulator.Simulator import Simulator
    #simulator = Simulator()
    #simulator.start()

    from PartyProblemSimulator.Solvers.EvoSAP import EvoSAP
    from PartyProblemSimulator.SatisfiabilitySimulator.BooleanEquation.Equation import Equation
    eq = Equation("(¬{0}+¬{1}+¬{2}).({0}+{1}+{2})")
    ga = EvoSAP()
    ga.run(eq, 3)