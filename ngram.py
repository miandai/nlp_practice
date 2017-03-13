import jieba.posseg as pseg
from collections import Counter

def ngram_count(file_name,n_gram):
    lm = Counter()
    for line in open(file_name):
        words = pseg.cut(line.strip())
        words = [i for i in words]
        for i in range(0, len(words)-n_gram):
            if 'x' in [k.flag for k in words[i:i+n_gram]]:#ÅÅ³ý±êµã·ûºÅ
                continue
            lm[' '.join([k.word for k in words[i:i+n_gram]])]+=1
    return lm
	
lm = ngram_count('Data/The_last_glory_of_Empire.txt',2)
for word,cnt in lm.most_common(10):
        print('%s %d' % (word,cnt))