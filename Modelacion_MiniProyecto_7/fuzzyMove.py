import matplotlib.pyplot as plt
from fuzzy_expert.variable import FuzzyVariable
from fuzzy_expert.rule import FuzzyRule
from fuzzy_expert.inference import DecompositionalInference

variables = {
    "positionUPDown": FuzzyVariable(
        universe_range=(0, 200),
        terms={
            "Y_Max": [(0, 0), (100, 0), (120, 1), (160, 1), (180,0), (200, 0)],
            "Y_Min": [(0, 0), (30, 0.8), (110,  0.8), (160, 0), (200, 0)],
        },
    ), 
    "positionLeftRight": FuzzyVariable(
        universe_range=(0, 200),
        terms={
            "X_Max": [(0, 0), (100, 0), (120, 1), (160, 1), (180,0), (200, 0)],
            "X_Min": [(0, 0), (30, 0.8), (110,  0.8), (160, 0), (200, 0)],
        },
    ),
    "decision": FuzzyVariable(
        universe_range=(0, 200),
        terms={
            "Move_Max": [(0, 0), (90, 0), (120, 0.8), (140, 0.8), (160,0.4), (180,0.4), (190,0), (200, 0)],
            "Move_Min": [(0, 0), (35, 0.3), (70,  0.3), (120, 1), (140, 1), (160,0), (200, 0)],
        },
    )
}

rules = [
    FuzzyRule(
        premise=[
            ("positionUPDown", "Y_Max"),
            ("AND", "positionLeftRight", "X_Max"),
            ("OR", "positionLeftRight", "X_Max"),
        ],
        consequence=[("decision", "Move_Max")],
    ),
    FuzzyRule(
        premise=[
            ("positionUPDown", "Y_Min"),
            ("AND", "positionLeftRight", "X_Min"),
            ("OR", "positionLeftRight", "X_Min"),
        ],
        consequence=[("decision", "Move_Min")],
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

def makeDecisionMovement(positionY, positionX):
    model(
        variables=variables,
        rules=rules,
        positionUPDown=positionY,
        positionLeftRight=positionX,
    )

def seeGraphsOfVariables():
    plt.figure(figsize=(10, 2.5))
    variables["decision"].plot()
    plt.show()

    variables["positionUPDown"].plot()
    plt.show()


    variables["positionLeftRight"].plot()
    plt.show()

    plt.figure(figsize=(10, 6))
    model.plot(
        variables=variables,
        rules=rules,
        positionUPDown=103,
        positionLeftRight=155,
    )
    plt.show()

def returnValueOfDecision():
    return(model.defuzzificated_infered_memberships['decision'])
    
