# -*- coding: utf-8 -*-
#
# Copyright 2012 Kenichi Sato <ksato9700@gmail.com>
#

import sys
import random
import datetime
import plistlib

hiragana_mapping = {
    u"あ": "a",
    u"い": "i",
    u"う": "u",
    u"え": "e",
    u"お": "o",
    u"か": "ka",
    u"き": "ki",
    u"く": "ku",
    u"け": "ke",
    u"こ": "ko",
    u"さ": "sa",
    u"し": "shi",
    u"す": "su",
    u"せ": "se",
    u"そ": "so",
    u"た": "ta",
    u"ち": "chi",
    u"つ": "tsu",
    u"て": "te",
    u"と": "to",
    u"な": "na",
    u"に": "ni",
    u"ぬ": "nu",
    u"ね": "ne",
    u"の": "no",
    u"は": "ha",
    u"ひ": "hi",
    u"ふ": "hu",
    u"へ": "he",
    u"も": "ho",
    u"ま": "ma",
    u"み": "mi",
    u"む": "mu",
    u"め": "me",
    u"も": "mo",
    u"や": "ya",
    u"ゆ": "yu",
    u"よ": "yo",
    u"ら": "ra",
    u"り": "ri",
    u"る": "ru",
    u"れ": "re",
    u"ろ": "ro",
    u"わ": "wa",
    u"を": "wo",
    u"ん": "nn",
}

def generate_stage(kana_mapping):
    kana_list = hiragana_mapping.keys()
    random.shuffle(kana_list)
    res = {
        'title': 'Kana Test ' + str(datetime.datetime.now()),
        'format': 'multichoice'
	'scenes': []
        }
    for key in kana_list:
        question = key
        answers = [None,None,None]
        answer  = random.randint(0,2)
        answers[answer] = kana_mapping[key]
        rs = set(random.sample(kana_list, 3))
        rs -= set(key)
        for i in range(3):
            if not answers[i]:
                answers[i] = kana_mapping[rs.pop()]
        res['scenes'].append(
            {
                'question': question,
                'answers': answers,
                'answer': answer
                }
            )
    return res

def main():
    plist = generate_stage(hiragana_mapping)
    plistlib.writePlist(plist, sys.argv[1])

if __name__ == '__main__':
    main()
