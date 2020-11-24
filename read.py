
import os
import scipy as sp
import matplotlib.pyplot as plt

data_dir = os.path.join(
    os.path.dirname(os.path.realpath(__file__)), ".", "data")
data = sp.genfromtxt(os.path.join(data_dir, "web_traffic.tsv"), delimiter="\t")

x, y = data[:,0], data[:,1]
x, y = x[~sp.isnan(y)], y[~sp.isnan(y)]
fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
f2p = sp.polyfit(x, y, 2)
fx = sp.linspace(0, x[-1], 1000)
f1 = sp.poly1d(fp1)
f2 = sp.polyfit(f2p)

def error(f, x, y):
    return sp.sum((f(x)-y)**2)

plt.scatter(x, y)
plt.title('Web traffic over the last month')
plt.xlabel('Time')
plt.ylabel('Hits/hour')
plt.xticks([w*7*24 for w in range(10)], ['week %i' %w for w in range(10)])
plt.autoscale(tight=True)
plt.plot(fx, f1(fx), linewidth=4)
plt.plot(fx, f2(fx), linewidth=4)
plt.legend(['d=%i' % f1.order], loc='upper left')
plt.grid()
plt.show()

