# 참조 코드 https://www.codingnow.co.kr/python/?bmode=view&idx=5751558&back_url=&t=board&page=1

import tkinter as tk

disValue = 0.0
operator = {'+': 1, '-': 2, '/': 3, 'x': 4, 'C': 5, '=': 6, '＋':7, '+/-':8 , 'del':9, '.':10}
stoValue = 0
opPre = 0
floatchange=0


def number_click(value):
    global disValue, floatchange

    if floatchange ==1:
        disValue = (disValue)+(0.1*value)
        floatchange =0
    else:
        disValue = (disValue * 10) + value
    str_value.set(disValue)

def delnum():
    global disValue
    disValue = disValue/10

def makefloat():
    global floatchange
    floatchange=1

def clear():
    global disValue, stoValue, opPre
    stoValue = 0
    opPre = 0
    disValue = 0
    str_value.set(str(disValue))

def absnum():
    global disValue
    disValue = 0-disValue
    str_value.set(disValue)

def oprator_click(value):
    global disValue, operator, stoValue, opPre
    op = operator[value]

    if op == 5:
        clear()
    elif op == 8:
        absnum()
    elif op == 9:
        delnum()
    elif op ==10:
        makefloat()
    elif disValue == 0:
        opPre = 0
    elif opPre == 0:
        opPre = op
        stoValue = disValue
        disValue = 0
        str_value.set(str(disValue))
    elif op == 6:
        if opPre == 1:
            disValue = stoValue + disValue
        if opPre == 2:
            disValue = stoValue - disValue
        if opPre == 3:
            disValue = stoValue / disValue
        if opPre == 4:
            disValue = stoValue * disValue
        if opPre == 7:
            disValue = stoValue % disValue

        str_value.set(str(disValue))
        disValue = 0
        stoValue = 0
        opPre = 0



def button_click(value):
    try:
        value = float(value)
        number_click(value)
    except:
        oprator_click(value)


win = tk.Tk()
win.title('계산기')

str_value = tk.StringVar()
str_value.set(str(disValue))
dis = tk.Entry(win, textvariable=str_value, justify='right', bg='white', fg='red')
dis.grid(column=0, row=0, columnspan=5, ipadx=80, ipady=30)

calItem = [['C', '＋', '/', 'del'],
           ['7', '8', '9', '+'],
           ['4', '5', '6', '-'],
           ['1', '2', '3', 'x'],
           ['+/-', '0', '.', '=']]

for i, items in enumerate(calItem):
    for k, item in enumerate(items):
        try:
            color = float(item)
            color = 'black'
            text_color = 'white'
        except:
            color = '#F8B86F'
            text_color = 'black'

        bt = tk.Button(win,
                       text=item,
                       width=10,
                       height=5,
                       bg=color,
                       fg=text_color,
                       command=lambda cmd=item: button_click(cmd)
                       )
        bt.grid(column=k, row=(i + 1))

win.mainloop()
