# Solution by Kavyansh Khaitan (kavyansh.tech)

#### Pythagorean Triples Checker ####
# If you do not know how basic right triangles work, read this article on Wikipedia.
#
# Tasks:
# [-] Allows the user to input the sides of any triangle in any order.
# [-] Return whether the triangle is a Pythagorean Triple or not.
# [-] Loop the program so the user can use it more than once without having
#     to restart the program.
#
# Bonus:
# [-] Add a gui.


import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font


class App:
    def __init__(self) -> None:
        self.title = "Pythagorean Triplets Checker"
        self.root = tk.Tk()
        self.root.title(self.title)

        ttk.Label(self.root, text=self.title, font=Font(size=24, weight="bold")).grid(
            row=0, column=0, columnspan=3, padx=20, pady=(10, 0)
        )

        ttk.Label(self.root, text="Enter three numbers to check").grid(
            row=1, column=0, columnspan=3, sticky="ew", padx=10
        )

        self.input1Var = tk.StringVar(value=6)
        self.input2Var = tk.StringVar(value=8)
        self.input3Var = tk.StringVar(value=10)
        
        ttk.Entry(self.root, textvariable=self.input1Var, justify='center').grid(
            row=2, column=0, sticky="ew", padx=10
        )
        ttk.Entry(self.root, textvariable=self.input2Var, justify='center').grid(
            row=2, column=1, sticky="ew", padx=10
        )
        ttk.Entry(self.root, textvariable=self.input3Var, justify='center').grid(
            row=2, column=2, sticky="ew", padx=10
        )
        
        ttk.Button(self.root, text="Check", command=self.check).grid(
            row=3, column=0, columnspan=3, padx=10, pady=10
        )
    
    def check(self):
        try:
            num1 = int(self.input1Var.get())
            num2 = int(self.input2Var.get())
            num3 = int(self.input3Var.get())
        except ValueError:
            messagebox.showerror(self.title, "One or more of the inputs are not integer numbers.")
            return
        found_triplets = False
        triplets = []
        if num1 ** 2 + num2 ** 2 == num3 ** 2 and not found_triplets:
            found_triplets = True
            triplets = [num1, num2, num3]
        
        if num3 ** 2 + num1 ** 2 == num2 ** 2 and not found_triplets:
            found_triplets = True
            triplets = [num3, num1, num2]
        
        if num2 ** 2 + num3 ** 2 == num1 ** 2 and not found_triplets:
            found_triplets = True
            triplets = [num2, num3, num1]
        
        if found_triplets:
            a, b, c = triplets
            a, b = sorted((a, b))
            messagebox.showinfo(self.title, f"Found a valid triplet!\n\n=> {a}^2 + {b}^2 = {c}^2")
        else:
            messagebox.showinfo(self.title, "No triplet found.")

    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
