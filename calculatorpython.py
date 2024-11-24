from tkinter import *
def clear():
    global expression
    global label_show_cal
    result = ""
    expression = ""
    label_show_cal.set(result)

def press(number):
    global expression
    global  label_show_cal
    expression = expression + number
    label_show_cal.set(expression)

def equal():
    try:
        global  expression
        global  label_show_cal
        result = str(eval(expression))
        label_show_cal.set(result)
    except:
        result = "Error"
        expression = ""
    label_show_cal.set(result)

window = Tk()
window.title("CALCULATOR_KNIGHT")
window.option_add("*font", "consolas 20")
window.configure(bg="#CC9999")
window.geometry("570x600+100+200")
label_show_cal = StringVar()
label_show_cal.set(0)
expression = ""

Label(window,textvariable=label_show_cal, width=17,height=2, font="arrial 30", bg = "#669966", \
      fg = "black").place(x = 42, y = 30)


Button(window, text="7", width=5 ,height= 1, font=("arrial 20 bold"), bd = 1,fg = "#fff" , bg = "#996666", \
       command=lambda:press("7")).place(x = 45, y = 150)
Button(window, text="8", width=5 ,height= 1, font=("arrial 20 bold"), bd = 1,fg = "#fff" , bg = "#996666", \
       command=lambda:press("8")).place(x = 145, y = 150)
Button(window, text="9", width=5 ,height= 1, font=("arrial 20 bold"), bd = 1,fg = "#fff" , bg = "#996666", \
       command=lambda:press("9")).place(x = 245, y = 150)
Button(window, text="/", width=5 ,height= 1, font=("arrial 20 bold"), bd = 1,fg = "#fff" , bg = "#D8BFD8", \
       command=lambda:press("/")).place(x = 345, y = 150)


Button(window, text="4", width=5 ,height= 1, font=("arrial 20 bold"), bd = 1,fg = "#fff" , bg = "#996666", \
       command=lambda:press("4")).place(x = 45, y = 220)
Button(window, text="5", width=5 ,height= 1, font=("arrial 20 bold"), bd = 1,fg = "#fff" , bg = "#996666", \
       command=lambda:press("5")).place(x = 145, y = 220)
Button(window, text="6", width=5 ,height= 1, font=("arrial 20 bold"), bd = 1,fg = "#fff" , bg = "#996666", \
       command=lambda:press("6")).place(x = 245, y = 220)
Button(window, text="x", width=5 ,height= 1, font=("arrial 20 bold"), bd = 1,fg = "#fff" , bg = "#D8BFD8", \
       command=lambda:press("*")).place(x = 345, y = 220)


Button(window, text="1", width=5 ,height= 1, font=("arrial 20 bold"), bd = 1,fg = "#fff" , bg = "#996666", \
       command=lambda:press("1")).place(x = 45, y = 290)
Button(window, text="2", width=5 ,height= 1, font=("arrial 20 bold"), bd = 1,fg = "#fff" , bg = "#996666", \
       command=lambda:press("2")).place(x = 145, y = 290)
Button(window, text="3", width=5 ,height= 1, font=("arrial 20 bold"), bd = 1,fg = "#fff" , bg = "#996666", \
       command=lambda:press("3")).place(x = 245, y = 290)
Button(window, text="-", width=5 ,height= 1, font=("arrial 20 bold"), bd = 1,fg = "#fff" , bg = "#D8BFD8", \
       command=lambda:press("-")).place(x = 345, y = 290)


Button(window, text="0", width=5 ,height= 1, font=("arrial 20 bold"), bd = 1,fg = "#fff" , bg = "#996666", \
       command=lambda:press("0")).place(x = 45, y = 360)
Button(window, text="c", width=5 ,height= 1, font=("arrial 20 bold"), bd = 1,fg = "#fff" , bg = "#996666", \
       command=clear).place(x = 145, y = 360)
Button(window, text="=", width=5 ,height= 1, font=("arrial 20 bold"), bd = 1,fg = "#fff" , bg = "#996666", \
       command=equal).place(x = 245, y = 360)
Button(window, text="+", width=5 ,height= 1, font=("arrial 20 bold"), bd = 1,fg = "#fff" , bg = "#D8BFD8", \
       command=lambda:press("+")).place(x = 345, y = 360)


window.mainloop()
