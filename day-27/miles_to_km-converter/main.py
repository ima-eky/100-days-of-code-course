from tkinter import *
from tkinter import  messagebox

def miles_to_km():
    number_in_miles=miles_input.get()
    if number_in_miles.isdigit():
        number_in_km=float(number_in_miles) * 1.60934
        rounded_number=round(number_in_km,2)
        miles_to_kilo_label.config(text=f"{rounded_number}")
    else:
        miles_input.delete(0,END)
        messagebox.showinfo(title="Oops",message="Invalid Input\nInput given must be only numbers")

window=Tk()
window.title("Mile to Km Converter")
window.config(padx=35,pady=35,height=30,width=300)

#label
miles_label=Label(text="Miles")
miles_label.grid(row=1, column=3)

is_equal_to_label=Label(text="is equal to")
is_equal_to_label.grid(row=2, column=1)

km_label=Label(text="Km")
km_label.grid(row=2, column=3)

miles_to_kilo_label=Label(text="0")
miles_to_kilo_label.grid(row=2, column=2)


#button
button=Button(text= "Calculate",command=miles_to_km)
button.grid(row=3,column=2)

#input
miles_input=Entry(width=10)
miles_input.grid(row=1, column=2)










window.mainloop()
