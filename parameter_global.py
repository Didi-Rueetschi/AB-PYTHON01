# Global Variables Reference types

li = [3] # List
di = {"x":3} # Dictionary
se = set([3]) # Set
def func1():
    li=[8]; di={"x":5}; se=set([8])
    print("Func 1:", li, di, se)
def func2():
    li[0]=8; di["x"]=5; se.add(8)
    print("Func 2:", li, di, se)
func1()
print("Main 1:", li, di, se)
func2()
print("Main 2:", li, di, se)
t1 = (3, 12, 9)
print("t1:", t1)
