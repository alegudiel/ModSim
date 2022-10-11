import random
from matplotlib.lines import lineStyles
import matplotlib.pyplot as plt

result = []

def coin_monteCarlo_Simulation(N):
    values = 0

    for i in range(N):
        flip_ = random.randint(0,1)
        values += flip_

        prob = values / (i + 1)
        result.append(prob)

    return values/N


simulation = coin_monteCarlo_Simulation(1000)
print("Final prob: ", simulation, result)

plt.axhline(y=0.5, color='green', linestyle='.')
plt.xlabel('Iteration')
plt.ylabel('Probability')
plt.plot(result)
plt.show()
