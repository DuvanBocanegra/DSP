import numpy as num
import matplotlib.pyplot as matlab

x = []
t=num.arange(0,50,0.01)
for i in t:
    if i >= 0 and i < 20:
        x.append(int(0))
    elif i >= 20 and i < 50:
        x.append(int(1))
matlab.plot(t,x)
matlab.xlabel('x')
matlab.ylabel('y')
matlab.title('20230304 Exercise 003')
matlab.show()