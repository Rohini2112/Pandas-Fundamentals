## 1. Introduction to the Data ##

f500_head = f500.head(10)

f500_head.info()

## 2. Vectorized Operations ##

rank_change = f500["previous_rank"] - f500["rank"]
print(rank_change)

## 3. Series Data Exploration Methods ##

rank_change =  f500["previous_rank"] - f500["rank"]

rank_change_max = rank_change.max()
print(rank_change_max)

rank_change_min = rank_change.min()
print(rank_change_min)

## 4. Series Describe Method ##

rank = f500["rank"]
rank_desc = rank.describe()
print(rank_desc)

prev_rank = f500["previous_rank"]
prev_rank_desc = prev_rank.describe()
print(prev_rank_desc)

## 5. Method Chaining ##

zero_previous_rank = f500["previous_rank"].value_counts().loc[0]
print(zero_previous_rank)

## 6. Dataframe Exploration Methods ##

max_f500 = f500.max(axis = 0, numeric_only = True)
print(max_f500)

## 7. Dataframe Describe Method ##

f500_desc = f500.describe()

## 8. Assignment with pandas ##

print(f500.loc["Dow Chemical", "ceo"])
f500.loc["Dow Chemical", "ceo"] = "Jim Fitterling"
print(f500.loc["Dow Chemical", "ceo"])

## 9. Using Boolean Indexing with pandas Objects ##

motor_bool = f500["industry"] == "Motor Vehicles and Parts"
motor_countries = f500.loc[motor_bool, "country"]

## 10. Using Boolean Arrays to Assign Values ##

import numpy as np
prev_rank_before = f500["previous_rank"].value_counts(dropna=False).head()
print(prev_rank_before)

f500.loc[f500["previous_rank"] == 0, "previous_rank"] = np.nan

prev_rank_after = f500["previous_rank"].value_counts(dropna = False).head()
print(prev_rank_after)

## 11. Creating New Columns ##

f500["rank_change"] = f500["previous_rank"] - f500["rank"]
#print(rank_change)
rank_change_desc = f500["rank_change"].describe()
print(rank_change_desc)



## 12. Challenge: Top Performers by Country ##

industry_usa = f500["industry"][f500['country'] == "USA"].value_counts().head(2)
print(industry_usa)

sector_china = f500["sector"] [f500["country"] == "China"].value_counts().head(3)
print(sector_china)

## 12. Challenge: Top Performers by Country ##

industry_usa = f500["industry"][f500['country'] == "USA"].value_counts().head(2)
print(industry_usa)

sector_china = f500["sector"] [f500["country"] == "China"].value_counts().head(3)
print(sector_china)