import pandas as pd 

data ={
    "day": ["monday","tuesday","wednesday","thrusday","friday","saturday","sunday"],
    "ammount": [1200,800,950,1800,1300,2500,1700]
    }


df = pd.DataFrame(data)
print(df)

print (" \nthe maximum amount in this weekday \n")
max_row =df.loc[df["ammount"].idxmax()]
print(max_row)