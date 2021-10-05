import numpy as np
a = np.array([5,6,9])
print(a.ndim) # 1 dimension 
b = np.array([[1,2],[3,4],[5,6]])
print(b.ndim) # 2 dimension array
print(b.itemsize) #4 bytes 
print(b.dtype)
##############
c = np.array([[1,2],[3,4],[5,6]], dtype=np.float64) #data tipini degistirdik. 
print(c.itemsize) # Yeni veri boyutu 8 byte oldu
print(c)# bize 1. .... verir yani normal 1 den float degere cevirdi ve kendisi rakamlar ile doldurdu
print(c[0][0]) #4 du. ayrica hepsinin yanina 0 eklemis 