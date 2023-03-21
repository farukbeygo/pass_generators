import tkinter as tk
import random as rd
import json
from tkinter import messagebox, ttk

# window part
window = tk.Tk()
window.title("pass generator")
window.minsize(width=500, height=500)

# canva part(uploaded image)
canva = tk.Canvas(width=500, height=500, highlightthickness=1)
tomato_img = tk.PhotoImage(file="pass_generator_logo.png")
canva.create_image(250, 250, image=tomato_img)
canva.place(x=0, y=0)

# some list for random password
alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['%', '&', '*', '-', '_', '+', '=', '<', '/']


# some methods here
def get_action():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "username": username,
            "password": password,
        }
    }
    try:
        with open("data.json", 'r') as data_file:
            data = json.load(data_file)
            data.update(new_data)

        with open("data.json", 'w') as data_file:
            json.dump(data, data_file, indent=4)
    except FileNotFoundError:
        with open("data.json", 'w') as data_file:
            json.dump(new_data, data_file, indent=4)


def find_in_data():
    website = website_input.get()
    try:
        with open("data.json", 'r') as data_file:
            data = json.load(data_file)
            username = data[website]["username"]
            password = data[website]["password"]
            messagebox.showinfo("Your info", f"Your username/email: {username}, password: {password} ")
    except KeyError:
        print("There is no site in that name, please add this website!!")
    except FileNotFoundError:
        print("There is no site in that name, please add this website!!")


def generate_pass():
    password_input.delete(0, "end")
    password = ""
    for i in range(12):
        place = rd.randint(0,4)
        if place == 0:
            password += rd.choice(alphabet_lower)
        elif place == 1:
            password += rd.choice(numbers)
        elif place == 2:
            password += rd.choice(symbols)
        else:
            password += rd.choice(alphabet_upper)
    password_input.insert(index=0, string=password)


# input boxes and labels
font = ("Arial", 12)

# Define custom colors
dark_gray = "#444444"
light_gray = "#CCCCCC"

website_label = ttk.Label(canva, text="Website:", style="Custom.TLabel")
canva.create_window(100, 300, window=website_label)

website_input = ttk.Entry(canva, style="Custom.TEntry")
canva.create_window(250, 300, window=website_input)

find_button = ttk.Button(canva, text="Find", style="Custom.TButton", command=find_in_data)
canva.create_window(400, 300, window=find_button)

username_label = ttk.Label(canva, text="Email/Username:", style="Custom.TLabel")
canva.create_window(100, 350, window=username_label)

username_input = ttk.Entry(canva, style="Custom.TEntry")
canva.create_window(250, 350, window=username_input)

password_label = ttk.Label(canva, text="Password:", style="Custom.TLabel")
canva.create_window(100, 400, window=password_label)

password_input = ttk.Entry(canva, style="Custom.TEntry")
canva.create_window(250, 400, window=password_input)

# button to generate a random password
generate_password_button = ttk.Button(canva, text="Generate", style="Custom.TButton", command=generate_pass)
canva.create_window(400, 400, window=generate_password_button)

# submit button
submit_button = ttk.Button(canva, text="Add", style="Custom.TButton", command=get_action)
canva.create_window(250, 450, window=submit_button)

# Define custom styles
style = ttk.Style()
style.configure("Custom.TLabel", background=dark_gray, foreground="white", font=font)
style.configure("Custom.TEntry", background=light_gray, foreground="black", font=font, borderwidth=0, padding=5, highlightthickness=1, highlightcolor=dark_gray, highlightbackground=dark_gray, insertbackground="black")
style.map("Custom.TEntry", foreground=[("disabled", "#AAAAAA")])
style.configure("Custom.TButton", background=light_gray, foreground="black", font=font, borderwidth=0, padding=0.5, highlightthickness=1, highlightcolor=dark_gray, highlightbackground=dark_gray)

window.mainloop()