# -*- coding: utf-8 -*-
import json
import sys



from numpy.random import choice
def wchoice(dic):
    return choice(dic.keys(), p=dic.values())

js = sys.stdin.read()
loaded_object = json.loads(js)

count_dict = loaded_object["count"]
one_dict = loaded_object["one"]
two_dict = loaded_object["two"]

"""
for w in sorted(d, key=d.get, reverse=False):
    print w.encode("utf-8"), d[w]
"""
text_arr = []
text_str = ""

while len(text_arr) < 100:
    prev_prev = wchoice(count_dict) 
    if prev_prev == ".":
        continue
    text_str += prev_prev.capitalize()
    text_arr.append(prev_prev.capitalize())
    prev = wchoice(one_dict[prev_prev])
    if prev == u".":
        prev = wchoice(one_dict[prev_prev])
    if prev != u".":
        text_str += " "
    text_str += prev
    text_arr.append(prev)

    while prev != u".":
        word = wchoice(two_dict[prev_prev][prev])
        if word != u".":
            text_str += " "
        text_str += word
        text_arr.append(word)
        prev_prev = prev
        prev = word
    text_str += " "
    #text_str += "|"

print text_str.encode("utf-8")


