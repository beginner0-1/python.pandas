import pandas as pd 
data ={
    "name" : ["ram","shyam","rohan","vinit"],
    "age" :  [23,22,24,25],
    "salary": [50000,40000,70000,55000]
}
df=pd.DataFrame(data)
#adding a new column 

df["bonus"] =df["salary"] *0.1
#print(df)
df["actual-salary"]=df["bonus"] + df["salary"]
#print(df)

#we have another method to insert data

# df.insert(0,"employee id ",[10,50,60,20])

#how to update any value 

df.loc[0,"age"] = 26
#print(df)

#removing acolumn
#df.drop(columns=["actual-salary"],inplace = True)
print(df)
