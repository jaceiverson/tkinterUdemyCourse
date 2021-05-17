import tkinter as tk

root = tk.Tk()
root.title('Buttons and Grid')
root.iconbitmap('./Resources/Section2/thinking.ico')
root.geometry('500x500')
root.resizable(0,0)
root.config(bg='#123456')

#buttons

button1 = tk.Button(root,text='Click ME1')
#option 1 = pack() option 2 = .grid()
button1.grid(row=0,column=0)

button2 = tk.Button(root,text='Click ME2',bg="#00ffff",activebackground="#ff0000")
button2.grid(row=0,column=1) 

#activebackground is color when clicked
button3 = tk.Button(root,text='Click ME3',bg='#ffffff',activebackground='red')
button3.grid(row=0,column=2,padx=10,pady=10,ipadx=15)

button4 = tk.Button(root,text='Click ME4')
button4.config(bg='black',borderwidth=5,activebackground='green')
button4.grid(row=1,column=0,columnspan=3,sticky="WE")

test1 = tk.Button(root,text='TEST1')
test2 = tk.Button(root,text='TEST2')
test3 = tk.Button(root,text='TEST3')
test4 = tk.Button(root,text='TEST4')
test5 = tk.Button(root,text='TEST5')
test6 = tk.Button(root,text='TEST6')

test1.grid(row=2,column=0,padx=5,pady=5)
test2.grid(row=2,column=1,padx=5,pady=5)
test3.grid(row=2,column=2,padx=5,pady=5,sticky='W')
test4.grid(row=3,column=0,padx=5,pady=5)
test5.grid(row=3,column=1,padx=5,pady=5)
test6.grid(row=3,column=2,padx=5,pady=5)

root.mainloop()