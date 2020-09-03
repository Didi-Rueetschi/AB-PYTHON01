#Local Variables - value types

number= 3             # Integer
text = "Hello"    # String

def func1():
    number=5
    text="Bye"
    print("Func 1:", number, text)
def func2():
    global number, text
    number=5
    text="Bye"
    print("Func 2:", number, text)

func1()
print("Main 1:", number, text)
func2()
print("Main 2:", number, text)
