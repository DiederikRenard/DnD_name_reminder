from tkinter import *
from tkinter import messagebox

import pandas
import json

# =============================== save info ======================================
# TODO save info


def save_info():
    name_input = name_entry.get()
    desc_input = desc_entry.get()
    align_input = align_entry.get()
    new_data = {
        name_input: {
            "Description": desc_input,
            "Align": align_input
        }
    }
    try:
        with open("char_data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        with open("char_data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4)
    else:
        data.update(new_data)
        with open("char_data.json", "w") as data_file:
            json.dump(data, data_file, indent=4)
    finally:
        name_entry.delete(0, END)
        desc_entry.delete(0, END)
        align_entry.delete(0, END)


# =============================== recuperate info ======================================

def search_info():
    name_input = name_entry.get()
    try:
        with open("char_data.json", "r") as data_file:
            data = json.load(data_file)
            messagebox.showinfo(title=f"{name_input}", message=f"Description: {data[name_input]['Description']}\n"
                                   f"Align: {data[name_input]['Align']}")
    except FileNotFoundError:
        messagebox.showwarning(title="Warning", message="Nothing saved yet!")
    except KeyError:
        messagebox.showwarning(title="Not found", message="No such name has been found.")
    finally:
        name_entry.delete(0, END)
        desc_entry.delete(0, END)
        align_entry.delete(0, END)
# =============================== UI ======================================


# TODO create canvas/window
window = Tk()
window.title("DnD Name Reminder")
window.config(padx=30, pady=30, bg="white", highlightthickness=0)

my_image = PhotoImage(file="dnd_name_logo.png")
canvas = Canvas(width=400, height=400, bg="white", highlightthickness=0)
canvas.create_image(200, 200, image=my_image)
canvas.grid(column=1, row=1, columnspan=2, rowspan=8)

# TODO spot for name, short description, friend-or-foe

name_label = Label(window, text="Name:", font=("Ariel", 15, "italic"), bg="white")
name_label.grid(column=3, row=1)

desc_label = Label(window, text="Description:", font=("Ariel", 15, "italic"), bg="white")
desc_label.grid(column=3, row=3)

align_label = Label(window, text="Friend or Foe:", font=("Ariel", 15, "italic"), bg="white")
align_label.grid(column=3, row=5)


name_entry = Entry(window, width=30, bg="white")
name_entry.grid(column=3, row=2)

desc_entry = Entry(window, width=30, bg="white")
desc_entry.grid(column=3, row=4)

align_entry = Entry(window, width=30, bg="white")
align_entry.grid(column=3, row=6)

add_button = Button(text="Add", width=30, command=save_info)
add_button.grid(column=3, row=7)

search_button = Button(text="Search", width=30, command=search_info)
search_button.grid(column=3, row=8)


# TODO recuperate info


window.mainloop()