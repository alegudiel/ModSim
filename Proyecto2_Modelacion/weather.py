import matplotlib.pyplot as plt
from fuzzy_expert.variable import FuzzyVariable
from fuzzy_expert.rule import FuzzyRule
from fuzzy_expert.inference import DecompositionalInference

variables = {
    "weatherTemp": FuzzyVariable(
        universe_range=(0, 50),
        terms={
            "Hot": [(0, 0), (23, 0), (35, 0.5), (40, 1), (45,1), (50, 0)],
            "Cold": [(0, 0), (10, 0.8), (15, 1), (20, 1), (22, 0.3), (25, 0)],
        },
    ),
    "weatherHumidity": FuzzyVariable(
        universe_range=(0, 100),
        terms={
            "HighHumidity": [(0, 0), (50, 0), (70, 1), (80, 1), (90,0.8), (95,0.5), (100, 0)],
            "LowHumidity": [(0, 0), (15, 0.8), (30, 0.8), (42,  0.8), (52, 0.5), (60, 0)],
        },
    ),
    "decision": FuzzyVariable(
        universe_range=(0, 1),
        terms={
            "should_buy": [(0, 0), (0.1, 0), (0.3, 0.8), (0.4, 0.8), (0.6,0.4), (0.7,0.4), (0.9,0.1), (1, 0)],
            "should_not_buy": [(0, 0), (0.1, 0.3), (0.4,  0.3), (0.6, 1), (0.8, 1), (0.9,0), (1, 0)],
        },
    )
}

rules = [
    FuzzyRule(
        premise=[
            ("weatherTemp", "Hot"),
            ("AND", "weatherHumidity", "HighHumidity"),
            ("OR", "weatherHumidity", "HighHumidity"),
        ],
        consequence=[("decision", "should_not_buy")],
    ),
    FuzzyRule(
        premise=[
            ("weatherTemp", "Cold"),
            ("AND", "weatherHumidity", "LowHumidity"),
        ],
        consequence=[("decision", "should_buy")],
    )
]

model = DecompositionalInference(
    and_operator="min",
    or_operator="max",
    implication_operator="Rc",
    composition_operator="max-min",
    production_link="max",
    defuzzification_operator="cog",
)

def makeDecisionWeather(temp, humidity):
    model(
        variables=variables,
        rules=rules,
        weatherTemp=temp,
        weatherHumidity=humidity,
    )

def seeGraphsOfVariables():
    plt.figure(figsize=(10, 2.5))


    variables["weatherTemp"].plot()
    plt.show()

    variables["weatherHumidity"].plot()
    plt.show()

    variables["decision"].plot()
    plt.show()


    plt.figure(figsize=(10, 6))
    model.plot(
        variables=variables,
        rules=rules,
        weatherTemp=25,
        weatherHumidity=30,
    )
    plt.show()

def returnValueOfDecision():
    return(model.defuzzificated_infered_memberships['decision'])
