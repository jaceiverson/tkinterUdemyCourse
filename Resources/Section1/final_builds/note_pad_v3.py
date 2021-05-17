#Note Pad
#Icon Public Domain, http://www.doublejdesign.co.uk, Apache 2.0
import tkinter
from PIL import ImageTk, Image
from tkinter import StringVar, IntVar, scrolledtext, END, messagebox, filedialog

#Define window
root = tkinter.Tk()
root.title("Notepad")
root.iconbitmap('pad.ico')
root.geometry("600x600")
root.resizable(0,0)

#Define fonts and colors
text_color = "#fffacd"
menu_color = "#dbd9db"
root_color = "#6c809a"
root.config(background=root_color)

#Define functions
def change_font(event):
    """Change the given font based off dropbox option.  You must pass an event parameter to this function
    It is automatically passed from the dropdown box."""
    #If the font_option is set to 'none', do not use in font decleration.
    if font_option.get() == 'none':
        my_font = (font_family.get(), str(font_size.get()))
    else:
        my_font = (font_family.get(), str(font_size.get()), font_option.get())
    
    #Make the appropriate changes to the font for the text field.
    input_text.config(font=my_font)
    

def new_note():
    """Create a new 'Note' which essentially clears the screen."""
    #Use a messagebox to ask for a new note
    question = messagebox.askyesno("New Note", "Are you sure you want to start a new note?")
    if question == 1:
        input_text.delete("1.0", END)


def close_note():
    """Closes the 'Note' which essentially quits the program."""
    #Use messagebox to ask to close note
    question = messagebox.askyesno("Close Note", "Are you sure you want to close your note?")
    if question == 1:
        root.destroy()


def save_note():
    """Save the given 'Note'.  First three lines are saved as font family, font size, and font option."""
    #Use filedialog to get location and name of where/what to save the file as.
    save_name = filedialog.asksaveasfilename(initialdir="./", title="Save Note", filetypes=(("Text Files","*.txt"),("All Files","*.*")))
    with open(save_name, 'w') as f:
        #First three lines of save file are font_familiy, font_size, font_options.  font_size must be string not int.
        f.write(font_family.get() + "\n")
        f.write(str(font_size.get()) + "\n")
        f.write(font_option.get() + "\n")

        #Write remaining text in field to the file.
        f.write(input_text.get("1.0", END))


def open_note():
    """Open a previously saved note. First three lines of note are font family, font size, and font option.
    Set the font, then load the text."""
    #Use filedialog to get location and directory of 'Note' file.
    open_name = filedialog.askopenfilename(initialdir="./", title="Open Note", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
    with open(open_name, 'r') as f:
        #Clear the current text.
        input_text.delete("1.0", END)

        #First three lines are font_family, font_size, and font_option...you must strip the new line char at the end of each line though!
        font_family.set(f.readline().strip())
        font_size.set(int(f.readline().strip()))
        font_option.set(f.readline().strip())

        #Call the change font for these .set() to go into effect.  Must pass an event to change_font() so pass an arbitrary value.
        change_font(1)

        #Read the rest of the file and insert it into the text field using the correct font setting.
        text = f.read()
        input_text.insert("1.0", text)


#GUI Layout
#Make two frames; one for the menu options and one for the text
menu_frame = tkinter.LabelFrame(root, bg=menu_color)
text_frame = tkinter.LabelFrame(root, bg=text_color)
menu_frame.pack(padx=5, pady=5)
text_frame.pack(padx=5, pady=5)

#Layout for the menu frame
#Create the menu:  new, open, save, close, font family, font size, font option
new_image = ImageTk.PhotoImage(Image.open('new.png'))
new_button = tkinter.Button(menu_frame, image=new_image, command=new_note)
new_button.grid(row=0, column=0, padx=5, pady=5)

open_image = ImageTk.PhotoImage(Image.open('open.png'))
open_button = tkinter.Button(menu_frame, image=open_image, command=open_note)
open_button.grid(row=0, column=1, padx=5, pady=5)

save_image = ImageTk.PhotoImage(Image.open('save.png'))
save_button = tkinter.Button(menu_frame, image=save_image, command=save_note)
save_button.grid(row=0, column=2, padx=5, pady=5)

close_image = ImageTk.PhotoImage(Image.open('close.png'))
close_button = tkinter.Button(menu_frame, image=close_image, command=close_note)
close_button.grid(row=0, column=3, padx=5, pady=5)

#Picked random fonts but you can use more fonts using tkinter.font.families().  Just import font
families = ['Terminal', 'Modern', 'Script', 'Courier', 'Arial', 'Calibri', 'Cambria', 'Georgia', 'MS Gothic', 'SimSun', 'Tahoma', 'Times New Roman', 'Verdana', 'Wingdings']
font_family = StringVar()
font_family.set(families[0])
font_family_drop = tkinter.OptionMenu(menu_frame, font_family, *families, command=change_font)
#Set the width so it will fit 'Times New Roman' and remain constant
font_family_drop.config(width=16)
font_family_drop.grid(row=0, column=4, padx=5, pady=5)

sizes =[8, 10, 12, 14, 16, 16, 20, 24, 32, 48, 64, 72, 96] 
font_size = IntVar()
font_size.set(sizes[2])
font_size_drop = tkinter.OptionMenu(menu_frame, font_size, *sizes, command=change_font)
#Set the width so it will remain constant,even if 8 is chosen.
font_size_drop.config(width=2)
font_size_drop.grid(row=0, column=5, padx=5, pady=5)

options = ['none', 'bold', 'italic']
font_option = StringVar()
font_option.set(options[0])
option_drop = tkinter.OptionMenu(menu_frame, font_option, *options, command=change_font)
#Set the width to be constant.
option_drop.config(width=5)
option_drop.grid(row=0, column=6, padx=5, pady=5)

#Layout for the text frame.
#Set the current font params. (family, size, option)  Since, the starting value of font_options is 'none', do not set it here.
my_font = (font_family.get(), str(font_size.get()))

#Create input_text as a scrolltext so you can scroll through the text field.
#Set default width and height to be more than window such that on the smallest text size, the text field size remains constant in the window.
input_text = tkinter.scrolledtext.ScrolledText(text_frame, width=1000, height=100, bg=text_color, font=my_font)
input_text.pack()

#Run the root window's main loop
root.mainloop()