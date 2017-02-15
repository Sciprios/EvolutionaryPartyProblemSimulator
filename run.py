from equation.BoolTree import Equation
from solvers.FlipGA import FlipGA
from solvers.EvoSAP import EvoSAP

# Define problem
#vars = '(A+B+D).(A+B+D).(A+E+C).(F+B+C).(D+I+H).(A+H+G).(G+J+C).(G+B+I).(E+H+J).(I+J+F).(K+I+M).(K+H+L).(K+G+D).(K+J+N).(M+B+D).(N+E+L).(N+C+D).(L+A+O).(M+I+J).(O+G+K).'
#vars = vars + '(¬A+¬B+¬D).(¬A+¬B+¬D).(¬A+¬E+¬C).(¬F+¬B+¬C).(¬D+¬I+¬H).(¬A+¬H+¬G).(¬G+¬J+¬C).(¬G+¬B+¬I).(¬E+¬H+¬J).(¬I+¬J+¬F).'
#vars = vars + '(¬K+¬I+¬M).(¬K+¬H+¬L).(¬K+¬G+¬D).(¬K+¬J+¬N).(¬M+¬B+¬D).(¬N+¬E+¬L).(¬N+¬C+¬D).(¬L+¬A+¬O).(¬M+¬I+¬J).(¬O+¬G+¬K)'
#ga = FlipGA(eq, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'])
#ga.run()

vars = '(A+B+D).(A+B+D).(A+E+C).(F+B+C).(D+I+H).(A+H+G).(G+J+C).(G+B+I).(E+H+J).(I+J+F).'
vars = vars + '(¬A+¬B+¬D).(¬A+¬B+¬D).(¬A+¬E+¬C).(¬F+¬B+¬C).(¬D+¬I+¬H).(¬A+¬H+¬G).(¬G+¬J+¬C).(¬G+¬B+¬I).(¬E+¬H+¬J).(¬I+¬J+¬F)'
# Define equation and algorithm
eq = Equation(vars)
#ga = FlipGA(eq, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
ga = EvoSAP(eq, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])

ga.run()

# eq = Equation('(A).(B).(C).(D).(E).(F).(G).(H).(I).(J).(K).(L).(M).(N).(O).(P).(Q).(R).(S).(T).(U).(V).(W).(X).(Y).(Z)')
# ga = FlipGA(eq, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
# ga.run()

#eq = Equation('(A).(B).(C).(D).(E).(F)')
#ga = FlipGA(eq, ['A', 'B', 'C', 'D', 'E', 'F'])
#ga.run().0