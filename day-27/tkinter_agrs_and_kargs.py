from tkinter import  *

window =Tk()
window.title("My first GUI program")
window.minsize(width=500,height=300)
window.config(padx=20,pady=40)

#label
my_label=Label(text="I am a Label",font=("Arial",24,"bold"))
my_label.grid(row=0,column=0)
# my_label['text']="New text"
# my_label.config(text="New Text")

def button_clicked():
    my_label['text']=input.get()
#Button
button=Button(text="Click me",command=button_clicked)
button.grid(row=2,column=2)
button2=Button(text="Click me")
button2.grid(row=0,column=3)

#input
input=Entry(width=30)
input.insert(END,string="Some text to begin with")
input.grid(row=3,column=4)

# #text
# text=Text(height=5,width=30)
# text.focus()
# text.insert(END,"Example of a multiline entry")
#
# print(text.get("1.0",END))
# text.pack()
#
#
# #spinbox
# def spinbox_used():
#     #gets current value in spinbox
#     print(spinbox.get())
# spinbox=Spinbox(from_ =0, to=10, width =5,command=spinbox_used)
# spinbox.pack()
#
# #Scale
# #Called with current scale value.
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# #checkbutton
# def checkbutton_used():
#     print(checked_state.get())
#
# checked_state=IntVar()
# checkbutton=Checkbutton(text="Is on?",variable=checked_state,command=checkbutton_used)
# checkbutton.pack()
#
# #radiobutton
#
# def radio_used():
#     print(radio_state.get())
# radio_state=IntVar()
# radiobutton1=Radiobutton(text="Option 1",value=1,variable=radio_state,command=radio_used)
# radiobutton2=Radiobutton(text="Option 2",value=2,variable=radio_state,command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
# #listbox
#
# def listbox_used(event):
#     # Gets current selection from listbox
#     print(listbox.get(listbox.curselection()))
# listbox=Listbox(height=4)
# fruits=["Apple","Pawpaw","Orange","Banana"]
# for fruit in fruits:
#     listbox.insert(fruits.index(fruit),fruit)
# listbox.bind("<<ListboxSelect>>",listbox_used)
# listbox.pack()

window.mainloop()