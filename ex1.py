import numpy as np
import matplotlib.pylab as plt
data1=np.genfromtxt("field.txt",delimiter=",")
t=data1[:,0]
x=data1[:,1]
y=data1[:,2]
plt.figure()
plt.title("x vs y")
plt.plot(x,y,"r")
plt.savefig("TorresRafael_final_15.pdf")