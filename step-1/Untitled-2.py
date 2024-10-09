# %%
import json
import csv

with open("run2_log-also-stopwords-removed.json", "r", encoding="utf-8") as f:
    log = json.load(f)

with open("words_06-07-2024_23-14-51.csv", "r", encoding="utf-8") as f:
    # read with header as word
    reader = csv.reader(f)
    words = [row[0] for row in reader]
    # skip header
    words = words[1:]

print("number of words in wordlist from farsnet, with sense count of >= 7 to <=15", len(words))    

# %%
result = {}
for word in words:
    if word in log:
        result[word] = log[word]
    
print(json.dumps(result, indent=4, ensure_ascii=False))

print(len(result))

# %%
    
with open("words_in_log.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)
print(json.dumps(result, indent=4, ensure_ascii=False))

print(len(result))

# %%
# print len result
print("len(result) = ", len(result))

# %%
import datetime
timestamp = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
print(timestamp)

# %%
with open(f"words_in_log_{timestamp}.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["word"])
    for word in result:
        writer.writerow([word])

# %%
import json
import csv

with open("run2_log-also-stopwords-removed.json", "r", encoding="utf-8") as f:
    log = json.load(f)
with open("words_06-07-2024_21-57-03.csv", "r", encoding="utf-8") as f:
    # read with header as word
    reader = csv.reader(f)
    words = [row[0] for row in reader]
    # skip header
    words = words[1:]
    print("number of words in wordlist from farsnet, with sense count of >= 7 to <=15", len(words))
result = {}
for word in words:
    if word in log:
        result[word] = log[word]

import datetime
timestamp = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
with open(f"words_in_log_{timestamp}.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)
print(json.dumps(result, indent=4, ensure_ascii=False))

print(len(result))

# %%
# sort result dict by value
result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
print(json.dumps(result, indent=4, ensure_ascii=False))

# %%
# bring me the 400 tail of the sorted result
result = dict(list(result.items())[-400:])
display(result)

# %%
# bring me the 400 tail of the sorted result
result = dict(list(result.items())[-100:])
display(result)

# %%
# sum of the values in the result
sum(result.values())

# %%
# I want to read my data in a csv file as in below:
# word,frequency
# ??,314370
# ???????,23243
# ??,546261
# ?????,245294
# ??,159236
# ?????,39511
# ???,116699
# ???,739651

with open("word_frequencies06-d-2024_02-52-10.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)
    data = {row[0]: int(row[1]) for row in reader}
    
print(json.dumps(data, indent=4, ensure_ascii=False))


# %%
import json
import csv

with open("run3_log.json", "r", encoding="utf-8") as f:
    log = json.load(f)
with open("words_06-07-2024_21-57-03.csv", "r", encoding="utf-8") as f:
    # read with header as word
    reader = csv.reader(f)
    words = [row[0] for row in reader]
    # skip header
    words = words[1:]
    print("number of words in wordlist from farsnet, with sense count of >= 7 to <=15", len(words))
result = {}
for word in words:
    if word in log:
        result[word] = log[word]

import datetime
timestamp = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
with open(f"words_in_log_{timestamp}.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=4, ensure_ascii=False)
print(json.dumps(result, indent=4, ensure_ascii=False))

print(len(result))

# %%
# sort result dict by value
result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
print(json.dumps(result, indent=4, ensure_ascii=False))
# bring me the 400 tail of the sorted result

# %%
result = dict(list(result.items())[-100:])
display(result)

sum(result.values())
sum(dict(list(result.items())[-100:]).values())

# %%
# apply int to the values of the result
# result = {k: int(v) for k, v in result.items()}

# %%
# give me keys of the result that sum up to 100000
# start from least frequent words and don't count words with less than 10 frequency
keys = []
total = 0
result = dict(sorted(result.items(), key=lambda item: item[1], reverse=True))
for key in result:
    if int(result[key]) >= 10 and total < 100000:
        keys.append(key)
        total += result[key]
        if total >= 100000:
            break
print(keys)
print(total)

# %%
# Ok got the keys as a list, now I want to write them as json with their value
# keys are words
print(json.dumps({key: result[key] for key in keys}, indent=4, ensure_ascii=False))
# save as json
with open(f"words_in_log_{timestamp}.json", "w", encoding="utf-8") as f:
    json.dump({key: result[key] for key in keys}, f, indent=4, ensure_ascii=False)

# %%
# save as csv
with open(f"words_in_log_{timestamp}.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["word"])
    for key in keys:
        writer.writerow([key.strip()])

# %%


# %%


# %%
# read ambiguous_sentences-complete-06-d-2024_04-39-45.csv
import json
import csv
import datetime
with open("ambiguous_sentences-complete-06-d-2024_04-39-45.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    data = [row for row in reader]
# print(data)

# drop rows which word == cd are in them
data = [row for row in data if row[0] != "cd"]
# save the data to a new file
timestamp = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
with open(f"ambiguous_sentences-complete-filtered-{timestamp}.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)


# %%

# read this file to check if the word cd is in it
# ambiguous_sentences-complete-06-d-2024_04-39-45-filtered.csv
with open("ambiguous_sentences-complete-06-d-2024_04-39-45-filtered.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    data = [row for row in reader]

# Print as dataframe
import pandas as pd
df = pd.DataFrame(data)
df

# %%
# change column names to word and sentence
df.columns = ["word", "sentence"]
df

# %%
# remove word if it's english
import re
df_without_english_words = df[~df["word"].str.contains(r"[a-zA-Z]", flags=re.IGNORECASE, regex=True)]
df_without_english_words

# %%
# show rows which are deleted from the original data
temp = df[~df.index.isin(df_without_english_words.index)]
# unique words in this data
unique_words = list(set(temp["word"]))
print("number of unique words in the data", len(unique_words))
print("number of words in the data", len(temp["word"]))
print("words: ", unique_words)

# %%
# save df_without_english_words as a new csv 
timestamp = datetime.datetime.now().strftime("%m-%d-%Y-%H-%M-%S")
df_without_english_words.to_csv(f"ambiguous_sentences-complete-filtered-{timestamp}-without-english.csv", index=False, encoding="utf-8")


# %%
# read word column values from the data and save them unique as a csv
word_list = list(set(df_without_english_words["word"]))
with open(f"words_{timestamp}.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["word"])
    for word in word_list:
        writer.writerow([word])

print("number of words in the data", len(word_list))
print("words: ", word_list)


# %%
