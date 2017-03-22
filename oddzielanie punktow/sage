A = [ (1.0, 2.0), (2.0, 3.0), (3.0, 4.0) ]
B = [ (1.0, 1.0), (2.0, 2.0), (3.0, 3.0) ]


p = MixedIntegerLinearProgram(maximization = False)


var = p.new_variable(real = True, nonnegative=False)
a, b = var['a'], var['b']
eps = var['e']

p.set_objective(eps)

for pt in A:
    p.add_constraint(a * pt[0] + b + eps >= pt[1])
for pt in B:
    p.add_constraint(a * pt[0] + b - eps<= pt[1])
   
p.solve()

print "y = ", p.get_values(a), "* x + ", p.get_values(b)
list_plot(A) + list_plot(B, color = "red") + plot(p.get_values(a) * x + p.get_values(b), color="green")
