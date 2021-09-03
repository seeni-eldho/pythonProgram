x=5
def foo():
    global y
    y=7
    print('loccal',y)

foo()
print('local',y)
