# https://builtin.com/data-science/poisson-process
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson
from weather import *

# Probability mass function
def poissonMassFunction(temp, hum, mu):
    
    makeDecisionWeather(temp, hum)
    k = np.arange(0, 100)
    pmf = poisson.pmf(k, mu=mu)
    pmf = np.round(pmf, 5)
    pmf = pmf * returnValueOfDecision()

    plt.plot(k, pmf, marker='o')
    plt.xlabel('K Students')
    plt.ylabel('Probability')
    plt.show()
# De 6:30am a 7:30am temp=17, Humedad 68
poissonMassFunction(15, 71, 40)
# De 12:30pm a 1:30pm temp=21, Humedad 51
poissonMassFunction(25, 51, 40)
# De 6:30pm a 7:30pm temp=21, Humedad 45
poissonMassFunction(19, 70, 40)

# seeGraphsOfVariables()
# seeGraphsOfDecision(15, 71)
# seeGraphsOfDecision(25, 51)
# seeGraphsOfDecision(19, 70)