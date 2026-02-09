import pandas as pd

data ={
    "name" : ["ram","shyam","rohan","vinit"],
    "age" :  [23,22,24,25],
    "salary": [50000,40000,70000,55000]
}

df =pd.DataFrame(data)

#grouping
group =df.groupby("age")["salary"].sum()
print(group)

#grouping based on more than one column
group=df.groupby(["age","name"])["salary"].sum()
print(group)