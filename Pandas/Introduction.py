import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



titanic_df = pd.read_excel("titanic3.xls" , "titanic3", index_col=None , na_values=["NA"]) # Read excel sheet to Dataframe
titanic_df.head()