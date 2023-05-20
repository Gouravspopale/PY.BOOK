import tkinter as tk
import csv 

def submit():
    cust=txt1.get()
    phonenum=txt2.get()
    proname=txt3.get()
    proamt=txt4.get()
    total=txt1.get()

    with open("C:/Users/User7/Desktop/PY.BOOK/cust.csv","w") as file:
        data=csv.writer(file)
        
        data.writerow([cust,phonenum,proname,proamt,total])

main = tk.Tk(className="  #COSTUMER DETAILES#")
main.geometry("600x600")
main.configure(bg='white')

lable1=tk.Label(main,text="COSTUMER NAME:").grid(row=0,column=0)
txt1=tk.Entry(main)
txt1.grid(row=0,column=1)

lable2=tk.Label(main,text="PHONE NUMBER:").grid(row=1,column=0)
txt2=tk.Entry(main)
txt2.grid(row=1,column=1)

lable3=tk.Label(main,text="PRODUCT NAME:").grid(row=2,column=0)
txt3=tk.Entry(main)
txt3.grid(row=2,column=1)

lable4=tk.Label(main,text="PRODUCT AMOUNT:").grid(row=3,column=0)
txt4=tk.Entry(main)
txt4.grid(row=3,column=1)

lable5=tk.Label(main,text="TOTAL AMOUNT INCLUDE ALL TAX:").grid(row=4,column=0)
txt5=tk.Entry(main)
txt5.grid(row=4,column=1)

btn6=tk.Button(main,text="submit",command=submit).grid(row=6,column=1)

main.mainloop()

