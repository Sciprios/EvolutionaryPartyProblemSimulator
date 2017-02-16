if __name__ == '__main__': # pragma : no cover
    from equation.BoolTree import Equation
    from solvers.FlipGA import FlipGA
    from solvers.EvoSAP import EvoSAP

    # Define problem
    equation = '(A+B+D).(A+B+D).(A+E+C).(F+B+C).(D+I+H).(A+H+G).(G+J+C).(G+B+I).(E+H+J).(I+J+F).(K+I+M).(K+H+L).(K+G+D).(K+J+N).(M+B+D).(N+E+L).(N+C+D).(L+A+O).(M+I+J).(O+G+K).'
    equation = equation + '(¬A+¬B+¬D).(¬A+¬B+¬D).(¬A+¬E+¬C).(¬F+¬B+¬C).(¬D+¬I+¬H).(¬A+¬H+¬G).(¬G+¬J+¬C).(¬G+¬B+¬I).(¬E+¬H+¬J).(¬I+¬J+¬F).'
    equation = equation + '(¬K+¬I+¬M).(¬K+¬H+¬L).(¬K+¬G+¬D).(¬K+¬J+¬N).(¬M+¬B+¬D).(¬N+¬E+¬L).(¬N+¬C+¬D).(¬L+¬A+¬O).(¬M+¬I+¬J).(¬O+¬G+¬K)'

    print("Generating Equation")
    eq = Equation(equation)
    print("Instantiating Algorithm")
    ga = FlipGA(eq, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R'])
    ga.run()