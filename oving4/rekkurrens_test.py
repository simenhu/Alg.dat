from math import floor
from matplotlib import pyplot as plt

def f1(i, time):
    time += 1
    if i <= 1:
        return time
    return f1(floor(i/2), time)+f1(i-2, time)

x = [f1(x,0) for x in range(200)]
x1 = [x for x in range(200)]
x2 = [x**2 for x in range(200)]
x3 = [x**3 for x in range(200)]
x4 = [x**4 for x in range(200)]
plt.plot(x)
plt.plot(x2)
plt.plot(x3)


plt.show()

