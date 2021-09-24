import pandas as pd
import numpy as np


dat = pd.read_csv("ds_ex2.txt")
labels = ["ID", "height", "bmi", "weight", "LDL", "Systol"]
dat = pd.DataFrame(dat)
dat.columns = labels

dat2 = dat.loc[dat["LDL"] != -1].copy()
co1 = dat2["height"].corr(dat2["bmi"])
co2 = dat2["height"].corr(dat2["weight"])
co3 = dat2["height"].corr(dat2["LDL"])
co4 = dat2["height"].corr(dat2["Systol"])
co5 = dat2["bmi"].corr(dat2["weight"])
co6 = dat2["bmi"].corr(dat2["LDL"])
co7 = dat2["bmi"].corr(dat2["Systol"])
co8 = dat2["weight"].corr(dat2["LDL"])
co9 = dat2["weight"].corr(dat2["Systol"])
co10 = dat2["LDL"].corr(dat2["Systol"])
coeffs2 = np.array([co1, co2, co3, co4, co5, co6, co7, co8, co9, co10])

corrLabels = ["height:bmi", "height:weight", "height:LDL", "height:Systol", "bmi:weight", "bmi:LDL", "bmi:Systol", "weight:LDL", "weight:Systol", "LDL:Systol"]

print("Means of columns 2, 3, 4, 5 with -1's removed\n")
corr2 = pd.DataFrame([coeffs2], columns = corrLabels)
print(dat2.mean().iloc[1:5])
print(f"\nCorrelation coefficients for first dataframe \n {corr2}")


dat3 = dat.copy()
oldMean = dat2["LDL"].mean()
dat3["LDL"].replace({-1: oldMean}, inplace=True)


co1 = dat3["height"].corr(dat3["bmi"])
co2 = dat3["height"].corr(dat3["weight"])
co3 = dat3["height"].corr(dat3["LDL"])
co4 = dat3["height"].corr(dat3["Systol"])
co5 = dat3["bmi"].corr(dat3["weight"])
co6 = dat3["bmi"].corr(dat3["LDL"])
co7 = dat3["bmi"].corr(dat3["Systol"])
co8 = dat3["weight"].corr(dat3["LDL"])
co9 = dat3["weight"].corr(dat3["Systol"])
co10 = dat3["LDL"].corr(dat3["Systol"])

coeffs3 = np.array([co1, co2, co3, co4, co5, co6, co7, co8, co9, co10])


print("Means of columns 2, 3, 4, 5 with -1's replaced with 129.904412\n")
corr3 = pd.DataFrame([coeffs3], columns = corrLabels)
print(dat3.mean().iloc[1:5])
print(f"\nCorrelation coefficients for second dataframe \n {corr3}")












