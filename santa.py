#!/usr/bin/env python
import random
from time import sleep
from googlevoice import Voice
import ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open(r'numbers.cfg'))
voice = Voice()
voice.login()

names = ['CookieMonster', 'Sandy', 'Candybar' ]
matches = ['CookieMonster', 'Sandy', 'Candybar' ]
random.shuffle(names)        
random.shuffle(matches)
def Pick_match (n,matches):
    sleep(1)
    global pick
    global match
    if len(matches) > 1:
        p = random.randrange(1,len(matches))
    else:
        p = 0
    match = matches[p]
    if match is n:
        try:
            match = matches[(p+1)]
        except:
            match = matches[(p-1)]
    matches.remove(match)
    return match, matches

for n in names:
    Pick_match(n,matches)
    text = "Hi %s! Please provide a gift for %s\nHappy Holidays!\n" % (n, match)
    number = config.get('Phone Numbers', n) 
    voice.send_sms(number, text)

