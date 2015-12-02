# -*- coding: utf-8 -*-
import json
import sys



from numpy.random import choice
def wchoice(dic):
    return choice(dic.keys(), p=dic.values())

def write_text(count_dict, one_dict, two_dict, length=10000):
    text_arr = []
    word_counter = 0
    text_str = ""

    while length > word_counter:
        prev_prev = wchoice(count_dict) 
        if prev_prev == ".":
            continue
        text_str += prev_prev.capitalize()
        word_counter += 1
        prev = wchoice(one_dict[prev_prev])
        if prev == u".":
            prev = wchoice(one_dict[prev_prev])
        if prev != u".":
            text_str += " "
        text_str += prev
        word_counter += 1
        text_arr.append(prev)

        while prev != u".":
            word = wchoice(two_dict[prev_prev][prev])
            if word != u".":
                text_str += " "
            text_str += word
            word_counter += 1
            text_arr.append(word)
            prev_prev = prev
            prev = word
        text_str += " "
        #text_str += "|"

    return text_str

 
def main():
    js = sys.stdin.read()
    loaded_object = json.loads(js)

    count_dict = loaded_object["count"]
    one_dict = loaded_object["one"]
    two_dict = loaded_object["two"]
    if len(sys.argv) > 1:
        text_str = write_text(count_dict, one_dict, two_dict, int(sys.argv[-1]))
    else:
        text_str = write_text(count_dict, one_dict, two_dict)
    print text_str.encode("utf-8")

if __name__ == "__main__":
    main()


