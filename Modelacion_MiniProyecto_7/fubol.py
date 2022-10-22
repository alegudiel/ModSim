import matplotlib.pyplot as plt
from fuzzy_expert.variable import FuzzyVariable
from fuzzy_expert.rule import FuzzyRule
from fuzzy_expert.inference import DecompositionalInference

variables = {
    "positionUPDown": FuzzyVariable(
        universe_range=(0, 120),
        terms={
            "Up": [(0, 0), (60, 0), (65, 0.3), (70, 0.4), (80, 0.7), (110, 0.9), (120, 1)],
            "Down": [(0, 1), (30, 1), (35,  0.9), (40, 0.7), (50, 0.5), (55, 0.2), (60, 0)],
        },
    ), 
    "positionRight": FuzzyVariable(
        universe_range=(0, 200),
        terms={
            "Right": [(0, 0), (100, 0), (135, 0.3), (150, 0.4), (170, 0.7), (180, 0.9), (200, 1)],
            "Middle": [(0, 1), (35, 1), (50,  0.9), (65, 0.7), (70, 0.5), (80, 0.2), (100, 0)],
        },
    )
}
plt.figure(figsize=(10, 2.5))
# variables["positionUPDown"].plot()
# plt.show()

# variables["positionRight"].plot()
# plt.show()

rules = [
    FuzzyRule(
        premise=[
            ("positionUPDown", "Up"),
            ("AND", "positionRight", "Right"),
        ],
        consequence=[("decision", "MoveRight")],
    ),
    FuzzyRule(
        premise=[
            ("positionUPDown", "Down"),
            ("AND", "positionRight", "Middle"),
        ],
        consequence=[("decision", "MoveLeft")],
    )
]

print(rules[0])
print()
print(rules[1])


# model = DecompositionalInference(
#     and_operator="min",
#     or_operator="max",
#     implication_operator="Rc",
#     composition_operator="max-min",
#     production_link="max",
#     defuzzification_operator="cog",
# )

# model(
#     variables=variables,
#     rules=rules,
#     positionUPDown=103,
#     positionRight=155,
# )