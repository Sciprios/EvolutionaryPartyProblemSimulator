if __name__ == '__main__':
    from PartyProblemSimulator.Simulator import Simulator
    simulator = Simulator()
    simulator.start()

    #from PartyProblemSimulator.Solvers.EvoSAP import EvoSAP
    #from PartyProblemSimulator.SatisfiabilitySimulator.BooleanEquation.Equation import Equation
    #eq = Equation("(¬{0}+¬{1}+¬{3}).({0}+{1}+{3}).(¬{0}+¬{2}+¬{4}).({0}+{2}+{4}).(¬{1}+¬{2}+¬{5}).({1}+{2}+{5}).(¬{3}+¬{4}+¬{5}).({3}+{4}+{5})")
    #ga = EvoSAP()
    #ga.run(eq, 5)