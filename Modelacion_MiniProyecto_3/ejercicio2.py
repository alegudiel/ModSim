import matplotlib.pyplot as plt
import random
dicNums = {1: 0.25, 2: 0.15, 3: 0.15, 4: 0.45}

results = []
def takeNum():
    r = random.random()

    if (r < 0.45):
        return 4
    elif (r < 0.70):
        return 3
    elif (r < 0.85):
        return 2
    else:
        return 1

for i in range(1000):
    results.append(takeNum())

plt.xlabel('Number')
plt.ylabel('Frequency')
plt.title('Histogram of repetitions')
plt.hist(results)
plt.show()
