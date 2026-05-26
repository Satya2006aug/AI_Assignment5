# bayesian network example

from pgmpy.models import BayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination


model = BayesianNetwork([

    ('Rain', 'WetGrass'),
    ('Sprinkler', 'WetGrass')

])


cpd_rain = TabularCPD(

    variable='Rain',
    variable_card=2,

    values=[
        [0.7],
        [0.3]
    ]
)


cpd_sprinkler = TabularCPD(

    variable='Sprinkler',
    variable_card=2,

    values=[
        [0.6],
        [0.4]
    ]
)


cpd_wetgrass = TabularCPD(

    variable='WetGrass',
    variable_card=2,

    values=[
        [0.99, 0.9, 0.8, 0.0],
        [0.01, 0.1, 0.2, 1.0]
    ],

    evidence=['Rain', 'Sprinkler'],
    evidence_card=[2,2]
)


model.add_cpds(cpd_rain,
               cpd_sprinkler,
               cpd_wetgrass)

print(model.check_model())


infer = VariableElimination(model)

result = infer.query(

    variables=['WetGrass'],
    evidence={'Rain':1}
)

print(result)
