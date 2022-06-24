import  os
import random
BACKGROUND_COLOR = "light blue"
from tkinter import *
from tkinter import  messagebox
import pandas
english_word=""
random_word=""
data=""
with open ("scoreboard.txt") as scoreboard:
    score=int(scoreboard.read())
#---------------generate word-----------
def flip_card(card_back):
    canvas.itemconfig(canvas_image,image=card_back)
    canvas.itemconfig(title,text="English")
    canvas.itemconfig(word,text=english_word)
    answer_entry.grid_remove()
    right_button.grid_remove()
def generate_word():
    answer_entry.delete(0,END)
    answer_entry.grid(row=2,column=1,columnspan=2)
    right_button.grid(row=2,column=2)
    global english_word ,random_word
    random_word=random.choice(data)
    french_word=random_word["French"]
    english_word=random_word["English"]
    canvas.itemconfig(canvas_image,image=card_front)
    canvas.itemconfig(title,text="French")
    canvas.itemconfig(word,text=french_word)
def get_answer():
    global  user_answer,score
    user_answer=answer_entry.get()
    if len(user_answer) <= 0:
        messagebox.showinfo(title="Oops",message="Try your luck by typing something")
    else:
        if user_answer.lower() == english_word.lower():
            score += 1
            score_label.config(text=f"Score:{score}/100")
            data.remove(random_word)
            print(len(data))
            words_to_learn = pandas.DataFrame(data)
            words_to_learn.to_csv("data/remaining_words_to_learn.csv", index=False)
            with open("scoreboard.txt", "w") as scoreboard:
                scoreboard.write(f"{score}")
            messagebox.showinfo(title="Correct",message="You got it right")
            generate_word()
        else:
            messagebox.showinfo(title="Incorrect",message="You got it wrong\nReview it again")
            window.after(100,flip_card,card_back)
    answer_entry.delete(0,END)


#----------User Interface -----------
window=Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR,padx=50,pady=50)
#timer=window.after(3000,func=flip_card)
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

score_label=Label(text=f"Score:{score}",font=("Arial",20,"italic"),fg="green",bg="light blue")
score_label.grid(row=0,column=2,columnspan=2)
answer_entry=Entry(font=("Arial",19))
answer_entry.grid(row=2,column=1,columnspan=2)
progress_check=messagebox.askyesno(title="Progress check",message="Do you want to retain your old progress?")
if not progress_check:
    score = 0
    file="data/remaining_words_to_learn.csv"
    if (os.path.exists(file) and os.path.isfile(file)):
        os.remove(file)
    with open("scoreboard.txt","w") as scoreboard:
        scoreboard.write(f"{score}")
        score_label.config(text=f"Score:0/100")
    new_data_frame=pandas.read_csv("data/french_words.csv")
    data=new_data_frame.to_dict(orient="records")
else:
    try:
        new_data_frame = pandas.read_csv("data/remaining_words_to_learn.csv")
    except FileNotFoundError:
        data_frame = pandas.read_csv("data/french_words.csv")
        data = data_frame.to_dict(orient="records")

    else:
        data = new_data_frame.to_dict(orient="records")

generate_word()

window.after(10000,messagebox.showinfo(title="I love french",message="Click on the green tick button to check answer\nClick on the next "
                                                  "button to skip or get another word"))

answer_entry.focus_force()


window.mainloop()
