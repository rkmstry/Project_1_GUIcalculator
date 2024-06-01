from tkinter import * # import all from tkinter library
import tkinter as tk  
a=tk.Tk()
a.title("Calculator")                      #Giving title to calculator

expression=""

#function for Click
def bt_click(item):
    global expression
    expression = expression + str(item)
    input_text.set(expression)              #set method is used for handling expression

#function for clear
def bt_clear():
    global expression
    expression=""
    input_text.set("")                      #set method is used for handling expression

#function for equality
def bt_equal():

    try:
        global expression
        answer=str(eval(expression))        #evaluating the string expression directly
        input_text.set(answer)              #set method is used for handling answer
        expression = ""

    except:
        input_text.set("error")             #set method is used for handling error
        expression = ""
    
input_text=StringVar()

#function for entry field  
field=Entry(a,textvariable=input_text,justify=RIGHT)
field.grid(columnspan=4,ipadx=70,ipady=10)

# making buttons for row 1
button1=tk.Button(a,text="1",command=lambda:bt_click("1") ,width=10)
button1.grid(row=1,column=0)

button2=tk.Button(a,text="2",command=lambda: bt_click("2"),width=10)
button2.grid(row=1,column=1)

button3=tk.Button(a,text="3",command=lambda: bt_click("3"),width=10)
button3.grid(row=1,column=2)

buttonplus=tk.Button(a,text="+",command=lambda: bt_click("+"),width=10)
buttonplus.grid(row=1,column=3)

#making buttons for row 2
button4=tk.Button(a,text="4",command=lambda: bt_click("4"),width=10)
button4.grid(row=2,column=0)

button5=tk.Button(a,text="5",command=lambda: bt_click("5"),width=10)
button5.grid(row=2,column=1)

button6=tk.Button(a,text="6",command=lambda: bt_click("6"),width=10)
button6.grid(row=2,column=2)

buttonminus=tk.Button(a,text="-",command=lambda: bt_click("-"),width=10)
buttonminus.grid(row=2,column=3)

#making buttons for row 3
button7=tk.Button(a,text="7",command=lambda: bt_click("7"),width=10)
button7.grid(row=3,column=0)

button8=tk.Button(a,text="8",command=lambda: bt_click("8"),width=10)
button8.grid(row=3,column=1)

button9=tk.Button(a,text="9",command=lambda: bt_click("9"),width=10)
button9.grid(row=3,column=2)

buttonmul=tk.Button(a,text="*",command=lambda: bt_click("*"),width=10)
buttonmul.grid(row=3,column=3)

#making buttons for row 4
button0=tk.Button(a,text="0",command=lambda: bt_click("0"),width=10)
button0.grid(row=4,column=0)

buttondot=tk.Button(a,text=".",command=lambda: bt_click("."),width=10)
buttondot.grid(row=4,column=1)

buttondot=tk.Button(a,text="÷",command=lambda: bt_click("/"),width=10)
buttondot.grid(row=4,column=3)

buttoneq=tk.Button(a,text="=",command=lambda:bt_equal(),width=10)
buttoneq.grid(row=4,column=2)

#making buttons for row 5
buttonac=tk.Button(a,text="AC",command=lambda:bt_clear(),width=44)
buttonac.grid(row=5,column=0,columnspan=4)



a.mainloop()