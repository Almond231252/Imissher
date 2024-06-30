#2.11
import tkinter as tk

m=tk.Tk()
m.title('Main UI')
m.mainloop()

#2.12
import tkinter as tk

m=tk.Tk()

m.title('Main UI')
button=tk.Button(m, text='Stop',width=25, command=lambda:m.destroy())
button.pack()
m.mainloop()

#2.13
import tkinter as tk
def counting():
    global count
    global label1text
    count+=1
    label1text.set(str(count))

m=tk.Tk()
count=0
label1text=tk.StringVar()
label1text.set(str(count))

m.title=('Main window')
button = tk.Button(m, text='Stop', width=25,
                        command=lambda :m.destroy())
button.pack()

button2 = tk.Button(m, text='Counting', width=25,
                        command=lambda :counting())
button2.pack()

label1 = tk.Label(m, borderwidth=2, relief="ridge",
                  textvariable=label1text, width=30)
label1.pack()
m.mainloop()

#2.14
import tkinter as tk

def press(n):
    global expression
    global label1text
    expression = expression+n
    label1text.set(expression)

m=tk.Tk()
m.title=('Main window')

expression=''
label1text=tk.StringVar()
label1text.set(expression)

label1 = tk.Label(m, borderwidth=2, relief="ridge",
                  textvariable=label1text, width=30)
label1.pack()
button1 = tk.Button(m, text='1', width=25,
                   command=lambda:press('1'))
button1.pack()
button = tk.Button(m, text='Stop', width=25,
                   command=lambda: m.destroy())
button.pack()
m.mainloop()

#2.15
import tkinter as tk

def press(n):
    global expression
    global label1text
    expression = expression+n
    label1text.set(expression)

m=tk.Tk()
m.title('Main window')

expression=''
label1text=tk.StringVar()
label1text.set(expression)

label1 = tk.Label(m, borderwidth=2, relief="ridge",
                  textvariable=label1text,width=20)
label1.grid(row=0, columnspan=2)

button1 = tk.Button(m, text='1', width=6, command=lambda: press('1'))
button1.grid(row=2, column=0)
button2 = tk.Button(m, text='2', width=6, command=lambda: press('2'))
button2.grid(row=2, column=1)
button3 = tk.Button(m, text='3', width=6, command=lambda: press('3'))
button3.grid(row=1, column=0)
button4 = tk.Button(m, text='4', width=6, command=lambda: press('4'))
button4.grid(row=1, column=1)

button = tk.Button(m, text='Stop', width=16,
                   command=lambda: m.destroy())
button.grid(row=3, columnspan=2)
m.mainloop()

#####
def equal():
    try:
        global expression
        global label1text
        result = str(eval(expression))
        expression = result
    except:
        result = 'ERROR'
        expression
    label1text.set(result)

###กิจกรรม2.2
import tkinter as tk

def press(n):
    global expression
    global label1text
    expression = expression+n
    label1text.set(expression)

def equal():
    try:
        global expression
        global label1text
        result = str(eval(expression))
        expression = result
    except:
        result = 'ERROR'
        expression
    label1text.set(result)

def Clear():
    global expression
    global label1text
    expression = ''
    label1text.set(expression)

m=tk.Tk()
m.title=('Main window')

expression=''
label1text=tk.StringVar()
label1text.set(expression)
label1 = tk.Label(m, borderwidth=2, relief="ridge",
                  textvariable=label1text, width=30)
label1.pack()

button1 = tk.Button(m, text='1', width=25, command=lambda: press('1'))
button1.pack()
button2 = tk.Button(m, text='2', width=25, command=lambda: press('2'))
button2.pack()
button3 = tk.Button(m, text='3', width=25, command=lambda: press('3'))
button3.pack()
button4 = tk.Button(m, text='4', width=25, command=lambda: press('4'))
button4.pack()
button5 = tk.Button(m, text='5', width=25, command=lambda: press('5'))
button5.pack()
button6 = tk.Button(m, text='6', width=25, command=lambda: press('6'))
button6.pack()
button7 = tk.Button(m, text='7', width=25, command=lambda: press('7'))
button7.pack()
button8 = tk.Button(m, text='8', width=25, command=lambda: press('8'))
button8.pack()
button9 = tk.Button(m, text='9', width=25, command=lambda: press('9'))
button9.pack()

button_add = tk.Button(m, text='+', width=25, command=lambda: press('+'))
button_add.pack()
button_sub = tk.Button(m, text='-', width=25, command=lambda: press('-'))
button_sub.pack()
button_mul = tk.Button(m, text='x', width=25, command=lambda: press('*'))
button_mul.pack()
button_div = tk.Button(m, text='÷', width=25, command=lambda: press('/'))
button_div.pack()
button_eq = tk.Button(m, text='=', width=25, command=equal)
button_eq.pack()

button_clear = tk.Button(m, text='Clear', width=25, command=Clear)
button_clear.pack()

buttonstop = tk.Button(m, text='Stop', width=25,
                   command=lambda: m.destroy())
buttonstop.pack()

m.mainloop()

##END##
