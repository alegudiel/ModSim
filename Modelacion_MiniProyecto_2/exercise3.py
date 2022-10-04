import random

rangeValues = ['0.0-0.1','0.1-0.2','0.2-0.3','0.3-0.4','0.4-0.5','0.5-0.6','0.6-0.7','0.7-0.8','0.8-0.9','0.9-1.0']
X1 = 100
X2 = 5000
X3 = 100000

values = [0]*10

def ifsSegment(r):
    if (r < 0.1):
        values[0] += 1
    elif (r >= 0.1 and r < 0.2):
        values[1] += 1
    elif (r >= 0.2 and r < 0.3):
        values[2] += 1
    elif (r >= 0.3 and r < 0.4):
        values[3] += 1
    elif (r >= 0.4 and r < 0.5):
        values[4] += 1
    elif (r >= 0.5 and r < 0.6):
        values[5] += 1
    elif (r >= 0.6 and r < 0.7):
        values[6] += 1
    elif (r >= 0.7 and r < 0.8):
        values[7] += 1
    elif (r >= 0.8 and r < 0.9):
        values[8] += 1
    elif (r >= 0.9 and r < 1.0):
        values[9] += 1

def percentage(cont, X):
    return str(int((cont/X) * 100))

def dots(i, value, X):
    if (value != 0):
        print(rangeValues[i] + ': ' + "*" * int(X/value) + ' (' + str(value) + ' ' + percentage(value,X) + '%)')
    else:
        print(rangeValues[i] + ': ' + "*" * int(value) + ' (' + str(value) + ' ' + percentage(value,X) + '%)')

def generator3(X):
    for i in range(X):
        r = random.random()
        ifsSegment(r)
        
    for i in range(len(values)):
        dots(i, values[i], X)

def generator2(X):
    r = 100
    for i in range(X):
        r = 7**5 * r % (2**31 - 1)
        normalized = ((2**31 - 1)/r) - 1
        ifsSegment(normalized)
    
    for i in range(len(values)):
        dots(i, values[i], X)

def generator1(X):
    r = 200
    for i in range(X):
        r = 5**5 * r % (2**35 - 1)
        normalized = ((2**35 - 1)/r) - 1
        ifsSegment(normalized)
    
    for i in range(len(values)):
        dots(i, values[i], X)

print("---------- Inicio G1 -----------")
generator1(X1)
values = [0]*10
print("-----------------------------")
generator1(X2)
values = [0]*10
print("-----------------------------")
generator1(X3)
values = [0]*10

print("---------- Inicio G2 -----------")
generator2(X1)
values = [0]*10
print("-----------------------------")
generator2(X2)
values = [0]*10
print("-----------------------------")
generator2(X3)
values = [0]*10

print("---------- Inicio G3 -----------")
generator3(X1)
values = [0]*10
print("-----------------------------")
generator3(X2)
values = [0]*10
print("-----------------------------")
generator3(X3)
print("-----------------------------")

