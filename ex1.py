import numpy as np
import matplotlib.pylab as plt
data1=np.genfromtxt("field.txt",delimiter=",")
t=data1[:,0]
x=data1[:,1]
y=data1[:,2]
plt.figure()
plt.title("Posicion particula")
plt.plot(x,y,"r")
plt.xlabel("x")
plt.ylabel("y")
plt.savefig("TorresRafael_final_15.pdf")