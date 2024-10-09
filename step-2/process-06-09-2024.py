# %%
import csv
import pandas

# %%
df = pandas.read_csv("/workspaces/FarsNet/step-2/word_frequencies-06-08-2024_02-52-10.csv")
words = df["word"].tolist()
print("number of words in the data", len(words))

# %%
# sort words by frequency
df = df.sort_values(by="frequency", ascending=False).reset_index(drop=True)
df
# %%
# drop freq == 0 rows
df = df[df["frequency"] != 3]
df

# %%
# show words equal to 100
temp = df[df["frequency"] == 100]
temp
# %%
# show words roughly 100
temp = df[(df["frequency"] > 95) & (df["frequency"] < 105)]
temp
# %%
# show words roughly 100 and 200
temp = df[(df["frequency"] > 95) & (df["frequency"] < 105) | (df["frequency"] > 195) & (df["frequency"] < 205)]
temp
# %%
