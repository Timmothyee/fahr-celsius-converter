import tkinter as tk

def fahrenheit_to_celsius():
    fahrenheit=ent_temperature.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    lbl_result["text"]=f'{round(celsius,2)} \N{DEGREE CELSIUS}'

window=tk.Tk()
window.title('Temperature converter')
window.resizable(width=False,height=False)

window.rowconfigure(0,weight=1,minsize=50)
window.columnconfigure([0,2],weight=1,minsize=150)


frm_entry=tk.Frame(window)
frm_entry.grid(row=0,column=0)

ent_temperature=tk.Entry(frm_entry,width=10)
# ent_temperature.pack(side='left')
ent_temperature.grid(row=0,column=0)

lbl_temperature=tk.Label(frm_entry,text="\N{DEGREE FAHRENHEIT}")
# lbl_temperature.pack(side='right')
lbl_temperature.grid(column=1,row=0)

lbl_result=tk.Label(window,text="\N{DEGREE CELSIUS}")
lbl_result.grid(row=0,column=2)

btn_convert=tk.Button(window,text="\N{RIGHTWARDS BLACK ARROW}",command=fahrenheit_to_celsius)
btn_convert.grid(row=0,column=1)

window.mainloop()

