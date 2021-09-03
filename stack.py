
def push():
    global top,size
    if top<=size:
        n1=int(input('enter the number'))
        stack.append(n1)
        top+=1
    else:
        print('stack is full')
def pop():
    global top
    if top>0:
        stack.pop()
        top-=1
    else:
        print('stack is empty')
def display():
    print(stack)

size=int(input('size'))
stack=[]
top=0
a=int(input('input the choice'))
if a==1:
    push()
elif a==2:
    pop()
elif a==3:
    display()

