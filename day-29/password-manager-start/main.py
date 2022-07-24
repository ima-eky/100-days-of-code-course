from tkinter import *
from tkinter import messagebox
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from random import randint, choice, shuffle
def generate_random_password():
    password_entry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(7, 9))]
    password_numbers =[choice(numbers) for _ in range(randint(2, 5))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_list=password_symbols +password_letters+password_numbers

    shuffle(password_list)
    password="".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name=website_entry.get()
    password=password_entry.get()
    email_or_username=email_or_username_entry.get()
    new_content={
        website_name:{
            "email":email_or_username,
            "password":password,
        }
    }
    if len(website_name) == 0 or len(password) == 0 or len(email_or_username)==0:
        messagebox.showinfo(title="Oops",message="Please don't leave any of the fields empty")
    if "@" not in email_or_username:
        messagebox.showinfo(title="Oops",message="Please enter a valid email")
        email_or_username_entry.delete(0,END)

    else:
        try:
            with open ("data.json","r") as data_file:
                # reading old data
                data=json.load(data_file)
                # updating old data with new data
        except FileNotFoundError:
            with open ("data.json","w") as data_file:
                json.dump(new_content,data_file,indent=4)
        else:
            data.update(new_content)
            with open("data.json","w") as data_file:
                json.dump(data,data_file,indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)
# ----------------------------FIND PASSWORD-------------#
def find_password():
    website_name = website_entry.get()
    try:
        with open ("data.json") as data_file:
            data=json.load(data_file)

    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File  found\nClick Add button to create Data File")
    else:
        if website_name in data:
            email = data[website_name]['email']
            password = data[website_name]['password']
            messagebox.showinfo(title="website_name", message=f"Email:{email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error", message="No details for the website exists")

# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title('Password Manager')
window.config(padx=50,pady=50)

canvas=Canvas(width=200,height=200)
canvas.grid(row=0,column=1)
generator_image=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=generator_image)

website_label=Label(text="Website:")
website_label.grid(row=1,column=0)

email_or_username_label=Label(text="Email/Username:")
email_or_username_label.grid(row=2,column=0)

password_label=Label(text="Password:")
password_label.grid(row=3,column=0)




website_entry=Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()

email_or_username_entry=Entry(width=39)
email_or_username_entry.grid(row=2,column=1,columnspan=2)

password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)

generate_password_button=Button(text="Generate Password",command=generate_random_password)
generate_password_button.grid(row=3,column=2)

add_button=Button(text="Add",width=35,command=save)
add_button.grid(row=4,column=1,columnspan=2)

search_button=Button(text="Search",width=13,command=find_password)
search_button.grid(row=1,column=2)








window.mainloop()