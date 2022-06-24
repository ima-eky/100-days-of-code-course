from tkinter import  *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN =20
reps=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_label.config(text="Timer")
    check_marks.config(text="")
    global  reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global  reps
    reps += 1
    work_sec=WORK_MIN * 60
    short_break_sec=SHORT_BREAK_MIN * 60
    long_break_sec=LONG_BREAK_MIN * 60
    if reps == 8:
        count_down(long_break_sec)
        timer_label.config(text="Break",fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_sec)
        timer_label.config(text='Break',fg=PINK)
    else:
        count_down(work_sec)
        timer_label.config(text="Work",fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global  timer
    count_min=math.floor(count/60)
    count_sec=count % 60
    if count_sec < 10:
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks=""
        for _ in range(math.floor(reps/2)):
            marks += "🗸"
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window =Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_image=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_image)
timer_text=canvas.create_text(100,130,text="00:00",fill="green",font=(FONT_NAME,35,"bold"))
canvas.grid(row=2,column=2)


timer_label=Label(text="Timer",fg=GREEN,bg=YELLOW,font=(FONT_NAME,30,"normal"))
timer_label.grid(row=1,column=2)


start_button=Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(row=4,column=1)
reset_button=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(row=4,column=3)

# check_button=IntVar()
# check_mark=Checkbutton(check_button,)
check_marks=Label(fg="black",bg=YELLOW,font=(FONT_NAME,30))
check_marks.grid(row=5,column=2)
window.mainloop()