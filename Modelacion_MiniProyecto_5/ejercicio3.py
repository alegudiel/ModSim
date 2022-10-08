import matplotlib.pyplot as plt
import random
import math

U = random.random()

FirstInterval = 0
SecondInterval = 0
ThirdInterval = 0
Lambda = 10
ITERATIONS = 100
result = 0

def funcExp(result, lamVal):
    return result - float((1/lamVal)*math.log(random.random()))

for i in range(0, ITERATIONS):

    result = funcExp(result, Lambda)

    if (result < 1):
        FirstInterval += result
    elif (result > 1 and result <= 3):
        SecondInterval += result
    elif (result > 3):
        ThirdInterval += result

print((FirstInterval + SecondInterval + ThirdInterval)/ITERATIONS)
