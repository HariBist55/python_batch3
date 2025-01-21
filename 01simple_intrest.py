import tkinter as tk
def Calculate():
    principle =int(textbox1.get())
    Time = int(textbox2.get())
    Rate = int(textbox3.get())

    si=(principle*Time*Rate)/100
    result_label.config(text=f"Simple interest(SI){si}")
  
root = tk.Tk()
root.title("Software of Simple interest (SI):")
root.geometry("700x600")

label1 =tk.Label(root,text="Enter Principle (P):")
label1.pack(pady=5)
textbox1= tk.Entry(root)
textbox1.pack()

label2 = tk.Label(root,text="Enter Time (T):")
label2.pack(pady=5)
textbox2 =tk.Entry(root)
textbox2.pack()

label3 =tk.Label(root,text="Enter Rate (R):")
label3.pack(pady=5)
textbox3 =tk.Entry(root)
textbox3.pack()

Button1 =tk.Button(root,text="Calculate",command= Calculate )
Button1.pack(pady=5)

result_label = tk.Label(root,text="")
result_label.pack()

root.mainloop()