import numpy as np

my_list = [1,2,3,4,5]
print(type(my_list))


my_array = np.array(my_list) # istersen liste olarak da yazablirisn
print(my_array)
print(type(my_array))


###bu normal yol
a = [1,2,3,4,5]
b = [1,2,3,4,5]
asumb = []
for i in range(len(a)):
    asumb.append(a[i]+b[i] )

print(asumb)

###
c = np.array([1,2,3,4,5])
d = np.array([1,2,3,4,5])

print(c+d)

print (c.size)
print (c.shape)
print(c.dtype)
print(d.itemsize)
print(c.ndim)
###############

a1 = np.array([[1,2,3,4],[1,2,3,4],[2,3,4,5]])
b1 = np.array([[2,3,4,5],[1,2,4,5],[1,2,3,4]])

print(a1.size)
print(a1.shape)
print(a1)

print("..........................................................")
print(a1+b1)
print("..........................................................")
print("..........................................................")
print("..........................................................")


#£ boyutlu nasil olur?
a3 = np.array([[[2,3,4,5],[1,2,4,5],[1,2,3,4]],[[2,3,4,5],[1,2,4,5],[1,2,3,4]]])
print(a3)
print(a3.shape)  #3 boyutlu olacak

print("..........................................................")
print("..........................................................")

print("..........................................................")
print("..........................................................")

zero = np.zeros((5,3),dtype=int)
print(zero)


#import matplotlib.pyplot as plt
#%matplotlib inline 
#a = np.full((32,32,3), 255, dtype = int)
#a[:,:,0] = 122 # red
#a[:,:,1] = 20 # green
#a[:,:,2] = 120 # blue
#plt.imshow(a)

#print(list(range(50)))

