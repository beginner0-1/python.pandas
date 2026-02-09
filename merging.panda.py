import pandas as pd 
df_customers =pd.DataFrame(
    {
        "customer_id" :[1,2,3],
        "name":["ramesh","suresh","ujjwal"]
    }
)

df_orders = pd.DataFrame({
    "customer_id":[1,2,4],
    "orderammount":[250,450,670]
})

df_merge =pd.merge(df_customers,df_orders, on ="customer_id",how = "inner")
#print("inner join :")
#print(df_merge)

df_region1 = pd.DataFrame({
    "customerid" : [3,4],
    "name": ["gopal","raju"]
})

df_region2 = pd.DataFrame({
    "customerid":[1,2],
    "name":["shyan","baburao"]
})

df_concat = pd.concat([df_region1,df_region2],ignore_index=True)
print(df_concat)