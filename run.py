from equation.BoolTree import Equation
from solvers.FlipGA import FlipGA

eq = Equation('(A+(C+D).A).(B).(C).(D).(E).(F).(G)')
ga = FlipGA(eq, ['A', 'B', 'C', 'D', 'E', 'F', 'G'])
ga.run()