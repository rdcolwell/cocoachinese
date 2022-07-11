#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 16:45:50 2022

@author: richardcolwell
"""
import pandas as pd
from tkinter import *
from tkinter import ttk
import random as rand

#reads from a .csv file with headings: "Chinese character", "Pinyin", and "English Translation"]
chinese_df = pd.read_csv('chinese.csv', encoding='utf-8')

#Set lists of all vowel representations of tones in pinyin
neutral_tones = ['a','e','i','o','u']
rising_tones = ['á','é','í','ó','ú']
falling_tones = ['à','è','ì','ò','ù','ǚ']
low_tones = ['ǎ','ě','ǐ','ǒ','ǔ']
high_tones = ['ā','ē','ī','ō','ū']

#Creates a dictionary of tones based on tone names; values include the above lists of all vowels for that tone, and a unique color
tones_color_dictionary = {}
tones_color_dictionary['neutral'] = [neutral_tones,'#e261ff'] #purple
tones_color_dictionary['rising'] = [rising_tones,'#4cfc69'] #green
tones_color_dictionary['falling'] = [falling_tones,'#ff4f42'] #red
tones_color_dictionary['low'] = [low_tones,'#f6fc4c'] #yellow
tones_color_dictionary['high'] = [high_tones,'#17a2ff'] #blue

#creates a list of colors based on what tone is found in each character in the original .csv file
#note: this presumes that there is only one character and is not suitable for character pairs
#note: this is also not suitable for single characters containing multiple vowels, e.g. the verb "to speak:shuō/说"
colors = []
for pinyin in chinese_df['Pinyin']:
    for tone in tones_color_dictionary:
        for vowel in tones_color_dictionary[tone][0]:
            if vowel in pinyin:
                colors.append(tones_color_dictionary[tone][1])
                
#creates a new column in the dataframe to include the "tone color" and writes this to the original .csv file
#index=False above ensures that the index is not duplicated ad infinitum. Encoding ensures that the pinyin stays in tact.
chinese_df['Tone Color'] = colors
chinese_df.to_csv('chinese.csv',index=False, encoding='utf_8_sig')

#creates a tkinter window/interface
interface = Tk()
interface.geometry('400x400')
interface.title("Color-Coded Mandarin Flash Cards")
title = Label(interface,text="Color-coded Mandarin flash cards with spaced repitition!",)
title.pack()

#randomly picks a word from the data frame and returns the corresponding character, pinyin, etc. as variables in a list

def picknewword():
    index = rand.choice(range(len(chinese_df)))
    current_character = chinese_df['Chinese character'][index]
    current_pinyin = chinese_df['Pinyin'][index]
    current_translation = chinese_df['English Translation'][index]
    current_color = chinese_df["Tone Color"][index]

    displaychar.configure(text=current_character,bg=current_color)
    global sticky_values 
    sticky_values = [current_pinyin,current_translation]
    
#assigns current word's attributes to the "current word," and adds the character (over the "tone color" background, centered) to the tkinter interface
displaychar = Label(interface,text="",font=("Arial",120),fg="white")
displaychar.place(relx=0.5, rely=0.3, anchor=CENTER)

displaymeaning = Label(interface,text="",font=("Arial",12),fg="black")
displaymeaning.place(relx=0.5, rely= 0.65, anchor=CENTER)

newwordbutton = Button(interface,text="Click to generate a character to quiz yourself on!",fg="black", command=picknewword)
newwordbutton.place(relx=0.5, rely=0.8, anchor=CENTER)

def revealmeaning():
    meaningtext = "The pinyin for this character is:"+str(sticky_values[0])+ " and the meaning is '"+str(sticky_values[1])+"'"
    displaymeaning.configure(text=meaningtext,font=("Arial",12),fg="black")

revealmeaningbutton = Button(interface,text="Click to check the pinyin and meaning of this character!",command=revealmeaning)
revealmeaningbutton.place(relx=0.5, rely=0.55, anchor=CENTER)


#displays the tkinter interface
interface.mainloop()



        
