W = dict()
W['A'] = ('E')
W['E'] = ('A', 'H')
W['H'] = ('E', 'K')
W['K'] = ('H')
  

p = MixedIntegerLinearProgram(maximization = False)
var = p.new_variable(binary = True, nonnegative = True)
for w in W:
    var[w]

p.set_objective(sum(var[w] for w in W))

for w in W:
    p.add_constraint(var[w] + sum(var[v] for v in W[w]) >= 1)


p.solve()

print p.get_values(var)
