import numpy as num
import matplotlib.pyplot as matlab

x = []
t=num.arange(0,50,0.01)
for i in t:
    if i >= 0 and i < 12:
        x.append(int(0))
    elif i >= 12 and i < 21:
        x.append(int(-2))
    elif i >= 21 and i < 43:
        x.append(int(3))
    elif i >= 43:
        x.append(int(1))
matlab.plot(t,x)
matlab.xlabel('x')
matlab.ylabel('y')
matlab.title('20230304 Exercise 004')
matlab.show()