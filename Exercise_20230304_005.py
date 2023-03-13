import numpy as num
import matplotlib.pyplot as matlab

x = []
t=num.arange(0,50,0.01)
for i in t:
    if i >= 0 and i < 6:
        x.append(float(2))
    elif i >= 6 and i < 41:
        x.append(float(-4+i))
    else:
        x.append(float(10))
matlab.plot(t,x)
matlab.xlabel('x')
matlab.ylabel('y')
matlab.title('20230304 Exercise 005')
matlab.show()
