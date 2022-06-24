import random
BACKGROUND_COLOR = "light blue"
from tkinter import *
from tkinter import  messagebox
import pandas
english_word =""
#---------------generate word-----------

data_frame=pandas.read_csv("data/french_words.csv")
data=data_frame.to_dict(orient="records")
def flip_card(card_back):
    canvas.itemconfig(canvas_image, image=card_back)
    canvas.itemconfig(title, text="English")
    canvas.itemconfig(word, text=current_word["English"])

def generate_word():

    global  english_word,timer
    window.after_cancel(timer)
    random_data= random.choice(data)
    french_word=random_data["French"]
    english_word=random_data["English"]
    canvas.itemconfig(canvas_image, image=card_front)
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(word,text=french_word,fill="black")
    timer = window.after(3000, flip_card, card_back)
    return  random_data

#----------User Interface -----------
window=Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
timer=window.after(3000,func=flip_card)

right_tick_image=PhotoImage(file="images/right.png")
right_button=Button(image=right_tick_image,highlightthickness=0,command=get_answer)
right_button.grid(row=2,column=2)

next_tick_image=PhotoImage(file="images/next_arrow.png")
next_button=Button(image=next_tick_image, highlightthickness=0, command=generate_word)
next_button.grid(row=2, column=1)

canvas=Canvas(width=800,height=526)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=1,column=1,columnspan=2,)

card_front=PhotoImage(file="images/card_front.png")
card_back=PhotoImage(file="images/card_back.png")
canvas_image=canvas.create_image(400,263,image=card_front)
title=canvas.create_text(400,132,text="",font=("Ariel",40,"italic"))
word=canvas.create_text(400,265,text="",font=("Ariel",55,"bold"))

generate_word()
messagebox.showinfo(title="I love french",message="Click on the green tick button to check answer\nClick on the next "
                                                  "button to skip word")



window.mainloop()

