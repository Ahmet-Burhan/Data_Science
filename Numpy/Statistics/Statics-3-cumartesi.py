#MEAN MEDIAN STANDART SAPMA
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
a = [1,1,1,1,1,2,2,2,2,3,3,1,4,4,5,5,6,7,8,9,11]

print(len(a))
print(np.mean(a)) #ortalama
print(np.median(a)) #median veriyor (en ortada ki veri)
print(stats.mode(a)) #mode veriyor ve count u veriyor
print(stats.skew(a))
print(plt.hist(a)) #bize histogram veriyor # metlolipden cektik
print(np.var(a)) # variance hesabi verir

print("----------------------")

print(np.std(a)) #standart sapma verir
print(np.mean(a)-2*np.std(a)) #
