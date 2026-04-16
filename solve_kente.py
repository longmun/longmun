import sympy as sp

# Read the system of equations from the file
with open('system.txt', 'r') as file:
    equations = file.readlines()

# Prepare the symbols and equations
symbols = []
for eq in equations:
    lhs, rhs = eq.split('=')
    symbols.append(sp.symbols(lhs.strip()))
    equations.append(sp.sympify(rhs.strip()))

# Assuming equations are in the form of a list of sympy expressions
# Applying linearization and Gröbner basis methods
result = sp.groebner(equations, symbols)

# Print the result
print("Gröbner basis:")
for poly in result:
    print(poly)