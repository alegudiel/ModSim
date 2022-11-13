# https://builtin.com/data-science/poisson-process
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Probability mass function
def poissonMassFunction(k, mu):
    k = np.arange(0, k)
    pmf = poisson.pmf(k, mu=mu)
    pmf = np.round(pmf, 5)
    for value, prob in zip(k, pmf):
        print(f"El estudiante no. {value} tiene probabilidad de comprar una bebida caliente de: {prob}")
        print("--------------------------------------------")

    plt.plot(k, pmf, marker='o')
    plt.xlabel('k estudiantes')
    plt.ylabel('Probability')
    plt.show()

# Cumulative distribution function
def poissonCumulativeFunction(k, mu):
	k = np.arange(0, k)
	cdf = poisson.cdf(k, mu=mu)
	cdf = np.round(cdf, 5)

	for value, prob in zip(k, cdf):
		print(f"El estudiante no. {value} tiene probabilidad de comprar una bebida caliente de: {prob}")

	plt.plot(k, cdf, marker='o')
	plt.xlabel('k estudiantes')
	plt.ylabel('Cumulative Probability')
	plt.show()