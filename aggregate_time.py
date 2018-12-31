# coding:utf-8
import csv
import collections
import pandas as pd

df = pd.read_csv('./output/time_data.csv', parse_dates=[0], header=None, index_col=[0])
print(df)


# with open('./output/user_data', 'r') as f:
#     reader = csv.reader(f, delimiter='\t')
#     texts = []
#     for row in reader:
#         if(len(row) > 0):
#             texts.append(row[0])

# # print(texts)
# words2 = collections.Counter(texts)
# print(words2.most_common(10))

# f_out = open('./output/user_count_data', 'w')

# for item in words2.most_common(100):
#     print(item)
#     f_out.write(item[0] + " : " +str(item[1]) + "ツイート" + '\n')

# f_out.close()

# words_count, words = counter(texts)
# text = ' '.join(words)
