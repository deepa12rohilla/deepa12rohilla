# module  == module is a single file of code
# library is the broad collection of package , module ,submodule.
# import tkinter for creating GUI apps--- tkinter is a both module and library
import tkinter as tk
from tkinter import filedialog ,messagebox

#main window code
root= tk.Tk()
root.title("My text Editor")
root.geometry("800x600")

# Create a text area
text = tk.Text(
    root,
    wrap = tk.WORD,
    font = ("Helvetica", 13)
    )
text.pack(expand=True,fill=tk.BOTH)
#Main logic start  here
# FUNCTION 1: to create a new file
def new_file():
    text.delete(1.0,tk.END)

# FUNCTION 2: to open a new file
def open_file():
# open filedialog
    file_path = filedialog.askopenfilename(
        deafultextension = ".txt",
        filetypes=[("Text Files", "*.txt")]

    )
    if file_path:
        # open selected file
        with open_file("file_path", "r") as file:
            text.delete(1.0 , tk.END)
            text.insert(tk.END , file.read())

# FUNCTION 3: save the file
def save_file():
    # save the filedialog
    file_path = filedialog.asksavefilename(
        defaultextension = ".txt",
        filetypes = [("Text Files", "*.txt")]
    )
    if file_path:
        with open("file_path", "w") as file:
            file.write(text.get(1.0,tk.END))


    messagebox.showinfo("Info","File saved Successfully")
    # create Menu bar
    menu = tk.Menu(root)
    root.config(menu)

    file_menu = tk.Menu(menu)
    # New ,Open file , Save , exit
    # add filemenu to menu bar
    menu.add_cascade(label="File",menu =file_menu)

    file_menu.add_command(label="New", command=new_file)
    file_menu.add_command(label="open", command=open_file)
    file_menu.add_command(label="Save", command=save_file)
    file.add_separator()
    file_menu.add_command(label="Exit", command=root.quit)
# starts and keeps the window open
root.mainloop()