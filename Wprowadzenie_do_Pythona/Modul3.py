from timeit import timeit
setup = """
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

stmt1 = """
lista.insert(0,0)
"""
stmt2 = """
lista = [0] + lista
"""

stmt3 = """
lista.insert(5,0)
"""

stmt4 = """
lista.append(0)
lista.sort()
"""

stmt5 = """
lista.append(0)
"""
stmts = [stmt1, stmt2, stmt3, stmt4, stmt5]
iters = 10000

for idx, st in enumerate(stmts, start=1):
    print(f"Stmt{idx} time: {timeit(st, setup=setup, number=iters)}")