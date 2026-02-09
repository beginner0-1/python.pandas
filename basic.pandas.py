import pandas as pd 

data ={
    "name":["yuvraj","aman","kartikesh","abhey"],
    "age":[20 ,21,19,22],
    "city ":["meerut","ghaziabad","meerut","arrah"]
}

df =pd.DataFrame(data)
print(df)

#print(df.info())

#print(df.describe())

#print(f'shape:{df.shape}')

#print(f'column :{df.columns}')

#df.to_csv("first.csv",index =False)

print("\nThe names of the person which  has age more thsn 20\n")
specific_data=df[df["age"]>20]
print(specific_data)