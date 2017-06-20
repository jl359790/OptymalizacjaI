import re

def all_subnodes(direct_children, current_node):
    subnodes = list()
    subnodes.append(current_node)
    for child in direct_children[current_node]:
        subs = all_subnodes(direct_children, child)
        for sub in subs:
            subnodes.append(sub)
    return subnodes

fileName = "0.in"
file = open(fileName, "r")

N = int(file.readline())

Bw = list()
Bu = list()
Rw = list()
Ru = list()

for line in file:
    split = re.split(' ', line)
    Bw.append(int(split[0]))
    Bu.append(int(split[1]))
    Rw.append(int(split[2]))
    Ru.append(int(split[3]))

WSA_direct_subnodes = [[] for i in range(N)] #nodes' direct children

for i in range(N):
    self_parent = (i == Bw[i])
    if not (self_parent):
        WSA_direct_subnodes[Bw[i]].append(i)

WSA_all_subnodes = []

for i in range(N):
    WSA_all_subnodes.append(all_subnodes(WSA_direct_subnodes, i))
    
Union_direct_subnodes = [[] for i in range(N)] #nodes' direct children
for i in range(N):  
    self_parent = (i == Bu[i])
    if not (self_parent):
        Union_direct_subnodes[Bu[i]].append(i)

Union_all_subnodes = []

for i in range(N):
    Union_all_subnodes.append(all_subnodes(Union_direct_subnodes, i))
    
p = MixedIntegerLinearProgram(maximization=False, solver = "GLPK")
x = p.new_variable(binary = True)

p.set_objective(sum(x[i] for i in range(N)))

for i in range(N):
    p.add_constraint(sum(x[j] for j in WSA_all_subnodes[i]) >= Rw[i])
    
for i in range(N):
    p.add_constraint(sum(x[j] for j in Union_all_subnodes[i]) >= Ru[i])

print int(N - p.solve())
for i in range(N):
    if (int(p.get_values(x[i])) == 0):
        print i,
