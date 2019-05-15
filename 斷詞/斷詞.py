mport ckip
import pandas as pd
import numpy as np
import glob
from ckip import CkipSegmenter
from os import open

#-----------讀資料----------------

read_files = glob.glob(r'/Users/jianweicheng/Desktop/ＮＴＵＴ/Data for life and future/決選/假的NLP/PTT/女兵日記/選好/內容/*.csv')
print(read_files)
data = []
# for j in range(len(read_files)):

sourceUrl = pd.read_csv(read_files[1], sep=',', encoding='utf-8')
sourceUrl = pd.DataFrame(sourceUrl)

# print((sourceUrl))
# print(len(sourceUrl))

for j in range(230, len(sourceUrl)):
# j = 0
# for j in range(588):
    a = [j]
    b = '62'
    ##從233 333 433開始
    for i in a:
        text = sourceUrl['content'][i]


    # with open(sourceUrl, 'r', encoding="utf-8") as f:
    #     for line in sourceUrl['content']:
    #         line = line.replace('\n', '').split(',')
    #         data += line





    # text = line
    # # text = np.array(data)
    # # text = text.decode('utf-8')

    #--------------切字--------------

        segmenter = CkipSegmenter()


        result = segmenter.seg(text)

        # result.res is a list of tuples contain a token and its pos-tag.
        # print('result.res: {}\n'.format(result.res))

        # result.tok and result.pos contains only tokens and pos-tags respectively.
        # print('result.tok: {}\n'.format(result.tok))
        # print('result.pos: {}\n'.format(result.pos))

        print(result.tok)
        a1 = pd.value_counts(result.tok)
        print(a1)
        a1 = pd.DataFrame(a1)
        print(a1)

    dataName='/Users/jianweicheng/Desktop/ＮＴＵＴ/Data for life and future/決選/假的NLP/PTT/女兵日記/選好/內容/新結果/'+ str(j) +'.csv'
    a1.to_csv(dataName, encoding="utf_8_sig")
    print(j)

