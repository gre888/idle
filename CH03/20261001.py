import tkinter as tk
# from tkinter import Tk

def click():
  print("發生按下事件")
  result['text'] = entry1.get()+entry2.get()



root = tk.Tk()
root.geometry("300x600")


# label1 = tk.Label(root, text="這是第一個視窗")
# label2 = tk.Label(root, text="這是第二個視窗")
# label3 = tk.Label(root, text="這是第三個視窗")
# label4 = tk.Label(root, text="顯示結果")
# button=tk.Button(root, text="點擊我", width=10, command=click)


# label1.pack(pady=(20,0))
# label2.pack(pady=(20,0))
# label3.pack(pady=(20,0))
# button.pack(pady=(20,0))
# label4.pack(pady=(20,0))


# label1.grid(row=0, column=0)
# label2.grid(row=1, column=0)
# label3.grid(row=2, column=0)
# label4.grid(row=3, column=1)
# entry1= tk.Entry(root)
# entry2 = tk.Entry(root)
# entry1.grid(row=0, column=1)
# entry2.grid(row=1, column=1)
# def display():
#   label3['text'] = entry1.get() + " " + entry2.get()
# label1['text'] = "First Name:"  
# label2['text'] = "Last Name:"  
# button = tk.Button(root, text="顯示",width=10, command=display)
# button.grid(row=3, column=0)



# tk.Label(root, text="First Name:").grid(row=0, column=0)
# tk.Label(root, text="Last Name:").grid(row=1, column=0)

# # 不能這樣寫 grid變數傳回None 不能整行 要先視窗元件 在排列方式
# # result=tk.Label(root, text="這是第五個視窗").grid(row=0, column=0)
# result=tk.Label(root, text="Result")
# result.grid(row=3, column=0)

# entry1 = tk.Entry(root)
# entry1.grid(row=0, column=1)
# entry2 = tk.Entry(root)
# entry2.grid(row=1, column=1)

# button2=tk.Button(root, text="按下", width=32, command=click)
# button2.grid(row=2, column=0, columnspan=2)

tk.Label(root, text="身高(cm)").grid(row=4, column=0)
tk.Label(root, text="體重(kg)").grid(row=5, column=0)
entry3 = tk.Entry(root)
entry3.grid(row=4, column=1, padx=10, pady=5)
entry4 = tk.Entry(root)
entry4.grid(row=5, column=1, padx=10, pady=5)


def cal_bmi():
    h = float(entry3.get()) / 100
    w = float(entry4.get())
    bmi=w/h**2
    result['text'] =bmi
    
    if bmi < 18.5:
        std = "過輕"
    elif 18.5 <= bmi < 24:
        std = "標準"
    result_s['text'] = std
    
button3 = tk.Button(root, text="計算", width=32, command=cal_bmi)
button3.grid(row=6, column=0, columnspan=2)

result=tk.Label(root, text="BMI=")
result.grid(row=7, column=0, padx=10, pady=5)

result_s=tk.Label(root, text="")
result_s.grid(row=8, column=0, padx=10, pady=5)






root.mainloop()