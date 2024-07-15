from tkinter import *
from tkinter import messagebox, filedialog
import subprocess

root = Tk()
root.title("Python IDLE By Haroon")
root.geometry("1280x720+150+80")
root.config(bg="#323846")
root.resizable(False, False)

file_path = ''

def open_file():
    global file_path
    path = filedialog.askopenfilename(filetypes=[('Python Files', '*.py')])
    if path:
        with open(path, 'r') as file:
            code = file.read()
            code_input.delete('1.0', END)
            code_input.insert('1.0', code)
            file_path = path

def save_file():
    global file_path
    if file_path == '':
        path = filedialog.asksaveasfilename(filetypes=[('Python Files', '*.py')])
        if not path:
            return  # User canceled save dialog
        file_path = path
    with open(file_path, 'w') as file:
        code = code_input.get('1.0', END)
        file.write(code)

def run_file():
    global file_path
    if file_path == '':
        messagebox.showerror("Python IDLE", "Save Your Code")
        return
    
    command = f'python "{file_path}"'  # Enclose file path in quotes
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    
    # Append output to the code_output Text widget
    code_output.insert(END, "\n\n")  # Separate previous output
    code_output.insert(END, output.decode())  # Insert stdout
    code_output.insert(END, error.decode())  # Insert stderr

# Icon
image_icon = PhotoImage(file="C:/Python_Projects/Python_IDLE/images/logo.png")
root.iconphoto(False, image_icon)

# Input code
code_input = Text(root, font="consolas 18")
code_input.place(x=180, y=0, width=680, height=720)

# Output code
code_output = Text(root, font="consolas 15", bg="#323846", fg="lightgreen")
code_output.place(x=860, y=0, width=420, height=720)

# Buttons
Open = PhotoImage(file="C:/Python_Projects/Python_IDLE/images/open.png")
Save = PhotoImage(file="C:/Python_Projects/Python_IDLE/images/save.png")
Run = PhotoImage(file="C:/Python_Projects/Python_IDLE/images/run.png")

Button(root, image=Open, bg="#323846", bd=0, command=open_file).place(x=30, y=30)
Button(root, image=Save, bg="#323846", bd=0, command=save_file).place(x=30, y=145)
Button(root, image=Run, bg="#323846", bd=0, command=run_file).place(x=30, y=260)

root.mainloop()
