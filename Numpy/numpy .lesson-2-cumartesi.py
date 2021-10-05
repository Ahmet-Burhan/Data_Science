import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


#%matplotlib inline
#print(np.random.rand(5)) # Her seferinde farkli rakamlar verir
#print(np.random.rand(5,5)) # 5 e 5 random matriks olusturur

arr = np.random.randn(99999)
#plt.hist(arr,bins=100)
#plt.show();

#print(arr.std()) # standart sapma
arr.var()# standart sapmanin karesi variance a esittir

#print(np.random.randint(10))
#print(np.random.randint(0,10,size=(2,4))) # 2 ye 4 matriks olusturur ,0 ve 10 rakamlari arasinda
#print(np.random.randint(0,[10,6,2])) # 0 ve listenin her elemani ile sirasiyla rastgele bir sayi uretti
#print(np.random.randint(0,10,5))
#print(np.random.randint([1,2,3],[6,7,8],size=(3,3)))

##  CONCATENATE 
a = np.random.randint(2,10,size=(4,4))
b = np.ones((4,4))
#print(np.concatenate([a,b]))
#print(np.concatenate([a,b],axis = 1)) 


#SPLIT
#print(np.split(a,[2])) #ikinci satiri boluyor
#print(np.split(a,[2,3],axis=1))  #y ekseninde kes

df = sns.load_dataset("diamonds")

#print(df)
#print(df[["carat","depth"]])  #diamonds veri tabanindan sadece carat ve depth i getirdik

diamond1= np.array(df[["carat","depth"]]) #veriyi rakamlara arraye degistirecez
diamond= np.array(df) 
#print(diamond)
#print(diamond[0:5])
#print(diamond[satir,sstun,seperate]) ->(diamond[0:2  ,  0:3  ,  seperate]) 0 ve 3 uncu satir arasi al , sutunda ise 0 ve 3 arasi al.
#                                      ->diamond[0,2 , 1]  sadece 1 deki degerleri al. Yani bize 2 deger verecek
#                                      ->diamond[0,::2 ] 0 satirda - 0 inci 2 in ve 4 uncu satiri al.

abc = diamond[:,-3:].reshape(len(diamond),3)
#print(abc)
#print(abc[:,0])
volume=(abc[:,0]*abc[:,1]*abc[:,2])
print(volume.reshape(len(volume),1))
