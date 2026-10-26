from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Create Bayesian Network
model = DiscreteBayesianNetwork([
    ('Burglary', 'Alarm'),
    ('Earthquake', 'Alarm')
])

# CPT for Burglary
cpd_b = TabularCPD(
    variable='Burglary',
    variable_card=2,
    values=[[0.999], [0.001]]
)

# CPT for Earthquake
cpd_e = TabularCPD(
    variable='Earthquake',
    variable_card=2,
    values=[[0.998], [0.002]]
)

# CPT for Alarm
cpd_a = TabularCPD(
    variable='Alarm',
    variable_card=2,
    values=[
        [0.999, 0.71, 0.06, 0.05],
        [0.001, 0.29, 0.94, 0.95]
    ],
    evidence=['Burglary', 'Earthquake'],
    evidence_card=[2, 2]
)

# Add CPTs to model
model.add_cpds(cpd_b, cpd_e, cpd_a)

# Check model
print("Model is valid:", model.check_model())

# Perform inference
infer = VariableElimination(model)

result = infer.query(
    variables=['Burglary'],
    evidence={'Alarm': 1}
)

print(result)
print("P(Burglary | Alarm=True):",
      round(result.values[1], 4))