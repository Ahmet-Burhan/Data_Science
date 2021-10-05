from numpy.random.mtrand import sample
import seaborn as sns
import numpy as np
df = sns.load_dataset("mpg")

#print(sns.get_dataset_names())
#print(df.head(10))
#print(df.shape)
#print(df.columns) #tum kolumlarin isimlerini veriyor
#print(len(df.columns))  #kolum sayilarini gosterir , shape de de gorebilrisin
#print(df.info()) #non-null lari gosterir , data type i gosterir
#print(df.select_dtypes(include=["object"])) #filter liyoruz sadece bize objectleri veriyor
#print(df.nunique(axis=0)) # kactane farkli deger var
#print(df.plot.pie(y=[135,120,23])) # bu galiba yanlis oldu
#print (df.describe()) mean max count vs verir.


#print(np.random.seed(51))
population = np.random.randint(0,100, size=100000)
#print(population)
#print(len(population))

#sample = np.random.choice(population,100)
#print(sample)
#print(population.mean())

sample_means = []

for i in range(100):
    sample = np.random.choice(population,100)
    sample_means.append(sample.mean())

print(sample_means)
print(np.mean(sample_means))