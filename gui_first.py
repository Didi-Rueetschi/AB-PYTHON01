import tkinter

# function for the button end
def end():
    main.destroy()

# Main Window
main = tkinter.Tk()

# Button end
b = tkinter.Button(main, text = "end", command = end)
b.pack()

# Endless loop
main.mainloop()
