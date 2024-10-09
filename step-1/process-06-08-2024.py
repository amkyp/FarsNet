# %%
import pandas as pd
import csv
import datetime

# Read the data from the file
with open("ambiguous_sentences-complete-06-d-2024_04-39-45.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    data = [row for row in reader]

# Print the first 5 rows
for row in data[:5]:
    print(row)

# Create a DataFrame from the data
df_temp = pd.DataFrame(data, columns=["word", "sentence"])
df_temp = df_temp.drop(0)
df_temp = df_temp[df_temp["word"] != "cd"]
display(df_temp)

# Get unique words
words = df_temp["word"].unique()
print("Number of unique words in the data:", len(words))

# # Save words as a csv file
# timestamp = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
# file_name = f"words-from-Farsnet-466_words-in-miras-occurrence_{timestamp}.csv"
# with open(file_name, "w", encoding="utf-8") as f:
#     writer = csv.writer(f)
#     writer.writerow(["word"])
#     writer.writerows([[word] for word in words])

# %%
# Count the frequency of each word
word_freq = {}
for word in words:
    word_freq[word] = df_temp[df_temp["word"] == word].shape[0]
print(word_freq)

# %%
# sort words by frequency
word_freq = dict(sorted(word_freq.items(), key=lambda item: item[1], reverse=True))
print(word_freq)


# %%
# words from FarsNet which have multiple senses (specifically more than equal 3)
# read and sort /workspaces/FarsNet/step-2/word_frequencies-06-08-2024_02-52-10.csv
import pandas as pd
df = pd.read_csv("/workspaces/FarsNet/step-2/word_frequencies-06-08-2024_02-52-10.csv", encoding="utf-8")
df = df.sort_values(by="frequency", ascending=False).reset_index(drop=True)
df

# کل کلمات که دارای ۳ و بیشتر معنی در فارس‌نت هستند را شامل می‌شود
# از پیکیره میراث استخراج گردیده است
# در واقع نعداد رخداد هر کلمه در پیکره میراث بررسی شده است

# %%
# find freq of words in df that are in step-1/words-from-Farsnet-466_words-in-miras-occurrence_06-09-2024-20-47-56.csv
df_freq = pd.read_csv("words-from-Farsnet-466_words-in-miras-occurrence_06-09-2024-20-47-56.csv", encoding="utf-8")
df_freq = df_freq[df_freq["word"].isin(df["word"])]
# with their freq in df
df_freq = df_freq.merge(df, on="word", how="left")
df_freq = df_freq.sort_values(by="frequency", ascending=False).reset_index(drop=True)
display(df_freq)
# cusum on freq
df_freq["cumsum"] = df_freq["frequency"].cumsum()
display(df_freq)
# sum of freq
print("sum of freq", df_freq["frequency"].sum())

# reverse df
df_freq = df_freq.sort_values(by="frequency", ascending=True).reset_index(drop=True)
display(df_freq)
df_freq["cumsum"] = df_freq["frequency"].cumsum()
df_freq = df_freq[df_freq["cumsum"] <= 100000]
display(df_freq)

print("<>"*20)

# find freq for words in  /workspaces/FarsNet/step-2/words-to-search-in-MirasText-08-06-2024-08-00-23.csv
df_freq_temp = pd.read_csv("/workspaces/FarsNet/step-2/words-to-search-in-MirasText-08-06-2024-08-00-23.csv", encoding="utf-8")
display(df_freq_temp)
df_freq_temp = df_freq_temp[df_freq_temp["word"].isin(df["word"])]
df_freq_temp = df_freq_temp.merge(df, on="word", how="left")
df_freq_temp = df_freq_temp.sort_values(by="frequency", ascending=False).reset_index(drop=True)
display(df_freq_temp)
# cumsum
df_freq_temp["cumsum"] = df_freq_temp["frequency"].cumsum()
display(df_freq_temp)

# save to csv
timestamp = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
# farsnet_words_in_miras_occurrence-296-out-of-396-words_06-10-2024-01-09-04.csv
df_freq_temp.to_csv(f"farsnet_words_in_miras_occurrence-100-out-of-466-words_{timestamp}.csv", index=False)

print("<>"*20)

# bring me the other words that are in df_freq but not in df_freq_temp
df_freq = df_freq[~df_freq["word"].isin(df_freq_temp["word"])]
# amd reset the cumsum
df_freq["cumsum"] = df_freq["frequency"].cumsum()
# reset index
df_freq = df_freq.reset_index(drop=True)
display(df_freq)
# display head 50
display(df_freq.tail(92))
# save to csv
# import datetime
# timestamp = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
# df_freq.to_csv(f"words_freq_366_from_466_words_{timestamp}.csv", index=False)

# show words that sum up to 30000 cumsum
temp_words_list = []
for i, row in df_freq.iterrows():
    temp_words_list.append(row["word"])
    if row["cumsum"] >= 103_900 :
        break

for i, word in enumerate(temp_words_list):
    print(i, word)

# check of the words in the list are in the df
print("number of words in the list", len(temp_words_list))
print("number of words in the df", len(df_freq))

# give me the other ones plus their freq
df_freq = df[~df["word"].isin(df_freq["word"])]
display(df_freq)

# %%
# skip low freq words
df_freq = df_freq[df_freq["frequency"] > 9]
# sorted
df_freq = df_freq.sort_values(by="frequency", ascending=False).reset_index(drop=True)
display(df_freq)

# 

# %%
df = pd.read_csv("/workspaces/FarsNet/step-2/ambiguous_sentences-complete-filtered-06-08-2024-08-12-19.csv", encoding="utf-8")
# drop row wehere word column is equal to word
df = df[df["word"] != "word"]
# reset index and save to csv
df.reset_index(drop=True, inplace=True)
df

# %%
# give me unique words in the df
words = df["word"].unique()
print("number of unique words in the data", len(words))
# ۱۰۰ 
# کلمه از کلمات داخل فارس‌نت که دارای بیشتر از ۳ معنا هستند
# و در پیکره میراث نیز وجود داشته‌اند

# %%
# get these word frequency in /workspaces/FarsNet/step-2/word_frequencies-06-08-2024_02-52-10.csv
df_freq = pd.read_csv("/workspaces/FarsNet/step-2/word_frequencies-06-08-2024_02-52-10.csv", encoding="utf-8")
df_freq = df_freq[df_freq["word"].isin(words)]
df_freq
# save as csv
# df_freq.to_csv("words_freq.csv", index=False)
# df_freq.to_html("words_freq.html")

# sort by frequency
df_freq = df_freq.sort_values(by="frequency", ascending=False).reset_index(drop=True)
df_freq

# %%
df = pd.read_csv("/workspaces/FarsNet/step-2/ambiguous_sentences-complete-filtered-06-08-2024-08-12-19.csv", encoding="utf-8")
# drop row wehere word column is equal to word
df = df[df["word"] != "word"]
# reset index and save to csv
df.reset_index(drop=True, inplace=True)
df

# %%
# words = df["word"].unique()
print("number of unique words in the data", len(words))
# ۱۰۰ 
# کلمه از کلمات داخل فارس‌نت که دارای بیشتر از ۳ معنا هستند
# و در پیکره میراث نیز وجود داشته‌اند

# %%

# خب الان می‌خوام یه لیست از تعداد کلماتی که تعداد معنی بالا دارند و هم توی پیکره ما به تعداد بالایی رخ دادن رو دربیارم

# توزیع فرکانس کلمات با استفاده از bin رو بررسی می‌کنم
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
# برای چی از قوطی استفاده می‌کنیم؟
# برای اینکه توزیع فرکانس کلمات رو ببینیم



# %%
# /workspaces/FarsNet/words_500-top-sense-freq-Farsnet-09-06-2024-22-46-15.csv

farsnet_words = pd.read_csv("/workspaces/FarsNet/words_500-top-sense-freq-Farsnet-09-06-2024-22-46-15.csv", encoding="utf-8")
display(farsnet_words)
# rename search_value to word
farsnet_words = farsnet_words.rename(columns={"search_value": "word"})

# miras farasnet-words-occurrence
farsnet_words_in_miras_occurrence = pd.read_csv("/workspaces/FarsNet/step-2/word_frequencies-06-08-2024_02-52-10.csv", encoding="utf-8")
display(farsnet_words_in_miras_occurrence)
# remove search_value to word

# show farsnet words in farsnet-words-in-miras-occurrence
farsnet_words_in_miras_occurrence = farsnet_words_in_miras_occurrence[farsnet_words_in_miras_occurrence["word"].isin(farsnet_words["word"])]
display(farsnet_words_in_miras_occurrence)

# sort by frequency column farsnet_words_in_miras_occurrence and word sense freq from farsnet_words
farsnet_words_in_miras_occurrence = farsnet_words_in_miras_occurrence.sort_values(by="frequency", ascending=False).reset_index(drop=True)
farsnet_words = farsnet_words.sort_values(by="frequency", ascending=False).reset_index(drop=True)
display(farsnet_words_in_miras_occurrence)

# join farsnet_words_in_miras_occurrence with farsnet_words
farsnet_words_in_miras_occurrence = farsnet_words_in_miras_occurrence.merge(farsnet_words, on="word", how="left")
display(farsnet_words_in_miras_occurrence)

# %%
# inline
%matplotlib inline
from matplotlib import pyplot as plt
import numpy as np

freq = farsnet_words_in_miras_occurrence["frequency_x"]
freq = freq.to_numpy()
freq = np.log(freq)
# print(freq)
# clip infs to 0
freq = np.clip(freq, 0, None)

plt.hist(freq, bins=20)
plt.show()

# ok show me the words that have freq > 9  and freq < 15
# log the freq
log_freq = np.log(farsnet_words_in_miras_occurrence["frequency_x"])
# clip infs to 0
log_freq = np.clip(log_freq, 0, None)
farsnet_words_in_miras_occurrence["log_freq"] = log_freq
display(farsnet_words_in_miras_occurrence)
farsnet_words_in_miras_occurrence = farsnet_words_in_miras_occurrence[farsnet_words_in_miras_occurrence["log_freq"] > 5]
farsnet_words_in_miras_occurrence = farsnet_words_in_miras_occurrence[farsnet_words_in_miras_occurrence["log_freq"] < 15.5]
display(farsnet_words_in_miras_occurrence)

# %%
# sort by frequency_y
farsnet_words_in_miras_occurrence = farsnet_words_in_miras_occurrence.sort_values(by="frequency_y", ascending=False).reset_index(drop=True)
display(farsnet_words_in_miras_occurrence)


# %%
# sort by log_freq and frequency_y

# round log_freq and then sort
farsnet_words_in_miras_occurrence["log_freq"] = farsnet_words_in_miras_occurrence["log_freq"].round()
farsnet_words_in_miras_occurrence = farsnet_words_in_miras_occurrence.sort_values(by=["log_freq", "frequency_y"], ascending=False).reset_index(drop=True)
display(farsnet_words_in_miras_occurrence)

# # %%
# # drop rows with 0 log_freq
# farsnet_words_in_miras_occurrence = farsnet_words_in_miras_occurrence[farsnet_words_in_miras_occurrence["log_freq"] > 0]
# display(farsnet_words_in_miras_occurrence)

## %%

# # show rows with log_freq 5
# farsnet_words_in_miras_occurrence = farsnet_words_in_miras_occurrence[farsnet_words_in_miras_occurrence["log_freq"] == 6]
# display(farsnet_words_in_miras_occurrence)

# %%
# save to csv
import datetime
timestamp = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
farsnet_words_in_miras_occurrence.to_csv(f"farsnet_words_in_miras_occurrence_{timestamp}.csv", index=False)

# %%
# show words in farsnet_words_in_miras_occurrence
words = farsnet_words_in_miras_occurrence["word"].to_list()
display(words)

# %%
# display(farsnet_words_in_miras_occurrence)

# drop the word from words_to_search in farsnet_words_in_miras_occurrence
words_to_search = pd.read_csv("/workspaces/FarsNet/step-2/words-to-search-in-MirasText-08-06-2024-08-00-23.csv", encoding="utf-8")
words_to_search = words_to_search[words_to_search["word"].isin(words)]
display(words_to_search)

# show farasnet-words-in-miras-occurrence
farsnet_words_in_miras_occurrence = farsnet_words_in_miras_occurrence[~farsnet_words_in_miras_occurrence["word"].isin(words_to_search["word"])]
display(farsnet_words_in_miras_occurrence)



# %%
# save to csv
import datetime
timestamp = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
farsnet_words_in_miras_occurrence.to_csv(f"farsnet_words_in_miras_occurrence-296-out-of-396-words_{timestamp}.csv", index=False)

# %%
# save 100





# read word column values from the data
# %%
words = [row[0] for row in data]
print("number of words in the data", len(words))

# %%
# get unique words
unique_words = list(set(words))
print("number of unique words in the data", len(unique_words))
print("number of words in the data", len(words))
print("words: ", unique_words)

# %%
# check which words are in the log
import json
import csv

with open("words_06-07-2024_23-14-51.csv", "r", encoding="utf-8") as f:
    # read with header as word
    reader = csv.reader(f)
    words = [row[0] for row in reader]
    # skip header
    words = words[1:]
    print("number of words in wordlist from farsnet, with sense count of >= 7 to <=15", len(words))
result = {}
for word in unique_words:
    result[word] = word in words

# %%
# save the result to a json file
with open("words_in_log.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)
print(json.dumps(result, indent=4, ensure_ascii=False))

print(len(result))

# %%
# only keep the row in ambiguous_sentences-complete-06-d-2024_04-39-45.csv if the word is in result
data = [row for row in data if result[row[0]]]

# save the data to a new file
with open("ambiguous_sentences-complete-06-d-2024_04-39-45-filtered.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# %%
# read unique words from the filtered data
words = [row[0] for row in data]
unique_words = list(set(words))
print("number of unique words in the filtered data", len(unique_words))
print("number of words in the filtered data", len(words))

# %%
# write the unique words to a csv file.
with open("unique_words_06-08-2024.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["word"])
    for word in unique_words:
        writer.writerow([word])


# %%
# extract words in step-2/words-to-search-in-MirasText-08-06-2024-08-00-23.csv and filter step-2/ambiguous_sentences-complete-filtered-06-08-2024-06-51-49-without-english.csv on column word to get the filtered data

import pandas as pd
import csv
# "/workspaces/FarsNet/step-2/words-to-search-in-MirasText-08-06-2024-08-00-23.csv
words_to_search = pd.read_csv("/workspaces/FarsNet/step-2/words-to-search-in-MirasText-08-06-2024-08-00-23.csv", encoding="utf-8")
# drop row wehere word column is equal to word
words_to_search = words_to_search[words_to_search["word"] != "word"]
# reset index
words_to_search.reset_index(drop=True, inplace=True)
display(words_to_search)


# with open("/workspaces/FarsNet/step-2/ambiguous_sentences-complete-filtered-06-08-2024-06-51-49-without-english.csv", "r", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     data = [row for row in reader]
# print("number of rows in the data", len(data))


# get unique words
unique_words = list(set(words))
print("number of unique words in the data", len(unique_words))

# filter ambiguous_sentences-complete-filtered-06-08-2024-06-51-49-without-english.csv on column word using pandas
df = pd.DataFrame(data, columns=["word", "sentence"])
df = df[df["word"].isin(unique_words)]
print("number of rows in the filtered data", len(df))

# %%
import datetime
timestamp = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
# drop row wehere word column is equal to word
df = df[df["word"] != "word"]
# reset index and save to csv
df.reset_index(drop=True, inplace=True)
df.to_csv(f"ambiguous_sentences-complete-filtered-{timestamp}.csv", index=False)

# %%
import os
import pandas as pd
import datetime
import numpy as np
import csv

# load and show df
df = pd.read_csv("/workspaces/FarsNet/step-2/ambiguous_sentences-complete-filtered-06-08-2024-08-12-19.csv", encoding="utf-8")
df

# %%
# give me unique words in the df
words = df["word"].unique()
print("number of unique words in the data", len(words))

# %%
# devide my df to dfs of 1000 rows
import datetime
import csv
import pandas as pd
import csv
import pandas as pd
import datetime
import csv
import pandas as pd
chunks = []
for i in range(0, len(df), 1000):
    chunks.append(df[i:i+1000])
print("number of chunks", len(chunks))
# save each chunk to a csv file
timestamp = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
if os.path.exists("chunks") == False:
    os.mkdir("chunks")
for i, chunk in enumerate(chunks):
    chunk.to_csv(f"chunks/ambiguous_sentences-complete-filtered-{timestamp}-chunk-{i}.csv", index=False)

# %%
print(chunks)

# %%
# save each chunk to a csv file
timestamp = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
for i, chunk in enumerate(chunks):
    chunk.to_csv(f"MirasText-Sentences-{timestamp}-chunk-{i}.csv", index=False)


# %%
# use bash to zip chunks
!zip -r chunks.zip chunks
# %%
