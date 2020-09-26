# magic-8-ball
# Jordan Stoner
# September 2020

# Prompt:
# Simulate a magic 8-ball.
# Allow the user to enter their question.
# Display an in progress message(i.e. "thinking").
# Create 20 responses, and show a random response.
# Allow the user to ask another question or quit.
# Bonus:
# Add a gui.
# It must have box for users to enter the question.
# It must have at least 4 buttons:
# ask
# clear (the text box)
# play again
# quit (this must close the window)

from random import choice
from tkinter import *
import time

def prompt_user():
    print("Hi! I'm your magic 8-ball!  What would you like to ask?")
    prompt = input(">")


def thinking():
    thinking = "....."
    print("Hmm...let me think about that:")
    for i in range(5, 0, -1):
        time.sleep(0.5)
        print(thinking[0:i])
    time.sleep(0.25)


def generate_response():
    responses = [
        "Absolutely!",
        "Definitely yes!",
        "Sure thing!",
        "The stars say YES!"
        "Ask again...",
        "I'm not sure...",
        "Why would you ask that!?!",
        "Probably not",
        "Emphatically NO!"
    ]

    return choice(responses)


def main():
    # prompt_user()
    # thinking()
    # print(generate_response())
    root = Tk()
    
    def ask_click():
        myLabel = Label(root, text=e.get())
        myLabel.pack()

    entry_label = Label(root, text='What would you like to ask?', borderwidth=5)
    entry_label.pack()

    e = Entry(root, width=50)
    e.pack()
    e.insert(0, 'Type question here...')

    ask_button = Button(root, text='Ask', command=ask_click)    
    ask_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()