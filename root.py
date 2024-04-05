from tkinter import *
from datetime import datetime

root = Tk()
root.title('Calculator - CM: Mobin irandoust')
operator = ""

def cache(x):
    _date = datetime.now()
    with open("cache.txt",'a') as added:
        added.write(f"<{_date.year}/{_date.month}/{_date.day}> {_date.hour}:{_date.minute}:{_date.second} --> {x}\n")

def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    text_input.set(operator)
    
    
def btnClearDisplay():
    global operator
    operator = ""
    text_input.set("")
    

def btnEqualsInput():
    global operator
    sumup = str(eval(operator))
    text_input.set(sumup)
    cache(operator)
    operator=''
    
# صفحه نمایشگر ماشین حساب
text_input = StringVar()
txtDisplay = Entry(root,font=('arial',25,'bold'),textvariable=text_input,bd=30,
                   insertwidth=5,bg='powder blue',justify='center').grid(columnspan=5)


#===========================================================================#
btn7 = Button(root,command=lambda:btnClick(7),padx=18,pady=18,bd=8,fg='black',font=('arial',25,'bold'),
              text=7).grid(row=1,column=0)
btn8 = Button(root,command=lambda:btnClick(8),padx=18,pady=18,bd=8,fg='black',font=('arial',25,'bold'),
              text=8).grid(row=1,column=1)
btn9 = Button(root,command=lambda:btnClick(9),padx=18,pady=18,bd=8,fg='black',font=('arial',25,'bold'),
              text=9).grid(row=1,column=2)
plus = Button(root,command=lambda:btnClick('+'),padx=18,pady=18,bd=8,fg='green',font=('arial',25,'bold'),
              text='+').grid(row=1,column=3)
#===========================================================================#
btn4 = Button(root,command=lambda:btnClick(4),padx=18,pady=18,bd=8,fg='black',font=('arial',25,'bold'),
              text=4).grid(row=2,column=0)
btn5 = Button(root,command=lambda:btnClick(5),padx=18,pady=18,bd=8,fg='black',font=('arial',25,'bold'),
              text=5).grid(row=2,column=1)
btn6 = Button(root,command=lambda:btnClick(6),padx=18,pady=18,bd=8,fg='black',font=('arial',25,'bold'),
              text=6).grid(row=2,column=2)
subtractoin = Button(root,command=lambda:btnClick('-'),padx=18,pady=18,bd=8,fg='green',font=('arial',25,'bold'),
              text='-').grid(row=2,column=3)
#===========================================================================#
btn1 = Button(root,command=lambda:btnClick(1),padx=18,pady=18,bd=8,fg='black',font=('arial',25,'bold'),
              text=1).grid(row=3,column=0)
btn2 = Button(root,command=lambda:btnClick(2),padx=18,pady=18,bd=8,fg='black',font=('arial',25,'bold'),
              text=2).grid(row=3,column=1)
btn3 = Button(root,command=lambda:btnClick(3),padx=18,pady=18,bd=8,fg='black',font=('arial',25,'bold'),
              text=3).grid(row=3,column=2)
multi = Button(root,command=lambda:btnClick('*'),padx=18,pady=18,bd=8,fg='green',font=('arial',25,'bold'),
              text='x').grid(row=3,column=3)
#===========================================================================#
btnClear = Button(root,command=lambda:btnClearDisplay(),padx=18,pady=18,bd=8,fg='black',font=('arial',25,'bold'),
              text='C').grid(row=4,column=0)
btn0 = Button(root,command=lambda:btnClick(0),padx=18,pady=18,bd=8,fg='red',font=('arial',25,'bold'),
              text=0).grid(row=4,column=1)
btnEquals = Button(root,command=lambda:btnEqualsInput(),padx=18,pady=18,bd=8,fg='black',font=('arial',25,'bold'),
              text='=').grid(row=4,column=2)
division = Button(root,command=lambda:btnClick('/'),padx=18,pady=18,bd=8,fg='green',font=('arial',25,'bold'),
              text='/').grid(row=4,column=3)
#===========================================================================#

label = Label(text='Created:< Mobin IranDoust >',fg='yellow',bg='black')
root.mainloop()

