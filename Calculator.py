from tkinter import *
# Title and initialization
root = Tk()
root.title('Calculator')
# Entry field
e = Entry(root,width=35,borderwidth=5)
e.grid(row=0, column=0, columnspan=3, pady=15, padx=10)
#Functions
def onClick(char):
    global e
    current  = e.get()
    e.delete(0,END)
    e.insert(0,current + char)
    
def calculator():
 exp = str(e.get())   
 class stack():
    def __init__(self):
        self.elements = []

    def push(self, item):
        self.elements.append(item)

    def top(self):
        return self.elements[-1]

    def pop(self):
        b = self.elements[-1]
        del self.elements[-1]
        return b

    def isEmpty(self):
        return len(self.elements) == 0


 l = ['+', '-', '*', '/', '^', '(', ')']

#Converting string to list in a special way


 def strToList(s):
    l = ['+', '-', '*', '/', '^', '(', ')']
    k = []
    d = 0
    while d < len(s):
      if s[d] in l:
        k.append(s[d])
        d += 1
      else:
        c = 0
        res = ""
        while s[d+c] not in l:
            res += s[d+c]
            c += 1
        k.append(res)
        d = d+c
    return k

#-------------------------------------


 pref = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '(': 0, ')': 0}

# exp = input('Enter the infix expression: ')

#Function to convert infix to postfix expression


 def convert(e):
    o_stack = stack()
    op_stack = stack()
    e = '('+e+')'
    temp = strToList(e)
    for i in temp:
        if i not in l:
            o_stack.push(i)
        elif op_stack.isEmpty() and i in l:
            op_stack.push(i)
        elif not op_stack.isEmpty():
            if pref[i] > pref[op_stack.top()]:
                op_stack.push(i)
            elif pref[i] <= pref[op_stack.top()] and i != '(' and i != ')':
                while pref[op_stack.top()] >= pref[i] and op_stack.top() != '(':
                    o_stack.push(op_stack.pop())
                op_stack.push(i)
            elif i == '(':
                op_stack.push(i)
            elif i == ')':
                while op_stack.top() != '(':
                    o_stack.push(op_stack.pop())
                op_stack.pop()
    return o_stack


 ans_stack = convert(exp)
 ev_stack = stack()
 str1 = ""

#Popping stack to get postfix expression

 while not ans_stack.isEmpty():
  c = ans_stack.pop()
  if len(c) > 1:
    str1 += c[::-1]
    ev_stack.push(c)
  else:
    str1 += c
    ev_stack.push(c)
 str2 = str1[::-1]
 r_stack = stack()

#Evaluating postfix expression

 while not ev_stack.isEmpty():
  if ev_stack.top() not in l:
    r_stack.push(ev_stack.pop())
  else:
    if ev_stack.top() == '+':
      ev_stack.pop()
      b = r_stack.pop()
      a = r_stack.pop()
      c = float(a)+float(b)
      ev_stack.push(c)
    elif ev_stack.top() == '-':
      ev_stack.pop()
      b = r_stack.pop()
      a = r_stack.pop()
      c = float(a)-float(b)
      ev_stack.push(c)
    elif ev_stack.top() == '*':
      ev_stack.pop()
      b = r_stack.pop()
      a = r_stack.pop()
      c = float(a)*float(b)
      ev_stack.push(c)
    elif ev_stack.top() == '/':
      ev_stack.pop()
      b = r_stack.pop()
      a = r_stack.pop()
      c = float(a)/float(b)
      ev_stack.push(c)
    elif ev_stack.top() == '^':
      ev_stack.pop()
      b = r_stack.pop()
      a = r_stack.pop()
      c = float(a)**float(b)
      ev_stack.push(c)
 e.delete(0,END)
 e.insert(0,r_stack.pop())


def clear():
    e.delete(0,END)

def backspace():
    current = e.get()
    e.delete(0,END)
    e.insert(0,current[:-1])
# Adding buttons (Digits)
button1 = Button(root,text='1',padx=40,pady=20,command=lambda :onClick('1')).grid(row=1,column=0)
button2 = Button(root,text='2',padx=40,pady=20,command=lambda :onClick('2')).grid(row=1,column=1)
button3 = Button(root,text='3',padx=40,pady=20,command=lambda :onClick('3')).grid(row=1,column=2)
button4 = Button(root,text='4',padx=40,pady=20,command=lambda :onClick('4')).grid(row=2,column=0)
button5 = Button(root,text='5',padx=40,pady=20,command=lambda :onClick('5')).grid(row=2,column=1)
button6 = Button(root,text='6',padx=40,pady=20,command=lambda :onClick('6')).grid(row=2,column=2)
button7 = Button(root,text='7',padx=40,pady=20,command=lambda :onClick('7')).grid(row=3,column=0)
button8 = Button(root,text='8',padx=40,pady=20,command=lambda :onClick('8')).grid(row=3,column=1)
button9 = Button(root,text='9',padx=40,pady=20,command=lambda :onClick('9')).grid(row=3,column=2)
# Adding buttons (Operators)
button_plus = Button(root, text='+', padx=40,pady=20,command=lambda :onClick('+')).grid(row=4, column=0)
button_minus = Button(root, text='-', padx=40,pady=20,command=lambda :onClick('-')).grid(row=4, column=1)
button_multiply= Button(root, text='*', padx=40,pady=20,command=lambda :onClick('*')).grid(row=4, column=2)
button_divide = Button(root, text='/', padx=40,pady=20,command=lambda :onClick('/')).grid(row=5, column=0)
button_power= Button(root, text='^', padx=40,pady=20,command=lambda :onClick('^')).grid(row=5, column=1)
button_equal= Button(root, text='=', padx=40,pady=20,command=calculator).grid(row=5, column=2)
button_clear = Button(root,padx=30,pady=20,text='Clear',command=clear).grid(row=6,column=0)
button_back = Button(root,padx=30,pady=20,text='<---',command=backspace).grid(row=6,column=1)
button_dot = Button(root,text='.',padx=40,pady=20,command=lambda :onClick('.')).grid(row=6,column=2)
#Run Loop
root.mainloop()
