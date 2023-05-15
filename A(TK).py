import tkinter as tk

# def call():
#     input_label=(txt1.get())
#     print(input_label)
#     input_labe2=(txt2.get())
#     print(input_labe2)
#     input_labe3=(txt3.get())
#     print(input_labe3)
#     input_labe4=(txt4.get())
#     print(input_labe4)
#     input_labe5=(txt5.get())
#     print(input_labe5)


main = tk.Tk(className="  #COSTUMER DETAILES#")
main.geometry("600x600")
main.configure(bg='white')

lable1=tk.Label(main,text="COSTUMER NAME:").grid(row=0,column=0)
txt1=tk.Entry(main).grid(row=0,column=1)

lable2=tk.Label(main,text="PHONE NUMBER:").grid(row=1,column=0)
txt2=tk.Entry(main).grid(row=1,column=1)

lable3=tk.Label(main,text="PRODUCT NAME:").grid(row=2,column=0)
txt3=tk.Entry(main).grid(row=2,column=1)

lable4=tk.Label(main,text="PRODUCT AMOUNT:").grid(row=3,column=0)
txt4=tk.Entry(main).grid(row=3,column=1)

lable5=tk.Label(main,text="TOTAL AMOUNT INCLUDE ALL TAX:").grid(row=4,column=0)
txt5=tk.Entry(main).grid(row=4,column=1)

btn6=tk.Button(main,text="submit").grid(row=6,column=1)

main.mainloop()

