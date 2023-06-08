import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
con = sqlite3.connect("pytut.db")

df = pd.read_csv(r"C:\\Users\\pranjan24\\Downloads\\2021VAERSData (1)\\2021VAERSData.csv",encoding="utf-8")

print(df.head())
print(df.tail())
print(df.info())
print(df['STATE'])
# print(df.to_sql("covid",con))
print(df['AGE_YRS'].plot())
plt.imshow(img.reshape((28, 28)))
plt.show()
