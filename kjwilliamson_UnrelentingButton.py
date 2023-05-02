from tkinter import *
import random
root = Tk()
root.title('Sometimes you have to give up')
root.geometry('1500x800')

counter = 0
# function


def moveButton(event):
    global counter
    counter += 1
    if counter == 15:
        lblFirstMessage.pack()
        mvngButton['text'] = 'Click to Quit?'
        moveButton(event)
    elif counter == 35:
        lblSecondMessage.pack()
        mvngButton['text'] = "Don't Quit"
        moveButton(event)
    elif counter == 55:
        lblThirdMessage.pack()
        mvngButton['text'] = "May I have your data?"
        moveButton(event)
    elif counter == 100:
        lblFourthMessage.pack()
        mvngButton['text'] = 'You are mine :)'
        moveButton(event)
    else:
        x = random.randint(0, 1450)
        y = random.randint(0, 750)
        mvngButton.place(x=x, y=y)


# create widget
lblGreetings = Label(root, text="Welcome, and, I'm sorry")
lblFirstMessage = Label(root, text="I'm sorry you're struggling. It's okay to give up :)")
lblSecondMessage = Label(root, text="Seriously. It's okay. You've done enough.")
lblThirdMessage = Label(root, text="I'm sorry...You're addiction is getting too sad to watch. I should go... :'(")
lblFourthMessage = Label(root, text="OMG! Go do something else. PLEASE! I'm done D:")
mvngButton = Button(root, text='Click to Quit!')

# place widget
lblGreetings.pack()
mvngButton.place(x=100, y=100)
mvngButton.bind("<Button-1>", moveButton)
# event loop
root.mainloop()
