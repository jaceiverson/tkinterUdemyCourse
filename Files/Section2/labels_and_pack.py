import tkinter as tk
from tkinter import BOTH

#make window
root = tk.Tk()

root.title('Labels and  Such')
root.iconbitmap('./Resources/Section2/thinking.ico')
root.geometry('400x400')
root.resizable(0,0)
root.config(bg='#123456')

#widgets

#labels
label1 = tk.Label(root,text='Label Text1')
label1.pack()

label2 = tk.Label(root,text='Label Text2',font=('Arial',18,'bold'))
label2.pack()

label3 = tk.Label(root)
label3.config(text = 'Label Text3',font=('Cambria',10))
label3.config(bg='red')
label3.pack(padx=10,pady=50)

label4 = tk.Label(root,text='Label Text4',bg='white',fg='red')
label4.pack(pady=(0,10),ipadx=50,ipady=10,anchor='w')

label5 = tk.Label(root,text='Label Text5',bg='black',fg='green')
label5.pack(fill=BOTH,expand=True,padx=10,pady=10)

root.mainloop()