def check_contain_chinese(check_str):
    for ch in check_str:
        if ch < u'\u4e00' or ch > u'\u9fff':
            return False
    return True

def get_highfreq_wordtuple(file_path,top_n=10,min_char_count=1):
    worddics={}
    file_object=open(file_path)
    lines = file_object.readlines()
    for line in lines:
        wordlist = line.decode("utf-8").split(" ")
        lenrange = range(len(wordlist)-1)
        for i in lenrange:
            if len(wordlist[i])>=min_char_count and len(wordlist[i+1])>=min_char_count \
            and check_contain_chinese(wordlist[i]) and check_contain_chinese(wordlist[i+1]):
                wordtuple = wordlist[i]+" "+wordlist[i+1]
                worddics.setdefault(wordtuple,0)
                worddics[wordtuple]+=1
    wordsorted = sorted(worddics.items(), key=lambda e:e[1], reverse=True)
    return wordsorted[0:top_n-1]

# Example
filepath = "./Data/happiness_seg.txt"
topn=10
wordsorted=get_highfreq_wordtuple(filepath,topn,2)
for e in wordsorted:
    print e[0],e[1]