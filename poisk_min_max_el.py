import numpy as np
#y = np.loadtxt('poisk_min_max.csv')
x = np.zeros((10,10))
np.savetxt(delimiter=';',fname='zeros.csv',fmt='%1.1i', X=x)
y = np.loadtxt(delimiter=';',fname='zeros.csv')
print(y)
