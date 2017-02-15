from equation.BoolTree import Equation
from solvers.FlipGA import FlipGA
from solvers.EvoSAP import EvoSAP

# Define problem
#vars = '(A+B+D).(A+B+D).(A+E+C).(F+B+C).(D+I+H).(A+H+G).(G+J+C).(G+B+I).(E+H+J).(I+J+F).(K+I+M).(K+H+L).(K+G+D).(K+J+N).(M+B+D).(N+E+L).(N+C+D).(L+A+O).(M+I+J).(O+G+K).'
#vars = vars + '(¬A+¬B+¬D).(¬A+¬B+¬D).(¬A+¬E+¬C).(¬F+¬B+¬C).(¬D+¬I+¬H).(¬A+¬H+¬G).(¬G+¬J+¬C).(¬G+¬B+¬I).(¬E+¬H+¬J).(¬I+¬J+¬F).'
#vars = vars + '(¬K+¬I+¬M).(¬K+¬H+¬L).(¬K+¬G+¬D).(¬K+¬J+¬N).(¬M+¬B+¬D).(¬N+¬E+¬L).(¬N+¬C+¬D).(¬L+¬A+¬O).(¬M+¬I+¬J).(¬O+¬G+¬K)'
#eq = Equation(vars)
#ga = FlipGA(eq, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O'])
#ga.run()

#vars = '(A+B+D).(A+B+D).(A+E+C).(F+B+C).(D+I+H).(A+H+G).(G+J+C).(G+B+I).(E+H+J).(I+J+F).'
#vars = vars + '(¬A+¬B+¬D).(¬A+¬B+¬D).(¬A+¬E+¬C).(¬F+¬B+¬C).(¬D+¬I+¬H).(¬A+¬H+¬G).(¬G+¬J+¬C).(¬G+¬B+¬I).(¬E+¬H+¬J).(¬I+¬J+¬F)'
#eq = Equation(vars)
#ga = FlipGA(eq, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
#ga = EvoSAP(eq, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
#ga.run()

# eq = Equation('(A).(B).(C).(D).(E).(F).(G).(H).(I).(J).(K).(L).(M).(N).(O).(P).(Q).(R).(S).(T).(U).(V).(W).(X).(Y).(Z)')
# ga = FlipGA(eq, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
# ga.run()

