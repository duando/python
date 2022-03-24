import os

os.system('clear')
timeActual = os.times()
print(type(timeActual))
print(timeActual)
for i in range(len(timeActual)):
    print(i+1, timeActual[i], sep=' - ')