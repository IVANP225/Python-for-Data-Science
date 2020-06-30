import numpy as np
#создали матрицу 10 на 10
#x = np.random.randint(100, size=(10,10))
#np.savetxt(delimiter=';',fname='ran.csv',fmt='%1.1i', X=x)
y = np.loadtxt(delimiter=';',fname='ran.csv')

#поиск минимального и максимального элемента и позиций
x_minim = np.min(y)
x_maxim = np.max(y)

tmp_min = np.where(y ==x_minim)
tmp_max = np.where(y ==x_maxim)

# меняем местами
y[tmp_min] = x_maxim
y[tmp_max] = x_minim
np.savetxt(delimiter=';',fname='ran_izm.csv',fmt='%1.1i', X=y)
