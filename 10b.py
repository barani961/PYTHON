import pandas as pd
A=[1,None,3,4]
B=[5,6,None,8]
Data=pd.DataFrame(A,B)
Dropped=Data.dropna()
Print(Dropped)
Fill=input("data to be filled")
Filled=Data.fillna(Fill)
print(Filled)
