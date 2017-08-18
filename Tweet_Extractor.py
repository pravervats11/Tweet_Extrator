#!/usr/bin/env python3.5

from tkinter import *
import tweepy
from tweepy import OAuthHandler
import textblob
import re
import json
import codecs
import sys
import time
import webbrowser

def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))


def get_tweets():
    consumer_key = 'your_consumer_key'
    consumer_secret = 'your_consumer_secret'
    access_token = 'your_access_token'
    access_token_secret = 'your_access_token_secret'

    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    twitter_handle = e2.get()
    name = e1.get()
    alltweets = []
    
    new_tweets = api.user_timeline(twitter_handle, count=200)
       
    alcoholism = ["beer","alcohol","high","wasted","booz","Whiskey","vodka"]
    
    final_tuple = []
    for tweet in new_tweets:
        for word in alcoholism:
            if word.lower() in tweet.text.lower():
                final_tuple.append((tweet.text, tweet.id, "Alcoholism", word))
                break

    f = open('{0}_{1}.txt'.format(name, twitter_handle), 'w')

    f.write(str(final_tuple))
    f.close()
    print("Tweets have been extracted successfully !!")

def open_file():
    webbrowser.open_new("{0}_{1}.txt".format(e1.get(), e2.get()))

master = Tk()
master.title("Tweet Extractor")
Label(master, text= "Name").grid(row=0, sticky=S, pady =4)
Label(master, text= "Twitter Handle").grid(row=1, sticky=S, pady =4)
Label(master, text= "Date:" + "{0}".format(time.strftime("%d/%m/%Y"))).grid(row=2, column=0)

Label(master, text= "Time:" + "{0}".format(time.strftime("%H:%M:%S"))).grid(row=2, column=2)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=2)
e2.grid(row=1, column=2)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=E, pady=4)
Button(master, text='OK', command= get_tweets).grid(row=3, column=1, sticky=E, pady=4)
Button(master, text='Open File', command= open_file).grid(row=4, column=1,sticky =E, pady = 4)
mainloop( )
