from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpStatus, value

# Definir origens e destinos
origins = ["A", "B", "C", "D", "E", "F", "G"]
destinations = ["A", "B", "C", "D", "E", "F"]

# Definir os custos de transporte
costs = {
    ("A", "B"): 10, ("A", "C"): 12, ("A", "D"): 8, ("A", "E"): 9, ("A", "F"): 5,
    ("B", "A"): 10, ("B", "C"): 15, ("B", "D"): 16, ("B", "E"): 8, ("B", "F"): 10,
    ("C", "A"): 12, ("C", "B"): 15, ("C", "D"): 10, ("C", "E"): 8, ("C", "F"): 12,
    ("D", "A"): 8, ("D", "B"): 16, ("D", "C"): 10, ("D", "E"): 15, ("D", "F"): 5,
    ("E", "A"): 9, ("E", "B"): 8, ("E", "C"): 8, ("E", "D"): 15, ("E", "F"): 20,
    ("F", "A"): 5, ("F", "B"): 10, ("F", "C"): 12, ("F", "D"): 5, ("F", "E"): 20,
    ("G", "A"): 0, ("G", "B"): 0, ("G", "C"): 0, ("G", "D"): 0, ("G", "E"): 0, ("G", "F"): 0,
}

# Definir a demanda para os destinos
demand = {
    "A": 600,
    "B": 250,
    "C": 250,
    "D": 500,
    "E": 150,
    "F": 100,
}

# Definir a capacidade das origens
capacity = {
    "A": 400,
    "B": 300,
    "C": 150,
    "D": 300,
    "E": 100,
    "F": 250,
    "G": 350,
}

# Criar o modelo
model = LpProblem("Transporte", LpMinimize)

# Criar variáveis de decisão
variables = LpVariable.dicts("x", (origins, destinations), 0)

# Adicionar a função objetivo ao modelo
model += lpSum(costs[o, d] * variables[o][d] for o in origins for d in destinations if (o, d) in costs)

# Adicionar restrições de capacidade
for o in origins:
    model += lpSum(variables[o][d] for d in destinations if (o, d) in costs) <= capacity[o]

# Adicionar restrições de demanda
for d in destinations:
    model += lpSum(variables[o][d] for o in origins if (o, d) in costs) >= demand[d]

# Resolver o modelo
model.solve()

# Verificar o status da solução
print(f"Status: {LpStatus[model.status]}")

# Mostrar os valores das variáveis de decisão
for o in origins:
    for d in destinations:
        if (o, d) in costs:
            print(f"Quantidade transportada de {o} para {d}: {value(variables[o][d])}")

# Mostrar o valor total do custo
print(f"Custo total: {value(model.objective)}")


