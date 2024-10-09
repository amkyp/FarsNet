
# 100 words /workspaces/FarsNet/step-1/farsnet_words_in_miras_occurrence-100-out-of-466-words_06-10-2024-01-17-51.csv

# 296 /workspaces/FarsNet/step-1/farsnet_words_in_miras_occurrence-296-out-of-396-words_06-10-2024-01-09-04.csv

# %%
# # read both each file word column 
import pandas as pd
import numpy as np
import csv
import json

# %%
import os
if not os.path.exists('/workspaces/FarsNet/step-3'):
    os.makedirs('/workspaces/FarsNet/step-3')


# %%
hundred_words = pd.read_csv('/workspaces/FarsNet/step-1/farsnet_words_in_miras_occurrence-100-out-of-466-words_06-10-2024-01-17-51.csv')
hundred_words = hundred_words['word'].tolist()
# save as a csv with the word column
hundred_words = pd.DataFrame(hundred_words, columns=['word'])
hundred_words.to_csv('/workspaces/FarsNet/step-3/100_words.csv', index=False)
# %%
# read and save the 296 words
two_ninety_six_words = pd.read_csv('/workspaces/FarsNet/step-1/farsnet_words_in_miras_occurrence-296-out-of-396-words_06-10-2024-01-09-04.csv')
two_ninety_six_words = two_ninety_six_words['word'].tolist()
# save as a csv with the word column
two_ninety_six_words = pd.DataFrame(two_ninety_six_words, columns=['word'])
two_ninety_six_words.to_csv('/workspaces/FarsNet/step-3/296_words.csv', index=False)

# %%

