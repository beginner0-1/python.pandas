import pandas as pd
#syntax for sorting df.sort(by="column name",True/False , inplace = true)

data ={
    "name":["yuvraj","aman","kartikesh","abhey"],
    "age":[20 ,21,19,22],
    "city ":["meerut","ghaziabad","meerut","arrah"]
}

df=pd.DataFrame(data)
df.sort_values(by="age", ascending=True,inplace=True)
print(df)

#for sorting more than one data
#df.sort_values(by=["age","name"],ascending=[True,False],inplace= True)

#finding average of a specifie column 
#print("Average age :")
avg_age=df["age"].mean()
#print(avg_age)