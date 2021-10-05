import numpy as np
import pandas as pd

#np.array([1,2,3,4,5])
serr = pd.Series([11,22,33,44,55,66])
#print(serr)
#print(type(serr))
#print(len(serr))
#print(serr.size)
#print(serr.ndim) #indexleri dimension olarka gormuyor
#print(serr.values) #Numpy return etti.Itheriable dondenderdi. Icinde dolasabilirim

serr2 = pd.Series([11,22,33,44,55,66,77,88,99,00,12,34,45,65,68,78,89,90,0])
#print(serr2)
#print(serr2.head(10)) #Default 5

ll = list("clarusway")
#print(pd.Series(ll))

#################################
data = ["ankara","malatya","istanbul"]
index = ["x","y","z"]

#print(pd.Series(data,index))
##################################

Score = [70,60,90,50]
index2 = ["A","B","C","D"]
#print(pd.Series(Score,index2))

#####################################

dict_d = {"D":10,"E":20,"A":-10}
#print(pd.Series(dict_d)) 
######################################

ser1 = pd.Series([1,2,3,4], index = ['USA', 'Germany','USSR', 'Japan'])
ser2 = pd.Series([1,2,5,4], index = ['USA', 'Germany','Italy', 'Japan'])

#print(ser1.index)
#print(ser1.values)
#print(ser1.sort_values())  
#print(ser1["Germany"]) # Bulundugu  index numarasini verir. NOT: Girdiyi string olarak yapiyoruz...

#print(ser1[["Germany","Japan"]])  # Birden fazla index vermek icin liste icinde verin aksi takdir de hata verir.

#print(ser1.Japan)  # Bu da farkli bir yontemdir. Bu da index verir.

##########################

#print(ser1 + ser2)  # eger indexler ayni ise toplar

##############################

panser = pd.Series(data   = [121, 200, 150, 99, 145, 120, 180],
                    index = ["terry", "micheal", "orion", "jason","adam", "thomas", "zack"])

#print(panser.jason)
#print(panser["jason"])    #ikiside ayni islevi gorur
#print(panser["orion":"adam"])  #adamda dahil olur # indexliyoruz #string oldugu icin adami da dahil eder
#print(panser[2:5]) #string degil de integer ile indexlersek son rakam dahil olmaz


################
#print(panser.keys())
#print(panser.items())
#print(panser.index)
#print(panser.values) # values[0] or values[3]  de yapabilirsin
## zip 123124235 memory de ki yerini belirtiyor

#for key ,value in panser.items():
#    print(key,"   ", value)

#######################################
#print(panser[panser>=180]) # panserin icinden 180 den buyuk veya esit olanlari getir
print(panser[panser>180] == 150)
#print(panser)
print(panser)

#print("zack" in panser)
print(panser.isin([121,99])) #teker teker butun verileri true false kontrol eder ve donderirr
