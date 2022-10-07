import random
import math

U = random.random()
Ui = 0
Xi = 0
for i in range(0,10):
    if (i < 1):
        Ui += U*0.4 + 0.6
    elif (i > 1 and i <= 3):
        Ui += U*0.5 + 0.1
    elif (i > 3):
        Ui += U*0.1
    Xi = -math.log(Ui, math.e)
    print(Xi)