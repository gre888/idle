import tkinter as tk
# from tkinter import Tk


root = tk.Tk()

# label =  tk.Label(root, text="這是我第一個視窗")
# label.pack()
# button = tk.Button(root, text="關閉",width=10, command=root.destroy)
# button.pack()


# root.mainloop()



label1 = tk.Label(root, text="First Name")
label2 = tk.Label(root, text="Last Name")
label3 = tk.Label(root, text="")

label1.grid(row=0, column=0)
label2.grid(row=1, column=0)
label3.grid(row=2, column=0)

entry1= tk.Entry(root)
entry2 = tk.Entry(root)


entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)



def display():
  label3['text'] = entry1.get() + " " + entry2.get()


label1['text'] = "First Name:"  
label2['text'] = "Last Name:"  


button = tk.Button(root, text="顯示",width=10, command=display)
button.grid(row=3, column=0)

root.mainloop()