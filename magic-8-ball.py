# Solution by Kavyansh Khaitan (kavyansh.tech)

#### Magic 8 Ball ####
#
# Simulate a magic 8-ball.
#
# Tasks:
# [-] Allow the user to enter their question.
# [-] Display an in progress message(i.e. "thinking").
# [-] Create 20 responses, and show a random response.
# [-] Allow the user to ask another question or quit.
#
# Bonus:
# [-] Add a gui.
# [-] It must have box for users to enter the question.
# [-] It must have at least 4 buttons:
#     [-] ask
#     [-] clear (the text box)
#     [-] play again
#     [-] quit (this must close the window)


import random

import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

ANSWERS = [
    "It is certain",
    "It is decidedly so.",
    "Without a doubt",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful.",

    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again."
]

class App:
    def __init__(self) -> None:
        self.title = "Magic 8-ball"
        self.root = tk.Tk()
        self.root.title(self.title)
        self.root.resizable(False, False)

        ttk.Label(self.root, text=self.title, font=Font(size=24, weight="bold")).grid(
            row=0, column=0, columnspan=3, padx=20, pady=(10, 0)
        )

        self.inputVar = tk.StringVar()

        ttk.Label(self.root, text="Ask a question").grid(
            row=1, column=0, columnspan=3, sticky="ew", padx=10
        )
        ttk.Entry(self.root, width=50, textvariable=self.inputVar).grid(
            row=2, column=0, columnspan=3, sticky="ew", padx=10
        )

        self.ready = True
        self.playButtonTextVar = tk.StringVar(value="Ask")

        ttk.Button(self.root, textvariable=self.playButtonTextVar, command=self.play).grid(row=3, column=0, padx=5, pady=15)
        ttk.Button(self.root, text="Clear", command=self.clear).grid(row=3, column=1, padx=5, pady=15)
        ttk.Button(self.root, text="Quit", command=self.root.quit).grid(row=3, column=2, padx=5, pady=15)

        self.outputVar = tk.StringVar(value="Please ask a question to get started.")
        ttk.Label(self.root, textvariable=self.outputVar).grid(row=4, column=0, columnspan=4, pady=(0, 10))
    
    def play(self):
        if self.ready:
            if self.inputVar.get() == "":
                self.outputVar.set("Please ask a question!")
                return
            
            self.outputVar.set("Please wait, I am thinking...")
            self.root.after(500, self.show_answer)
        else:
            self.playButtonTextVar.set("Ask")
            self.outputVar.set("Please ask a question to get started.")
            self.clear()
        
        self.ready = not self.ready
    
    def show_answer(self):
        self.playButtonTextVar.set("Again")
        self.outputVar.set(random.choice(ANSWERS))
    
    def clear(self):
        self.inputVar.set("")

    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
