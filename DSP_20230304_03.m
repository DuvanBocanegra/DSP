clear all
t=(-20:1:30);
a=heaviside(t)

plot(t+20,a)
ylim([-0.5,1.5])
xlim([-20,60])
