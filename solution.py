import numpy as np
import matplotlib.pyplot as plt
repeat=1000;
data_points=3;
for i in range(repeat):
 x=np.random.choice(np.arange(-10,10),size=data_points);
 Noise=np.random.normal(0,0.2,size=data_points);
 y = ((x-2)**2 + 4 + Noise);
print("x values:", x)
print("y true values:", y)
b_H0=np.average(y);
@np.vectorize
def H0(x):
  return b_H0;
H1=[];
x_mean=np.average(x);
y_mean=np.average(y);
a_H1 = np.sum((x - x_mean) * (y - y_mean)) / np.sum((x - x_mean) ** 2);
b_H1 = y_mean - a_H1 * x_mean;
H1.append((a_H1,b_H1));
plt.figure(figsize=(10,5))
plt.plot(x,y,'b')
plt.plot(x,a_H1*x+b_H1,'r')
plt.plot(x,H0(x),'c')
plt.show()
H0_mean = np.average(H0(x))
H0_bias = np.average((y - H0_mean) ** 2)
H0_variance = np.average(((H0(x)) - H0_mean) ** 2)
H0_Eout = H0_bias + H0_variance + 0.2**2

H1_mean = np.average(H1)
H1_bias = np.mean((y - H1_mean) ** 2)
H1_variance = np.mean([(a * x + b - H1_mean) ** 2 for a, b in H1])
H1_Eout = H1_bias + H1_variance + 0.2**2

print(f"H0 - Bias^2: {H0_bias}, Variance: {H0_variance}, E_out: {H0_Eout}")
print(f"H1 - Bias^2: {H1_bias}, Variance: {H1_variance}, E_out: {H1_Eout}")
