from sympy.logic.boolalg import truth_table, Xnor
from sympy import *

a,b,c = symbols('a b c')

our_symbols = [a,b,c]

our_statements = [a, b, c, ~a, ~b, a >> ~b, ~a | (a >> ~b), Xnor((~a | (a >> ~b)), c)]
def create_table(statements, symbols):
    output = [ [] for _ in range(2 ** len(symbols) + 1) ]
    for statement in statements:
        output[0].append(statement)
        table = truth_table(statement, symbols, False)
        i = 1
        for t in table:
            output[i].append(t)
            i += 1
    return output

def print_table(table, pretty=True):
    if pretty:
        print(str(table[0])[1:-1])
    prettyp = ""
    for row in table[1:]:
        line = ""
        for val in row:
            if val == True:
                line += 'T, '
            else:
                line += 'F, '
        line = line[:-2] + '\n'
        prettyp+=line
    print(prettyp)

p,q,r = symbols('p q r')
qtwo_symbols = [p,q,r]
print_table(create_table(qtwo_symbols+[~p|(~q>>~r),~(p&~q&r)], qtwo_symbols))
