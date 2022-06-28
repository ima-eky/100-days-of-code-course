THEME_COLOR = "#375362"
from tkinter import  *
from quiz_brain import  QuizBrain
class  Quizinterface():
     def __init__(self,quiz_brain:QuizBrain):
         self.quiz=quiz_brain
         self.window =Tk()
         self.window.title("Quizzler")
         self.window.config(padx=20,pady=20,bg=THEME_COLOR)
         self.canvas=Canvas(height=250,width=300)
         self.question_text=self.canvas.create_text(
             150,
             125,
             width=280,
             text="Some Questions",fill=THEME_COLOR,font=("Arial",20,"italic"))
         self.canvas.grid(row=2,column=1,columnspan=2,pady=50)
         self.score_label=Label(text="Score:0",bg=THEME_COLOR,fg="white")
         self.score_label.grid(row=1,column=2)
         right_tick=PhotoImage(file="images/true.png")
         self.right_button=Button(image=right_tick,highlightthickness=0,command=self.true_pressed)
         self.right_button.grid(row=3,column=1)
         wrong_tick = PhotoImage(file="images/false.png")
         self.false_button = Button(image=wrong_tick,highlightthickness=0,command=self.false_pressed)
         self.false_button.grid(row=3, column=2)
         self.get_next_question()
         self.window.mainloop()
     def get_next_question(self):
         self.canvas.config(bg="white")
         self.score_label.config(text=f"Score:{self.quiz.score}")
         if self.quiz.still_has_questions():
             q_text=self.quiz.next_question()
             self.canvas.itemconfig(self.question_text,text=q_text)
         else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.false_button.config(state="disabled")


     def true_pressed(self):
         is_right= self.quiz.check_answer("true")
         self.give_feedback(is_right)
     def false_pressed(self):
         is_right=self.quiz.check_answer("false")
         self.give_feedback(is_right)
     def give_feedback(self,is_right):
         if is_right:
            self.canvas.config(bg="green")
         else:
             self.canvas.config(bg="red")

         self.window.after(1000, self.get_next_question)