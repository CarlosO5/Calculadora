from ast import Expression
from tkinter import *
import parser


root = Tk()
root.title("Calculadora")

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E)

i = 0


def numero(n):
    global i
    display.insert(i, n)
    i+=1

def operacion(operador):
    global i
    aperador_len = len(operador)
    display.insert(i, operador)
    i+operador

def clear_display():
    display.delete(0,END)


def undo():
    display_state = display.get()

    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, "Error")


def calcular():
    display_state = display.get()
    try:
        math_expression = parser.expr(display_state).compile()
        result = eval(math_expression)
        clear_display()
        display.insert(0, result)
    except:
        clear_display()
        display.insert(0, "Error")

    


#numeric Buttons
Button(root, text="1", command=lambda:numero(1)).grid(row=2, column=0, sticky=W+E)
Button(root, text="2", command=lambda:numero(2)).grid(row=2, column=1, sticky=W+E)
Button(root, text="3", command=lambda:numero(3)).grid(row=2, column=2, sticky=W+E)

Button(root, text="4", command=lambda:numero(4)).grid(row=3, column=0, sticky=W+E)
Button(root, text="5", command=lambda:numero(5)).grid(row=3, column=1, sticky=W+E)
Button(root, text="6", command=lambda:numero(6)).grid(row=3, column=2, sticky=W+E)

Button(root, text="7", command=lambda:numero(7)).grid(row=4, column=0, sticky=W+E)
Button(root, text="8", command=lambda:numero(8)).grid(row=4, column=1, sticky=W+E)
Button(root, text="9", command=lambda:numero(9)).grid(row=4, column=2, sticky=W+E)



#Buttons de operaciones

Button(root, text="AC", command=lambda:clear_display()).grid(row=5, column=0, sticky=W+E)
Button(root, text="0", command=lambda:numero(0)).grid(row=5, column=1, sticky=W+E)
Button(root, text="%", command=lambda:numero("%")).grid(row=5, column=2, sticky=W+E)


Button(root, text="+", command=lambda:operacion("+")).grid(row=2, column=3, sticky=W+E)
Button(root, text="-", command=lambda:operacion("-")).grid(row=3, column=3, sticky=W+E)
Button(root, text="*", command=lambda:operacion("*")).grid(row=4, column=3, sticky=W+E)
Button(root, text="/", command=lambda:operacion("/")).grid(row=5, column=3, sticky=W+E)


Button(root, text="←", command=lambda:undo()).grid(row=2, column=4, sticky=W+E, columnspan=2)
Button(root, text="Exp", command=lambda:operacion("**")).grid(row=3, column=4, sticky=W+E)
Button(root, text="^2", command=lambda:operacion("**2")).grid(row=3, column=5, sticky=W+E)
Button(root, text="(", command=lambda:operacion("(")).grid(row=4, column=4, sticky=W+E)
Button(root, text=")", command=lambda:operacion(")")).grid(row=4, column=5, sticky=W+E)
Button(root, text="=", command=lambda:calcular()).grid(row=5, column=4, sticky=W+E, columnspan=2)





root.mainloop()



















