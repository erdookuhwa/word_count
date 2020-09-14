import os
import pprint
import operator

def word_count(filename):
    DIR = os.path.dirname(__file__)
    text_to_be_read = os.path.join(DIR, filename)
    with open(text_to_be_read) as file_obj:
        contents = file_obj.read()
        formatted_contents = contents.lower().split()
        dic = {}
        for word in formatted_contents:
            dic.setdefault(word, 0)
            dic[word] += 1
            sorted_dic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
        pprint.pprint(sorted_dic)

word_count('article.txt')