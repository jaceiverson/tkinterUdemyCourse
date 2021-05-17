import tkinter as tk

#define
root = tk.Tk()

#create title
root.title('First GUI')

#add icon on windwo
root.iconbitmap('./Resources/Section2/thinking.ico')

#set the window size
root.geometry('250x700')

#want to change windw size (x,y)
root.resizable(0,0)

#colors str or hex
root.config(bg='blue')

#2nd window
top = tk.Toplevel()
top.title('2nd Window')
top.config(bg='green')
top.geometry('200x200+500+50')

#create
root.mainloop()