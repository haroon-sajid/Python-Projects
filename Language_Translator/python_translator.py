from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES



def convert(text="type", src='en', des='ur'):
    translator = Translator()
    translated = translator.translate(text, src=src, dest=des)
    return translated.text

def data():
    try:
        s = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(comb.get())]
        d = list(LANGUAGES.keys())[list(LANGUAGES.values()).index(des_comb.get())]
        msg = source_txt.get("1.0", END).strip()  # Get text from source text box and strip extra whitespace
        
        if msg and msg != source_placeholder:
            translated_text = convert(text=msg, src=s, des=d)
            des_text.delete("1.0", END)  # Clear previous text in destination text box
            des_text.insert(END, translated_text)  # Insert translated text into destination text box
        else:
            des_text.delete("1.0", END)  # Clear destination text box if no text in source
    except Exception as e:
        print(f"Translation error: {e}")


# Function to handle placeholder behavior
def on_entry(event, text_widget, placeholder):
    if text_widget.cget("fg") == 'grey' and text_widget.get("1.0", "end-1c") == placeholder:
        text_widget.delete("1.0", END)
        text_widget.config(fg='black')

def on_leave(event, text_widget, placeholder):
    if text_widget.get("1.0", "end-1c") == "":
        text_widget.insert("1.0", placeholder)
        text_widget.config(fg='grey')



# Create the main window
root = Tk()
root.title("Translator")
root.geometry("950x700")
root.config(bg="pink")

# Title label
lab_title = Label(root, text="Python Translator", font=("Anton SC", 35, "bold"), bg="pink", fg="navy")
lab_title.place(x=300, y=10, height=60, width=400)

# Label for the source text
lab_source = Label(root, bg="white", fg="grey")
lab_source.place(x=50, y=90, height=40, width=400)

# Label for the translated text
lab_translated = Label(root, bg="white", fg="grey")
lab_translated.place(x=500, y=90, height=40, width=400)

# Text box for the source text
source_placeholder = "Enter Text"
source_txt = Text(root, font=("Arial", 16), wrap=WORD, fg='grey')
source_txt.insert("1.0", source_placeholder)
source_txt.place(x=50, y=130, height=500, width=400)
source_txt.bind("<FocusIn>", lambda event: on_entry(event, source_txt, source_placeholder))
source_txt.bind("<FocusOut>", lambda event: on_leave(event, source_txt, source_placeholder))

# Text box for the translated text
translation_placeholder = "Translation"
des_text = Text(root, font=("Arial", 16), wrap=WORD, fg='grey')
des_text.insert("1.0", translation_placeholder)
des_text.place(x=500, y=130, height=500, width=400)
des_text.bind("<FocusIn>", lambda event: on_entry(event, des_text, translation_placeholder))
des_text.bind("<FocusOut>", lambda event: on_leave(event, des_text, translation_placeholder))


# Combobox for source language selection
lst_text = list(LANGUAGES.values())
comb = ttk.Combobox(root, values=lst_text, font=("Arial", 12))
comb.place(x=50, y=90, height=40, width=400)
comb.set("english")

# Combobox for destination language selection
des_comb = ttk.Combobox(root, values=lst_text, font=("Arial", 12))
des_comb.place(x=500, y=90, height=40, width=400)
des_comb.set("urdu")

# Configure button style
style = ttk.Style()
style.configure('TButton',
                font=('Arial', 14),
                background='white',  # steel blue
                foreground='navy',
                borderwidth=4,
                focusthickness=4,
                focuscolor='none')

# Button for translation
button = ttk.Button(root, text="Translate", style='TButton', command=data)
button.place(x=380, y=650, height=40, width=200)

# Run the application
root.mainloop()
