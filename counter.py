# -*- coding: utf-8 -*-
from nltk.tokenize import TweetTokenizer
import re
import codecs
import sys
import json
streamWriter = codecs.lookup('utf-8')[-1]
sys.stdout = streamWriter(sys.stdout)
stop_words = []
point = [u".",u"!",u"?",u"....",u"...",u".."]

def increase_counter(dic, w):
    try:
        dic[w] +=1
    except KeyError:
        dic[w] = 1

def normalize(dic):
    su = sum(dic.values())
    for w in dic.keys():
        dic[w] = float(dic[w])/su
    return dic

def construct_dict(tok):
    count_dict = {}
    #dic = collections.OrderedDict()
    one_dict = {}
    two_dict = {}
    alpha_re = re.compile(u'[a-z.а-я]+')
    prev_word = u"."
    prev_prev_word = None
    normal_words =[]
    for word in tok:
        w = word.lower()
        if w in point:
            w = u"."
        if alpha_re.match(w) != None:
            increase_counter(count_dict, w)
            normal_words.append(w)
                
            try:
                one_dict[prev_word]
            except KeyError:
                one_dict[prev_word] = {}

            try:
                one_dict[prev_word][w] += 1
            except KeyError:
                one_dict[prev_word][w] = 1

            if prev_prev_word != None:
                try:
                    two_dict[prev_prev_word]
                except KeyError:
                    two_dict[prev_prev_word] = {}

                try:
                    two_dict[prev_prev_word][prev_word]
                except KeyError:
                    two_dict[prev_prev_word][prev_word] = {}
                    
                try:
                    two_dict[prev_prev_word][prev_word][w] += 1
                except KeyError:
                    two_dict[prev_prev_word][prev_word][w] = 1


            prev_prev_word = prev_word
            if w == ".":
                prev_prev_word = None
            prev_word = w

    normalize(count_dict)
    for w in one_dict.keys():
        normalize(one_dict[w])

    for fw in two_dict.keys():
        for sw in two_dict[fw]:
            normalize(two_dict[fw][sw])

    saved_object = {}
    saved_object["count"] = count_dict
    saved_object["one"] = one_dict
    saved_object["two"] = two_dict
    return saved_object


def main():
    text = sys.stdin.read().decode("utf-8")

    tknzr = TweetTokenizer()
    tok = tknzr.tokenize(text)
    saved_object = construct_dict(tok)
    print json.dumps(saved_object)

if __name__ == "__main__":
    main()