vars = '(A+B+C).(A+B+D).(A+B+E).(A+B+F).(A+B+G).(A+B+H).(A+B+I).(A+B+J).(A+B+K).(A+B+L).(A+B+M).(A+B+N).(A+B+O).(A+B+P).(A+B+Q).(A+B+R).(A+B+S).(A+B+T).(A+C+D).(A+C+E).(A+C+F).(A+C+G).(A+C+H).(A+C+I).(A+C+J).(A+C+K).(A+C+L).(A+C+M).(A+C+N).(A+C+O).(A+C+P).(A+C+Q).(A+C+R).(A+C+S).(A+C+T).(A+D+E).(A+D+F).(A+D+G).(A+D+H).(A+D+I).(A+D+J).(A+D+K).(A+D+L).(A+D+M).(A+D+N).(A+D+O).(A+D+P).(A+D+Q).(A+D+R).(A+D+S).(A+D+T).(A+E+F).(A+E+G).(A+E+H).(A+E+I).(A+E+J).(A+E+K).(A+E+L).(A+E+M).(A+E+N).(A+E+O).(A+E+P).(A+E+Q).(A+E+R).(A+E+S).(A+E+T).(A+F+G).(A+F+H).(A+F+I).(A+F+J).(A+F+K).(A+F+L).(A+F+M).(A+F+N).(A+F+O).(A+F+P).(A+F+Q).(A+F+R).(A+F+S).(A+F+T).(A+G+H).(A+G+I).(A+G+J).(A+G+K).(A+G+L).(A+G+M).(A+G+N).(A+G+O).(A+G+P).(A+G+Q).(A+G+R).(A+G+S).(A+G+T).(A+H+I).(A+H+J).(A+H+K).(A+H+L).(A+H+M).(A+H+N).(A+H+O).(A+H+P).(A+H+Q).(A+H+R).(A+H+S).(A+H+T).(A+I+J).(A+I+K).(A+I+L).(A+I+M).(A+I+N).(A+I+O).(A+I+P).(A+I+Q).(A+I+R).(A+I+S).(A+I+T).(A+J+K).(A+J+L).(A+J+M).(A+J+N).(A+J+O).(A+J+P).(A+J+Q).(A+J+R).(A+J+S).(A+J+T).(A+K+L).(A+K+M).(A+K+N).(A+K+O).(A+K+P).(A+K+Q).(A+K+R).(A+K+S).(A+K+T).(A+L+M).(A+L+N).(A+L+O).(A+L+P).(A+L+Q).(A+L+R).(A+L+S).(A+L+T).(A+M+N).(A+M+O).(A+M+P).(A+M+Q).(A+M+R).(A+M+S).(A+M+T).(A+N+O).(A+N+P).(A+N+Q).(A+N+R).(A+N+S).(A+N+T).(A+O+P).(A+O+Q).(A+O+R).(A+O+S).(A+O+T).(A+P+Q).(A+P+R).(A+P+S).(A+P+T).(A+Q+R).(A+Q+S).(A+Q+T).(A+R+S).(A+R+T).(A+S+T).(B+C+D).(B+C+E).(B+C+F).(B+C+G).(B+C+H).(B+C+I).(B+C+J).(B+C+K).(B+C+L).(B+C+M).(B+C+N).(B+C+O).(B+C+P).(B+C+Q).(B+C+R).(B+C+S).(B+C+T).(B+D+E).(B+D+F).(B+D+G).(B+D+H).(B+D+I).(B+D+J).(B+D+K).(B+D+L).(B+D+M).(B+D+N).(B+D+O).(B+D+P).(B+D+Q).(B+D+R).(B+D+S).(B+D+T).(B+E+F).(B+E+G).(B+E+H).(B+E+I).(B+E+J).(B+E+K).(B+E+L).(B+E+M).(B+E+N).(B+E+O).(B+E+P).(B+E+Q).(B+E+R).(B+E+S).(B+E+T).(B+F+G).(B+F+H).(B+F+I).(B+F+J).(B+F+K).(B+F+L).(B+F+M).(B+F+N).(B+F+O).(B+F+P).(B+F+Q).(B+F+R).(B+F+S).(B+F+T).(B+G+H).(B+G+I).(B+G+J).(B+G+K).(B+G+L).(B+G+M).(B+G+N).(B+G+O).(B+G+P).(B+G+Q).(B+G+R).(B+G+S).(B+G+T).(B+H+I).(B+H+J).(B+H+K).(B+H+L).(B+H+M).(B+H+N).(B+H+O).(B+H+P).(B+H+Q).(B+H+R).(B+H+S).(B+H+T).(B+I+J).(B+I+K).(B+I+L).(B+I+M).(B+I+N).(B+I+O).(B+I+P).(B+I+Q).(B+I+R).(B+I+S).(B+I+T).(B+J+K).(B+J+L).(B+J+M).(B+J+N).(B+J+O).(B+J+P).(B+J+Q).(B+J+R).(B+J+S).(B+J+T).(B+K+L).(B+K+M).(B+K+N).(B+K+O).(B+K+P).(B+K+Q).(B+K+R).(B+K+S).(B+K+T).(B+L+M).(B+L+N).(B+L+O).(B+L+P).(B+L+Q).(B+L+R).(B+L+S).(B+L+T).(B+M+N).(B+M+O).(B+M+P).(B+M+Q).(B+M+R).(B+M+S).(B+M+T).(B+N+O).(B+N+P).(B+N+Q).(B+N+R).(B+N+S).(B+N+T).(B+O+P).(B+O+Q).(B+O+R).(B+O+S).(B+O+T).(B+P+Q).(B+P+R).(B+P+S).(B+P+T).(B+Q+R).(B+Q+S).(B+Q+T).(B+R+S).(B+R+T).(B+S+T).(C+D+E).(C+D+F).(C+D+G).(C+D+H).(C+D+I).(C+D+J).(C+D+K).(C+D+L).(C+D+M).(C+D+N).(C+D+O).(C+D+P).(C+D+Q).(C+D+R).(C+D+S).(C+D+T).(C+E+F).(C+E+G).(C+E+H).(C+E+I).(C+E+J).(C+E+K).(C+E+L).(C+E+M).(C+E+N).(C+E+O).(C+E+P).(C+E+Q).(C+E+R).(C+E+S).(C+E+T).(C+F+G).(C+F+H).(C+F+I).(C+F+J).(C+F+K).(C+F+L).(C+F+M).(C+F+N).(C+F+O).(C+F+P).(C+F+Q).(C+F+R).(C+F+S).(C+F+T).(C+G+H).(C+G+I).(C+G+J).(C+G+K).(C+G+L).(C+G+M).(C+G+N).(C+G+O).(C+G+P).(C+G+Q).(C+G+R).(C+G+S).(C+G+T).(C+H+I).(C+H+J).(C+H+K).(C+H+L).(C+H+M).(C+H+N).(C+H+O).(C+H+P).(C+H+Q).(C+H+R).(C+H+S).(C+H+T).(C+I+J).(C+I+K).(C+I+L).(C+I+M).(C+I+N).(C+I+O).(C+I+P).(C+I+Q).(C+I+R).(C+I+S).(C+I+T).(C+J+K).(C+J+L).(C+J+M).(C+J+N).(C+J+O).(C+J+P).(C+J+Q).(C+J+R).(C+J+S).(C+J+T).(C+K+L).(C+K+M).(C+K+N).(C+K+O).(C+K+P).(C+K+Q).(C+K+R).(C+K+S).(C+K+T).(C+L+M).(C+L+N).(C+L+O).(C+L+P).(C+L+Q).(C+L+R).(C+L+S).(C+L+T).(C+M+N).(C+M+O).(C+M+P).(C+M+Q).(C+M+R).(C+M+S).(C+M+T).(C+N+O).(C+N+P).(C+N+Q).(C+N+R).(C+N+S).(C+N+T).(C+O+P).(C+O+Q).(C+O+R).(C+O+S).(C+O+T).(C+P+Q).(C+P+R).(C+P+S).(C+P+T).(C+Q+R).(C+Q+S).(C+Q+T).(C+R+S).(C+R+T).(C+S+T).(D+E+F).(D+E+G).(D+E+H).(D+E+I).(D+E+J).(D+E+K).(D+E+L).(D+E+M).(D+E+N).(D+E+O).(D+E+P).(D+E+Q).(D+E+R).(D+E+S).(D+E+T).(D+F+G).(D+F+H).(D+F+I).(D+F+J).(D+F+K).(D+F+L).(D+F+M).(D+F+N).(D+F+O).(D+F+P).(D+F+Q).(D+F+R).(D+F+S).(D+F+T).(D+G+H).(D+G+I).(D+G+J).(D+G+K).(D+G+L).(D+G+M).(D+G+N).(D+G+O).(D+G+P).(D+G+Q).(D+G+R).(D+G+S).(D+G+T).(D+H+I).(D+H+J).(D+H+K).(D+H+L).(D+H+M).(D+H+N).(D+H+O).(D+H+P).(D+H+Q).(D+H+R).(D+H+S).(D+H+T).(D+I+J).(D+I+K).(D+I+L).(D+I+M).(D+I+N).(D+I+O).(D+I+P).(D+I+Q).(D+I+R).(D+I+S).(D+I+T).(D+J+K).(D+J+L).(D+J+M).(D+J+N).(D+J+O).(D+J+P).(D+J+Q).(D+J+R).(D+J+S).(D+J+T).(D+K+L).(D+K+M).(D+K+N).(D+K+O).(D+K+P).(D+K+Q).(D+K+R).(D+K+S).(D+K+T).(D+L+M).(D+L+N).(D+L+O).(D+L+P).(D+L+Q).(D+L+R).(D+L+S).(D+L+T).(D+M+N).(D+M+O).(D+M+P).(D+M+Q).(D+M+R).(D+M+S).(D+M+T).(D+N+O).(D+N+P).(D+N+Q).(D+N+R).(D+N+S).(D+N+T).(D+O+P).(D+O+Q).(D+O+R).(D+O+S).(D+O+T).(D+P+Q).(D+P+R).(D+P+S).(D+P+T).(D+Q+R).(D+Q+S).(D+Q+T).(D+R+S).(D+R+T).(D+S+T).(E+F+G).(E+F+H).(E+F+I).(E+F+J).(E+F+K).(E+F+L).(E+F+M).(E+F+N).(E+F+O).(E+F+P).(E+F+Q).(E+F+R).(E+F+S).(E+F+T).(E+G+H).(E+G+I).(E+G+J).(E+G+K).(E+G+L).(E+G+M).(E+G+N).(E+G+O).(E+G+P).(E+G+Q).(E+G+R).(E+G+S).(E+G+T).(E+H+I).(E+H+J).(E+H+K).(E+H+L).(E+H+M).(E+H+N).(E+H+O).(E+H+P).(E+H+Q).(E+H+R).(E+H+S).(E+H+T).(E+I+J).(E+I+K).(E+I+L).(E+I+M).(E+I+N).(E+I+O).(E+I+P).(E+I+Q).(E+I+R).(E+I+S).(E+I+T).(E+J+K).(E+J+L).(E+J+M).(E+J+N).(E+J+O).(E+J+P).(E+J+Q).(E+J+R).(E+J+S).(E+J+T).(E+K+L).(E+K+M).(E+K+N).(E+K+O).(E+K+P).(E+K+Q).(E+K+R).(E+K+S).(E+K+T).(E+L+M).(E+L+N).(E+L+O).(E+L+P).(E+L+Q).(E+L+R).(E+L+S).(E+L+T).(E+M+N).(E+M+O).(E+M+P).(E+M+Q).(E+M+R).(E+M+S).(E+M+T).(E+N+O).(E+N+P).(E+N+Q).(E+N+R).(E+N+S).(E+N+T).(E+O+P).(E+O+Q).(E+O+R).(E+O+S).(E+O+T).(E+P+Q).(E+P+R).(E+P+S).(E+P+T).(E+Q+R).(E+Q+S).(E+Q+T).(E+R+S).(E+R+T).(E+S+T).(F+G+H).(F+G+I).(F+G+J).(F+G+K).(F+G+L).(F+G+M).(F+G+N).(F+G+O).(F+G+P).(F+G+Q).(F+G+R).(F+G+S).(F+G+T).(F+H+I).(F+H+J).(F+H+K).(F+H+L).(F+H+M).(F+H+N).(F+H+O).(F+H+P).(F+H+Q).(F+H+R).(F+H+S).(F+H+T).(F+I+J).(F+I+K).(F+I+L).(F+I+M).(F+I+N).(F+I+O).(F+I+P).(F+I+Q).(F+I+R).(F+I+S).(F+I+T).(F+J+K).(F+J+L).(F+J+M).(F+J+N).(F+J+O).(F+J+P).(F+J+Q).(F+J+R).(F+J+S).(F+J+T).(F+K+L).(F+K+M).(F+K+N).(F+K+O).(F+K+P).(F+K+Q).(F+K+R).(F+K+S).(F+K+T).(F+L+M).(F+L+N).(F+L+O).(F+L+P).(F+L+Q).(F+L+R).(F+L+S).(F+L+T).(F+M+N).(F+M+O).(F+M+P).(F+M+Q).(F+M+R).(F+M+S).(F+M+T).(F+N+O).(F+N+P).(F+N+Q).(F+N+R).(F+N+S).(F+N+T).(F+O+P).(F+O+Q).(F+O+R).(F+O+S).(F+O+T).(F+P+Q).(F+P+R).(F+P+S).(F+P+T).(F+Q+R).(F+Q+S).(F+Q+T).(F+R+S).(F+R+T).(F+S+T).(G+H+I).(G+H+J).(G+H+K).(G+H+L).(G+H+M).(G+H+N).(G+H+O).(G+H+P).(G+H+Q).(G+H+R).(G+H+S).(G+H+T).(G+I+J).(G+I+K).(G+I+L).(G+I+M).(G+I+N).(G+I+O).(G+I+P).(G+I+Q).(G+I+R).(G+I+S).(G+I+T).(G+J+K).(G+J+L).(G+J+M).(G+J+N).(G+J+O).(G+J+P).(G+J+Q).(G+J+R).(G+J+S).(G+J+T).(G+K+L).(G+K+M).(G+K+N).(G+K+O).(G+K+P).(G+K+Q).(G+K+R).(G+K+S).(G+K+T).(G+L+M).(G+L+N).(G+L+O).(G+L+P).(G+L+Q).(G+L+R).(G+L+S).(G+L+T).(G+M+N).(G+M+O).(G+M+P).(G+M+Q).(G+M+R).(G+M+S).(G+M+T).(G+N+O).(G+N+P).(G+N+Q).(G+N+R).(G+N+S).(G+N+T).(G+O+P).(G+O+Q).(G+O+R).(G+O+S).(G+O+T).(G+P+Q).(G+P+R).(G+P+S).(G+P+T).(G+Q+R).(G+Q+S).(G+Q+T).(G+R+S).(G+R+T).(G+S+T).(H+I+J).(H+I+K).(H+I+L).(H+I+M).(H+I+N).(H+I+O).(H+I+P).(H+I+Q).(H+I+R).(H+I+S).(H+I+T).(H+J+K).(H+J+L).(H+J+M).(H+J+N).(H+J+O).(H+J+P).(H+J+Q).(H+J+R).(H+J+S).(H+J+T).(H+K+L).(H+K+M).(H+K+N).(H+K+O).(H+K+P).(H+K+Q).(H+K+R).(H+K+S).(H+K+T).(H+L+M).(H+L+N).(H+L+O).(H+L+P).(H+L+Q).(H+L+R).(H+L+S).(H+L+T).(H+M+N).(H+M+O).(H+M+P).(H+M+Q).(H+M+R).(H+M+S).(H+M+T).(H+N+O).(H+N+P).(H+N+Q).(H+N+R).(H+N+S).(H+N+T).(H+O+P).(H+O+Q).(H+O+R).(H+O+S).(H+O+T).(H+P+Q).(H+P+R).(H+P+S).(H+P+T).(H+Q+R).(H+Q+S).(H+Q+T).(H+R+S).(H+R+T).(H+S+T).(I+J+K).(I+J+L).(I+J+M).(I+J+N).(I+J+O).(I+J+P).(I+J+Q).(I+J+R).(I+J+S).(I+J+T).(I+K+L).(I+K+M).(I+K+N).(I+K+O).(I+K+P).(I+K+Q).(I+K+R).(I+K+S).(I+K+T).(I+L+M).(I+L+N).(I+L+O).(I+L+P).(I+L+Q).(I+L+R).(I+L+S).(I+L+T).(I+M+N).(I+M+O).(I+M+P).(I+M+Q).(I+M+R).(I+M+S).(I+M+T).(I+N+O).(I+N+P).(I+N+Q).(I+N+R).(I+N+S).(I+N+T).(I+O+P).(I+O+Q).(I+O+R).(I+O+S).(I+O+T).(I+P+Q).(I+P+R).(I+P+S).(I+P+T).(I+Q+R).(I+Q+S).(I+Q+T).(I+R+S).(I+R+T).(I+S+T).(J+K+L).(J+K+M).(J+K+N).(J+K+O).(J+K+P).(J+K+Q).(J+K+R).(J+K+S).(J+K+T).(J+L+M).(J+L+N).(J+L+O).(J+L+P).(J+L+Q).(J+L+R).(J+L+S).(J+L+T).(J+M+N).(J+M+O).(J+M+P).(J+M+Q).(J+M+R).(J+M+S).(J+M+T).(J+N+O).(J+N+P).(J+N+Q).(J+N+R).(J+N+S).(J+N+T).(J+O+P).(J+O+Q).(J+O+R).(J+O+S).(J+O+T).(J+P+Q).(J+P+R).(J+P+S).(J+P+T).(J+Q+R).(J+Q+S).(J+Q+T).(J+R+S).(J+R+T).(J+S+T).(K+L+M).(K+L+N).(K+L+O).(K+L+P).(K+L+Q).(K+L+R).(K+L+S).(K+L+T).(K+M+N).(K+M+O).(K+M+P).(K+M+Q).(K+M+R).(K+M+S).(K+M+T).(K+N+O).(K+N+P).(K+N+Q).(K+N+R).(K+N+S).(K+N+T).(K+O+P).(K+O+Q).(K+O+R).(K+O+S).(K+O+T).(K+P+Q).(K+P+R).(K+P+S).(K+P+T).(K+Q+R).(K+Q+S).(K+Q+T).(K+R+S).(K+R+T).(K+S+T).(L+M+N).(L+M+O).(L+M+P).(L+M+Q).(L+M+R).(L+M+S).(L+M+T).(L+N+O).(L+N+P).(L+N+Q).(L+N+R).(L+N+S).(L+N+T).(L+O+P).(L+O+Q).(L+O+R).(L+O+S).(L+O+T).(L+P+Q).(L+P+R).(L+P+S).(L+P+T).(L+Q+R).(L+Q+S).(L+Q+T).(L+R+S).(L+R+T).(L+S+T).(M+N+O).(M+N+P).(M+N+Q).(M+N+R).(M+N+S).(M+N+T).(M+O+P).(M+O+Q).(M+O+R).(M+O+S).(M+O+T).(M+P+Q).(M+P+R).(M+P+S).(M+P+T).(M+Q+R).(M+Q+S).(M+Q+T).(M+R+S).(M+R+T).(M+S+T).(N+O+P).(N+O+Q).(N+O+R).(N+O+S).(N+O+T).(N+P+Q).(N+P+R).(N+P+S).(N+P+T).(N+Q+R).(N+Q+S).(N+Q+T).(N+R+S).(N+R+T).(N+S+T).(O+P+Q).(O+P+R).(O+P+S).(O+P+T).(O+Q+R).(O+Q+S).(O+Q+T).(O+R+S).(O+R+T).(O+S+T).(P+Q+R).(P+Q+S).(P+Q+T).(P+R+S).(P+R+T).(P+S+T).(Q+R+S).(Q+R+T).(Q+S+T).(R+S+T).(¬A+¬B+¬C).(¬A+¬B+¬D).(¬A+¬B+¬E).(¬A+¬B+¬F).(¬A+¬B+¬G).(¬A+¬B+¬H).(¬A+¬B+¬I).(¬A+¬B+¬J).(¬A+¬B+¬K).(¬A+¬B+¬L).(¬A+¬B+¬M).(¬A+¬B+¬N).(¬A+¬B+¬O).(¬A+¬B+¬P).(¬A+¬B+¬Q).(¬A+¬B+¬R).(¬A+¬B+¬S).(¬A+¬B+¬T).(¬A+¬C+¬D).(¬A+¬C+¬E).(¬A+¬C+¬F).(¬A+¬C+¬G).(¬A+¬C+¬H).(¬A+¬C+¬I).(¬A+¬C+¬J).(¬A+¬C+¬K).(¬A+¬C+¬L).(¬A+¬C+¬M).(¬A+¬C+¬N).(¬A+¬C+¬O).(¬A+¬C+¬P).(¬A+¬C+¬Q).(¬A+¬C+¬R).(¬A+¬C+¬S).(¬A+¬C+¬T).(¬A+¬D+¬E).(¬A+¬D+¬F).(¬A+¬D+¬G).(¬A+¬D+¬H).(¬A+¬D+¬I).(¬A+¬D+¬J).(¬A+¬D+¬K).(¬A+¬D+¬L).(¬A+¬D+¬M).(¬A+¬D+¬N).(¬A+¬D+¬O).(¬A+¬D+¬P).(¬A+¬D+¬Q).(¬A+¬D+¬R).(¬A+¬D+¬S).(¬A+¬D+¬T).(¬A+¬E+¬F).(¬A+¬E+¬G).(¬A+¬E+¬H).(¬A+¬E+¬I).(¬A+¬E+¬J).(¬A+¬E+¬K).(¬A+¬E+¬L).(¬A+¬E+¬M).(¬A+¬E+¬N).(¬A+¬E+¬O).(¬A+¬E+¬P).(¬A+¬E+¬Q).(¬A+¬E+¬R).(¬A+¬E+¬S).(¬A+¬E+¬T).(¬A+¬F+¬G).(¬A+¬F+¬H).(¬A+¬F+¬I).(¬A+¬F+¬J).(¬A+¬F+¬K).(¬A+¬F+¬L).(¬A+¬F+¬M).(¬A+¬F+¬N).(¬A+¬F+¬O).(¬A+¬F+¬P).(¬A+¬F+¬Q).(¬A+¬F+¬R).(¬A+¬F+¬S).(¬A+¬F+¬T).(¬A+¬G+¬H).(¬A+¬G+¬I).(¬A+¬G+¬J).(¬A+¬G+¬K).(¬A+¬G+¬L).(¬A+¬G+¬M).(¬A+¬G+¬N).(¬A+¬G+¬O).(¬A+¬G+¬P).(¬A+¬G+¬Q).(¬A+¬G+¬R).(¬A+¬G+¬S).(¬A+¬G+¬T).(¬A+¬H+¬I).(¬A+¬H+¬J).(¬A+¬H+¬K).(¬A+¬H+¬L).(¬A+¬H+¬M).(¬A+¬H+¬N).(¬A+¬H+¬O).(¬A+¬H+¬P).(¬A+¬H+¬Q).(¬A+¬H+¬R).(¬A+¬H+¬S).(¬A+¬H+¬T).(¬A+¬I+¬J).(¬A+¬I+¬K).(¬A+¬I+¬L).(¬A+¬I+¬M).(¬A+¬I+¬N).(¬A+¬I+¬O).(¬A+¬I+¬P).(¬A+¬I+¬Q).(¬A+¬I+¬R).(¬A+¬I+¬S).(¬A+¬I+¬T).(¬A+¬J+¬K).(¬A+¬J+¬L).(¬A+¬J+¬M).(¬A+¬J+¬N).(¬A+¬J+¬O).(¬A+¬J+¬P).(¬A+¬J+¬Q).(¬A+¬J+¬R).(¬A+¬J+¬S).(¬A+¬J+¬T).(¬A+¬K+¬L).(¬A+¬K+¬M).(¬A+¬K+¬N).(¬A+¬K+¬O).(¬A+¬K+¬P).(¬A+¬K+¬Q).(¬A+¬K+¬R).(¬A+¬K+¬S).(¬A+¬K+¬T).(¬A+¬L+¬M).(¬A+¬L+¬N).(¬A+¬L+¬O).(¬A+¬L+¬P).(¬A+¬L+¬Q).(¬A+¬L+¬R).(¬A+¬L+¬S).(¬A+¬L+¬T).(¬A+¬M+¬N).(¬A+¬M+¬O).(¬A+¬M+¬P).(¬A+¬M+¬Q).(¬A+¬M+¬R).(¬A+¬M+¬S).(¬A+¬M+¬T).(¬A+¬N+¬O).(¬A+¬N+¬P).(¬A+¬N+¬Q).(¬A+¬N+¬R).(¬A+¬N+¬S).(¬A+¬N+¬T).(¬A+¬O+¬P).(¬A+¬O+¬Q).(¬A+¬O+¬R).(¬A+¬O+¬S).(¬A+¬O+¬T).(¬A+¬P+¬Q).(¬A+¬P+¬R).(¬A+¬P+¬S).(¬A+¬P+¬T).(¬A+¬Q+¬R).(¬A+¬Q+¬S).(¬A+¬Q+¬T).(¬A+¬R+¬S).(¬A+¬R+¬T).(¬A+¬S+¬T).(¬B+¬C+¬D).(¬B+¬C+¬E).(¬B+¬C+¬F).(¬B+¬C+¬G).(¬B+¬C+¬H).(¬B+¬C+¬I).(¬B+¬C+¬J).(¬B+¬C+¬K).(¬B+¬C+¬L).(¬B+¬C+¬M).(¬B+¬C+¬N).(¬B+¬C+¬O).(¬B+¬C+¬P).(¬B+¬C+¬Q).(¬B+¬C+¬R).(¬B+¬C+¬S).(¬B+¬C+¬T).(¬B+¬D+¬E).(¬B+¬D+¬F).(¬B+¬D+¬G).(¬B+¬D+¬H).(¬B+¬D+¬I).(¬B+¬D+¬J).(¬B+¬D+¬K).(¬B+¬D+¬L).(¬B+¬D+¬M).(¬B+¬D+¬N).(¬B+¬D+¬O).(¬B+¬D+¬P).(¬B+¬D+¬Q).(¬B+¬D+¬R).(¬B+¬D+¬S).(¬B+¬D+¬T).(¬B+¬E+¬F).(¬B+¬E+¬G).(¬B+¬E+¬H).(¬B+¬E+¬I).(¬B+¬E+¬J).(¬B+¬E+¬K).(¬B+¬E+¬L).(¬B+¬E+¬M).(¬B+¬E+¬N).(¬B+¬E+¬O).(¬B+¬E+¬P).(¬B+¬E+¬Q).(¬B+¬E+¬R).(¬B+¬E+¬S).(¬B+¬E+¬T).(¬B+¬F+¬G).(¬B+¬F+¬H).(¬B+¬F+¬I).(¬B+¬F+¬J).(¬B+¬F+¬K).(¬B+¬F+¬L).(¬B+¬F+¬M).(¬B+¬F+¬N).(¬B+¬F+¬O).(¬B+¬F+¬P).(¬B+¬F+¬Q).(¬B+¬F+¬R).(¬B+¬F+¬S).(¬B+¬F+¬T).(¬B+¬G+¬H).(¬B+¬G+¬I).(¬B+¬G+¬J).(¬B+¬G+¬K).(¬B+¬G+¬L).(¬B+¬G+¬M).(¬B+¬G+¬N).(¬B+¬G+¬O).(¬B+¬G+¬P).(¬B+¬G+¬Q).(¬B+¬G+¬R).(¬B+¬G+¬S).(¬B+¬G+¬T).(¬B+¬H+¬I).(¬B+¬H+¬J).(¬B+¬H+¬K).(¬B+¬H+¬L).(¬B+¬H+¬M).(¬B+¬H+¬N).(¬B+¬H+¬O).(¬B+¬H+¬P).(¬B+¬H+¬Q).(¬B+¬H+¬R).(¬B+¬H+¬S).(¬B+¬H+¬T).(¬B+¬I+¬J).(¬B+¬I+¬K).(¬B+¬I+¬L).(¬B+¬I+¬M).(¬B+¬I+¬N).(¬B+¬I+¬O).(¬B+¬I+¬P).(¬B+¬I+¬Q).(¬B+¬I+¬R).(¬B+¬I+¬S).(¬B+¬I+¬T).(¬B+¬J+¬K).(¬B+¬J+¬L).(¬B+¬J+¬M).(¬B+¬J+¬N).(¬B+¬J+¬O).(¬B+¬J+¬P).(¬B+¬J+¬Q).(¬B+¬J+¬R).(¬B+¬J+¬S).(¬B+¬J+¬T).(¬B+¬K+¬L).(¬B+¬K+¬M).(¬B+¬K+¬N).(¬B+¬K+¬O).(¬B+¬K+¬P).(¬B+¬K+¬Q).(¬B+¬K+¬R).(¬B+¬K+¬S).(¬B+¬K+¬T).(¬B+¬L+¬M).(¬B+¬L+¬N).(¬B+¬L+¬O).(¬B+¬L+¬P).(¬B+¬L+¬Q).(¬B+¬L+¬R).(¬B+¬L+¬S).(¬B+¬L+¬T).(¬B+¬M+¬N).(¬B+¬M+¬O).(¬B+¬M+¬P).(¬B+¬M+¬Q).(¬B+¬M+¬R).(¬B+¬M+¬S).(¬B+¬M+¬T).(¬B+¬N+¬O).(¬B+¬N+¬P).(¬B+¬N+¬Q).(¬B+¬N+¬R).(¬B+¬N+¬S).(¬B+¬N+¬T).(¬B+¬O+¬P).(¬B+¬O+¬Q).(¬B+¬O+¬R).(¬B+¬O+¬S).(¬B+¬O+¬T).(¬B+¬P+¬Q).(¬B+¬P+¬R).(¬B+¬P+¬S).(¬B+¬P+¬T).(¬B+¬Q+¬R).(¬B+¬Q+¬S).(¬B+¬Q+¬T).(¬B+¬R+¬S).(¬B+¬R+¬T).(¬B+¬S+¬T).(¬C+¬D+¬E).(¬C+¬D+¬F).(¬C+¬D+¬G).(¬C+¬D+¬H).(¬C+¬D+¬I).(¬C+¬D+¬J).(¬C+¬D+¬K).(¬C+¬D+¬L).(¬C+¬D+¬M).(¬C+¬D+¬N).(¬C+¬D+¬O).(¬C+¬D+¬P).(¬C+¬D+¬Q).(¬C+¬D+¬R).(¬C+¬D+¬S).(¬C+¬D+¬T).(¬C+¬E+¬F).(¬C+¬E+¬G).(¬C+¬E+¬H).(¬C+¬E+¬I).(¬C+¬E+¬J).(¬C+¬E+¬K).(¬C+¬E+¬L).(¬C+¬E+¬M).(¬C+¬E+¬N).(¬C+¬E+¬O).(¬C+¬E+¬P).(¬C+¬E+¬Q).(¬C+¬E+¬R).(¬C+¬E+¬S).(¬C+¬E+¬T).(¬C+¬F+¬G).(¬C+¬F+¬H).(¬C+¬F+¬I).(¬C+¬F+¬J).(¬C+¬F+¬K).(¬C+¬F+¬L).(¬C+¬F+¬M).(¬C+¬F+¬N).(¬C+¬F+¬O).(¬C+¬F+¬P).(¬C+¬F+¬Q).(¬C+¬F+¬R).(¬C+¬F+¬S).(¬C+¬F+¬T).(¬C+¬G+¬H).(¬C+¬G+¬I).(¬C+¬G+¬J).(¬C+¬G+¬K).(¬C+¬G+¬L).(¬C+¬G+¬M).(¬C+¬G+¬N).(¬C+¬G+¬O).(¬C+¬G+¬P).(¬C+¬G+¬Q).(¬C+¬G+¬R).(¬C+¬G+¬S).(¬C+¬G+¬T).(¬C+¬H+¬I).(¬C+¬H+¬J).(¬C+¬H+¬K).(¬C+¬H+¬L).(¬C+¬H+¬M).(¬C+¬H+¬N).(¬C+¬H+¬O).(¬C+¬H+¬P).(¬C+¬H+¬Q).(¬C+¬H+¬R).(¬C+¬H+¬S).(¬C+¬H+¬T).(¬C+¬I+¬J).(¬C+¬I+¬K).(¬C+¬I+¬L).(¬C+¬I+¬M).(¬C+¬I+¬N).(¬C+¬I+¬O).(¬C+¬I+¬P).(¬C+¬I+¬Q).(¬C+¬I+¬R).(¬C+¬I+¬S).(¬C+¬I+¬T).(¬C+¬J+¬K).(¬C+¬J+¬L).(¬C+¬J+¬M).(¬C+¬J+¬N).(¬C+¬J+¬O).(¬C+¬J+¬P).(¬C+¬J+¬Q).(¬C+¬J+¬R).(¬C+¬J+¬S).(¬C+¬J+¬T).(¬C+¬K+¬L).(¬C+¬K+¬M).(¬C+¬K+¬N).(¬C+¬K+¬O).(¬C+¬K+¬P).(¬C+¬K+¬Q).(¬C+¬K+¬R).(¬C+¬K+¬S).(¬C+¬K+¬T).(¬C+¬L+¬M).(¬C+¬L+¬N).(¬C+¬L+¬O).(¬C+¬L+¬P).(¬C+¬L+¬Q).(¬C+¬L+¬R).(¬C+¬L+¬S).(¬C+¬L+¬T).(¬C+¬M+¬N).(¬C+¬M+¬O).(¬C+¬M+¬P).(¬C+¬M+¬Q).(¬C+¬M+¬R).(¬C+¬M+¬S).(¬C+¬M+¬T).(¬C+¬N+¬O).(¬C+¬N+¬P).(¬C+¬N+¬Q).(¬C+¬N+¬R).(¬C+¬N+¬S).(¬C+¬N+¬T).(¬C+¬O+¬P).(¬C+¬O+¬Q).(¬C+¬O+¬R).(¬C+¬O+¬S).(¬C+¬O+¬T).(¬C+¬P+¬Q).(¬C+¬P+¬R).(¬C+¬P+¬S).(¬C+¬P+¬T).(¬C+¬Q+¬R).(¬C+¬Q+¬S).(¬C+¬Q+¬T).(¬C+¬R+¬S).(¬C+¬R+¬T).(¬C+¬S+¬T).(¬D+¬E+¬F).(¬D+¬E+¬G).(¬D+¬E+¬H).(¬D+¬E+¬I).(¬D+¬E+¬J).(¬D+¬E+¬K).(¬D+¬E+¬L).(¬D+¬E+¬M).(¬D+¬E+¬N).(¬D+¬E+¬O).(¬D+¬E+¬P).(¬D+¬E+¬Q).(¬D+¬E+¬R).(¬D+¬E+¬S).(¬D+¬E+¬T).(¬D+¬F+¬G).(¬D+¬F+¬H).(¬D+¬F+¬I).(¬D+¬F+¬J).(¬D+¬F+¬K).(¬D+¬F+¬L).(¬D+¬F+¬M).(¬D+¬F+¬N).(¬D+¬F+¬O).(¬D+¬F+¬P).(¬D+¬F+¬Q).(¬D+¬F+¬R).(¬D+¬F+¬S).(¬D+¬F+¬T).(¬D+¬G+¬H).(¬D+¬G+¬I).(¬D+¬G+¬J).(¬D+¬G+¬K).(¬D+¬G+¬L).(¬D+¬G+¬M).(¬D+¬G+¬N).(¬D+¬G+¬O).(¬D+¬G+¬P).(¬D+¬G+¬Q).(¬D+¬G+¬R).(¬D+¬G+¬S).(¬D+¬G+¬T).(¬D+¬H+¬I).(¬D+¬H+¬J).(¬D+¬H+¬K).(¬D+¬H+¬L).(¬D+¬H+¬M).(¬D+¬H+¬N).(¬D+¬H+¬O).(¬D+¬H+¬P).(¬D+¬H+¬Q).(¬D+¬H+¬R).(¬D+¬H+¬S).(¬D+¬H+¬T).(¬D+¬I+¬J).(¬D+¬I+¬K).(¬D+¬I+¬L).(¬D+¬I+¬M).(¬D+¬I+¬N).(¬D+¬I+¬O).(¬D+¬I+¬P).(¬D+¬I+¬Q).(¬D+¬I+¬R).(¬D+¬I+¬S).(¬D+¬I+¬T).(¬D+¬J+¬K).(¬D+¬J+¬L).(¬D+¬J+¬M).(¬D+¬J+¬N).(¬D+¬J+¬O).(¬D+¬J+¬P).(¬D+¬J+¬Q).(¬D+¬J+¬R).(¬D+¬J+¬S).(¬D+¬J+¬T).(¬D+¬K+¬L).(¬D+¬K+¬M).(¬D+¬K+¬N).(¬D+¬K+¬O).(¬D+¬K+¬P).(¬D+¬K+¬Q).(¬D+¬K+¬R).(¬D+¬K+¬S).(¬D+¬K+¬T).(¬D+¬L+¬M).(¬D+¬L+¬N).(¬D+¬L+¬O).(¬D+¬L+¬P).(¬D+¬L+¬Q).(¬D+¬L+¬R).(¬D+¬L+¬S).(¬D+¬L+¬T).(¬D+¬M+¬N).(¬D+¬M+¬O).(¬D+¬M+¬P).(¬D+¬M+¬Q).(¬D+¬M+¬R).(¬D+¬M+¬S).(¬D+¬M+¬T).(¬D+¬N+¬O).(¬D+¬N+¬P).(¬D+¬N+¬Q).(¬D+¬N+¬R).(¬D+¬N+¬S).(¬D+¬N+¬T).(¬D+¬O+¬P).(¬D+¬O+¬Q).(¬D+¬O+¬R).(¬D+¬O+¬S).(¬D+¬O+¬T).(¬D+¬P+¬Q).(¬D+¬P+¬R).(¬D+¬P+¬S).(¬D+¬P+¬T).(¬D+¬Q+¬R).(¬D+¬Q+¬S).(¬D+¬Q+¬T).(¬D+¬R+¬S).(¬D+¬R+¬T).(¬D+¬S+¬T).(¬E+¬F+¬G).(¬E+¬F+¬H).(¬E+¬F+¬I).(¬E+¬F+¬J).(¬E+¬F+¬K).(¬E+¬F+¬L).(¬E+¬F+¬M).(¬E+¬F+¬N).(¬E+¬F+¬O).(¬E+¬F+¬P).(¬E+¬F+¬Q).(¬E+¬F+¬R).(¬E+¬F+¬S).(¬E+¬F+¬T).(¬E+¬G+¬H).(¬E+¬G+¬I).(¬E+¬G+¬J).(¬E+¬G+¬K).(¬E+¬G+¬L).(¬E+¬G+¬M).(¬E+¬G+¬N).(¬E+¬G+¬O).(¬E+¬G+¬P).(¬E+¬G+¬Q).(¬E+¬G+¬R).(¬E+¬G+¬S).(¬E+¬G+¬T).(¬E+¬H+¬I).(¬E+¬H+¬J).(¬E+¬H+¬K).(¬E+¬H+¬L).(¬E+¬H+¬M).(¬E+¬H+¬N).(¬E+¬H+¬O).(¬E+¬H+¬P).(¬E+¬H+¬Q).(¬E+¬H+¬R).(¬E+¬H+¬S).(¬E+¬H+¬T).(¬E+¬I+¬J).(¬E+¬I+¬K).(¬E+¬I+¬L).(¬E+¬I+¬M).(¬E+¬I+¬N).(¬E+¬I+¬O).(¬E+¬I+¬P).(¬E+¬I+¬Q).(¬E+¬I+¬R).(¬E+¬I+¬S).(¬E+¬I+¬T).(¬E+¬J+¬K).(¬E+¬J+¬L).(¬E+¬J+¬M).(¬E+¬J+¬N).(¬E+¬J+¬O).(¬E+¬J+¬P).(¬E+¬J+¬Q).(¬E+¬J+¬R).(¬E+¬J+¬S).(¬E+¬J+¬T).(¬E+¬K+¬L).(¬E+¬K+¬M).(¬E+¬K+¬N).(¬E+¬K+¬O).(¬E+¬K+¬P).(¬E+¬K+¬Q).(¬E+¬K+¬R).(¬E+¬K+¬S).(¬E+¬K+¬T).(¬E+¬L+¬M).(¬E+¬L+¬N).(¬E+¬L+¬O).(¬E+¬L+¬P).(¬E+¬L+¬Q).(¬E+¬L+¬R).(¬E+¬L+¬S).(¬E+¬L+¬T).(¬E+¬M+¬N).(¬E+¬M+¬O).(¬E+¬M+¬P).(¬E+¬M+¬Q).(¬E+¬M+¬R).(¬E+¬M+¬S).(¬E+¬M+¬T).(¬E+¬N+¬O).(¬E+¬N+¬P).(¬E+¬N+¬Q).(¬E+¬N+¬R).(¬E+¬N+¬S).(¬E+¬N+¬T).(¬E+¬O+¬P).(¬E+¬O+¬Q).(¬E+¬O+¬R).(¬E+¬O+¬S).(¬E+¬O+¬T).(¬E+¬P+¬Q).(¬E+¬P+¬R).(¬E+¬P+¬S).(¬E+¬P+¬T).(¬E+¬Q+¬R).(¬E+¬Q+¬S).(¬E+¬Q+¬T).(¬E+¬R+¬S).(¬E+¬R+¬T).(¬E+¬S+¬T).(¬F+¬G+¬H).(¬F+¬G+¬I).(¬F+¬G+¬J).(¬F+¬G+¬K).(¬F+¬G+¬L).(¬F+¬G+¬M).(¬F+¬G+¬N).(¬F+¬G+¬O).(¬F+¬G+¬P).(¬F+¬G+¬Q).(¬F+¬G+¬R).(¬F+¬G+¬S).(¬F+¬G+¬T).(¬F+¬H+¬I).(¬F+¬H+¬J).(¬F+¬H+¬K).(¬F+¬H+¬L).(¬F+¬H+¬M).(¬F+¬H+¬N).(¬F+¬H+¬O).(¬F+¬H+¬P).(¬F+¬H+¬Q).(¬F+¬H+¬R).(¬F+¬H+¬S).(¬F+¬H+¬T).(¬F+¬I+¬J).(¬F+¬I+¬K).(¬F+¬I+¬L).(¬F+¬I+¬M).(¬F+¬I+¬N).(¬F+¬I+¬O).(¬F+¬I+¬P).(¬F+¬I+¬Q).(¬F+¬I+¬R).(¬F+¬I+¬S).(¬F+¬I+¬T).(¬F+¬J+¬K).(¬F+¬J+¬L).(¬F+¬J+¬M).(¬F+¬J+¬N).(¬F+¬J+¬O).(¬F+¬J+¬P).(¬F+¬J+¬Q).(¬F+¬J+¬R).(¬F+¬J+¬S).(¬F+¬J+¬T).(¬F+¬K+¬L).(¬F+¬K+¬M).(¬F+¬K+¬N).(¬F+¬K+¬O).(¬F+¬K+¬P).(¬F+¬K+¬Q).(¬F+¬K+¬R).(¬F+¬K+¬S).(¬F+¬K+¬T).(¬F+¬L+¬M).(¬F+¬L+¬N).(¬F+¬L+¬O).(¬F+¬L+¬P).(¬F+¬L+¬Q).(¬F+¬L+¬R).(¬F+¬L+¬S).(¬F+¬L+¬T).(¬F+¬M+¬N).(¬F+¬M+¬O).(¬F+¬M+¬P).(¬F+¬M+¬Q).(¬F+¬M+¬R).(¬F+¬M+¬S).(¬F+¬M+¬T).(¬F+¬N+¬O).(¬F+¬N+¬P).(¬F+¬N+¬Q).(¬F+¬N+¬R).(¬F+¬N+¬S).(¬F+¬N+¬T).(¬F+¬O+¬P).(¬F+¬O+¬Q).(¬F+¬O+¬R).(¬F+¬O+¬S).(¬F+¬O+¬T).(¬F+¬P+¬Q).(¬F+¬P+¬R).(¬F+¬P+¬S).(¬F+¬P+¬T).(¬F+¬Q+¬R).(¬F+¬Q+¬S).(¬F+¬Q+¬T).(¬F+¬R+¬S).(¬F+¬R+¬T).(¬F+¬S+¬T).(¬G+¬H+¬I).(¬G+¬H+¬J).(¬G+¬H+¬K).(¬G+¬H+¬L).(¬G+¬H+¬M).(¬G+¬H+¬N).(¬G+¬H+¬O).(¬G+¬H+¬P).(¬G+¬H+¬Q).(¬G+¬H+¬R).(¬G+¬H+¬S).(¬G+¬H+¬T).(¬G+¬I+¬J).(¬G+¬I+¬K).(¬G+¬I+¬L).(¬G+¬I+¬M).(¬G+¬I+¬N).(¬G+¬I+¬O).(¬G+¬I+¬P).(¬G+¬I+¬Q).(¬G+¬I+¬R).(¬G+¬I+¬S).(¬G+¬I+¬T).(¬G+¬J+¬K).(¬G+¬J+¬L).(¬G+¬J+¬M).(¬G+¬J+¬N).(¬G+¬J+¬O).(¬G+¬J+¬P).(¬G+¬J+¬Q).(¬G+¬J+¬R).(¬G+¬J+¬S).(¬G+¬J+¬T).(¬G+¬K+¬L).(¬G+¬K+¬M).(¬G+¬K+¬N).(¬G+¬K+¬O).(¬G+¬K+¬P).(¬G+¬K+¬Q).(¬G+¬K+¬R).(¬G+¬K+¬S).(¬G+¬K+¬T).(¬G+¬L+¬M).(¬G+¬L+¬N).(¬G+¬L+¬O).(¬G+¬L+¬P).(¬G+¬L+¬Q).(¬G+¬L+¬R).(¬G+¬L+¬S).(¬G+¬L+¬T).(¬G+¬M+¬N).(¬G+¬M+¬O).(¬G+¬M+¬P).(¬G+¬M+¬Q).(¬G+¬M+¬R).(¬G+¬M+¬S).(¬G+¬M+¬T).(¬G+¬N+¬O).(¬G+¬N+¬P).(¬G+¬N+¬Q).(¬G+¬N+¬R).(¬G+¬N+¬S).(¬G+¬N+¬T).(¬G+¬O+¬P).(¬G+¬O+¬Q).(¬G+¬O+¬R).(¬G+¬O+¬S).(¬G+¬O+¬T).(¬G+¬P+¬Q).(¬G+¬P+¬R).(¬G+¬P+¬S).(¬G+¬P+¬T).(¬G+¬Q+¬R).(¬G+¬Q+¬S).(¬G+¬Q+¬T).(¬G+¬R+¬S).(¬G+¬R+¬T).(¬G+¬S+¬T).(¬H+¬I+¬J).(¬H+¬I+¬K).(¬H+¬I+¬L).(¬H+¬I+¬M).(¬H+¬I+¬N).(¬H+¬I+¬O).(¬H+¬I+¬P).(¬H+¬I+¬Q).(¬H+¬I+¬R).(¬H+¬I+¬S).(¬H+¬I+¬T).(¬H+¬J+¬K).(¬H+¬J+¬L).(¬H+¬J+¬M).(¬H+¬J+¬N).(¬H+¬J+¬O).(¬H+¬J+¬P).(¬H+¬J+¬Q).(¬H+¬J+¬R).(¬H+¬J+¬S).(¬H+¬J+¬T).(¬H+¬K+¬L).(¬H+¬K+¬M).(¬H+¬K+¬N).(¬H+¬K+¬O).(¬H+¬K+¬P).(¬H+¬K+¬Q).(¬H+¬K+¬R).(¬H+¬K+¬S).(¬H+¬K+¬T).(¬H+¬L+¬M).(¬H+¬L+¬N).(¬H+¬L+¬O).(¬H+¬L+¬P).(¬H+¬L+¬Q).(¬H+¬L+¬R).(¬H+¬L+¬S).(¬H+¬L+¬T).(¬H+¬M+¬N).(¬H+¬M+¬O).(¬H+¬M+¬P).(¬H+¬M+¬Q).(¬H+¬M+¬R).(¬H+¬M+¬S).(¬H+¬M+¬T).(¬H+¬N+¬O).(¬H+¬N+¬P).(¬H+¬N+¬Q).(¬H+¬N+¬R).(¬H+¬N+¬S).(¬H+¬N+¬T).(¬H+¬O+¬P).(¬H+¬O+¬Q).(¬H+¬O+¬R).(¬H+¬O+¬S).(¬H+¬O+¬T).(¬H+¬P+¬Q).(¬H+¬P+¬R).(¬H+¬P+¬S).(¬H+¬P+¬T).(¬H+¬Q+¬R).(¬H+¬Q+¬S).(¬H+¬Q+¬T).(¬H+¬R+¬S).(¬H+¬R+¬T).(¬H+¬S+¬T).(¬I+¬J+¬K).(¬I+¬J+¬L).(¬I+¬J+¬M).(¬I+¬J+¬N).(¬I+¬J+¬O).(¬I+¬J+¬P).(¬I+¬J+¬Q).(¬I+¬J+¬R).(¬I+¬J+¬S).(¬I+¬J+¬T).(¬I+¬K+¬L).(¬I+¬K+¬M).(¬I+¬K+¬N).(¬I+¬K+¬O).(¬I+¬K+¬P).(¬I+¬K+¬Q).(¬I+¬K+¬R).(¬I+¬K+¬S).(¬I+¬K+¬T).(¬I+¬L+¬M).(¬I+¬L+¬N).(¬I+¬L+¬O).(¬I+¬L+¬P).(¬I+¬L+¬Q).(¬I+¬L+¬R).(¬I+¬L+¬S).(¬I+¬L+¬T).(¬I+¬M+¬N).(¬I+¬M+¬O).(¬I+¬M+¬P).(¬I+¬M+¬Q).(¬I+¬M+¬R).(¬I+¬M+¬S).(¬I+¬M+¬T).(¬I+¬N+¬O).(¬I+¬N+¬P).(¬I+¬N+¬Q).(¬I+¬N+¬R).(¬I+¬N+¬S).(¬I+¬N+¬T).(¬I+¬O+¬P).(¬I+¬O+¬Q).(¬I+¬O+¬R).(¬I+¬O+¬S).(¬I+¬O+¬T).(¬I+¬P+¬Q).(¬I+¬P+¬R).(¬I+¬P+¬S).(¬I+¬P+¬T).(¬I+¬Q+¬R).(¬I+¬Q+¬S).(¬I+¬Q+¬T).(¬I+¬R+¬S).(¬I+¬R+¬T).(¬I+¬S+¬T).(¬J+¬K+¬L).(¬J+¬K+¬M).(¬J+¬K+¬N).(¬J+¬K+¬O).(¬J+¬K+¬P).(¬J+¬K+¬Q).(¬J+¬K+¬R).(¬J+¬K+¬S).(¬J+¬K+¬T).(¬J+¬L+¬M).(¬J+¬L+¬N).(¬J+¬L+¬O).(¬J+¬L+¬P).(¬J+¬L+¬Q).(¬J+¬L+¬R).(¬J+¬L+¬S).(¬J+¬L+¬T).(¬J+¬M+¬N).(¬J+¬M+¬O).(¬J+¬M+¬P).(¬J+¬M+¬Q).(¬J+¬M+¬R).(¬J+¬M+¬S).(¬J+¬M+¬T).(¬J+¬N+¬O).(¬J+¬N+¬P).(¬J+¬N+¬Q).(¬J+¬N+¬R).(¬J+¬N+¬S).(¬J+¬N+¬T).(¬J+¬O+¬P).(¬J+¬O+¬Q).(¬J+¬O+¬R).(¬J+¬O+¬S).(¬J+¬O+¬T).(¬J+¬P+¬Q).(¬J+¬P+¬R).(¬J+¬P+¬S).(¬J+¬P+¬T).(¬J+¬Q+¬R).(¬J+¬Q+¬S).(¬J+¬Q+¬T).(¬J+¬R+¬S).(¬J+¬R+¬T).(¬J+¬S+¬T).(¬K+¬L+¬M).(¬K+¬L+¬N).(¬K+¬L+¬O).(¬K+¬L+¬P).(¬K+¬L+¬Q).(¬K+¬L+¬R).(¬K+¬L+¬S).(¬K+¬L+¬T).(¬K+¬M+¬N).(¬K+¬M+¬O).(¬K+¬M+¬P).(¬K+¬M+¬Q).(¬K+¬M+¬R).(¬K+¬M+¬S).(¬K+¬M+¬T).(¬K+¬N+¬O).(¬K+¬N+¬P).(¬K+¬N+¬Q).(¬K+¬N+¬R).(¬K+¬N+¬S).(¬K+¬N+¬T).(¬K+¬O+¬P).(¬K+¬O+¬Q).(¬K+¬O+¬R).(¬K+¬O+¬S).(¬K+¬O+¬T).(¬K+¬P+¬Q).(¬K+¬P+¬R).(¬K+¬P+¬S).(¬K+¬P+¬T).(¬K+¬Q+¬R).(¬K+¬Q+¬S).(¬K+¬Q+¬T).(¬K+¬R+¬S).(¬K+¬R+¬T).(¬K+¬S+¬T).(¬L+¬M+¬N).(¬L+¬M+¬O).(¬L+¬M+¬P).(¬L+¬M+¬Q).(¬L+¬M+¬R).(¬L+¬M+¬S).(¬L+¬M+¬T).(¬L+¬N+¬O).(¬L+¬N+¬P).(¬L+¬N+¬Q).(¬L+¬N+¬R).(¬L+¬N+¬S).(¬L+¬N+¬T).(¬L+¬O+¬P).(¬L+¬O+¬Q).(¬L+¬O+¬R).(¬L+¬O+¬S).(¬L+¬O+¬T).(¬L+¬P+¬Q).(¬L+¬P+¬R).(¬L+¬P+¬S).(¬L+¬P+¬T).(¬L+¬Q+¬R).(¬L+¬Q+¬S).(¬L+¬Q+¬T).(¬L+¬R+¬S).(¬L+¬R+¬T).(¬L+¬S+¬T).(¬M+¬N+¬O).(¬M+¬N+¬P).(¬M+¬N+¬Q).(¬M+¬N+¬R).(¬M+¬N+¬S).(¬M+¬N+¬T).(¬M+¬O+¬P).(¬M+¬O+¬Q).(¬M+¬O+¬R).(¬M+¬O+¬S).(¬M+¬O+¬T).(¬M+¬P+¬Q).(¬M+¬P+¬R).(¬M+¬P+¬S).(¬M+¬P+¬T).(¬M+¬Q+¬R).(¬M+¬Q+¬S).(¬M+¬Q+¬T).(¬M+¬R+¬S).(¬M+¬R+¬T).(¬M+¬S+¬T).(¬N+¬O+¬P).(¬N+¬O+¬Q).(¬N+¬O+¬R).(¬N+¬O+¬S).(¬N+¬O+¬T).(¬N+¬P+¬Q).(¬N+¬P+¬R).(¬N+¬P+¬S).(¬N+¬P+¬T).(¬N+¬Q+¬R).(¬N+¬Q+¬S).(¬N+¬Q+¬T).(¬N+¬R+¬S).(¬N+¬R+¬T).(¬N+¬S+¬T).(¬O+¬P+¬Q).(¬O+¬P+¬R).(¬O+¬P+¬S).(¬O+¬P+¬T).(¬O+¬Q+¬R).(¬O+¬Q+¬S).(¬O+¬Q+¬T).(¬O+¬R+¬S).(¬O+¬R+¬T).(¬O+¬S+¬T).(¬P+¬Q+¬R).(¬P+¬Q+¬S).(¬P+¬Q+¬T).(¬P+¬R+¬S).(¬P+¬R+¬T).(¬P+¬S+¬T).(¬Q+¬R+¬S).(¬Q+¬R+¬T).(¬Q+¬S+¬T).(¬R+¬S+¬T)'

print("Setting up equation.")
eq = Equation(vars)
print("Instantiate Algorithm")
ga = FlipGA(eq, ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T'])
print("Running algorithm")
ga.run()