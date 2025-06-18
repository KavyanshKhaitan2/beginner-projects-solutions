# Solution by Kavyansh Khaitan (kavyansh.tech)

#### Change Calculator ####
# Imagine that your friend is a cashier, but has a hard time counting back change to customers.

# Tasks:
# [-] Create a program that allows him to input a certain amount of change, and
#     then print how many quarters, dimes, nickels, and pennies are needed to
#     make up the amount needed.
# [-] Example: if he inputs 1.47, the program will say that he needs 5
#     quarters, 2 dimes, 0 nickels, and 2 pennies.

# Subgoals:
# [-] Allow him to type in the amount of money given to him and the price of
#     the item. The program should then tell him the amount of each coin he
#     needs like usual.
# [-] Loop the program back to the top so your friend can continue to use the
#     program without having to close and open it every time he needs to count
#     change.


import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font
import math

MONEY_UNIT = "Rs. "

DENOMINATIONS = [1, 2, 5, 10, 20, 50, 100, 200, 500]
DENOMINATIONS.sort(reverse=True)


class App:
    def __init__(self) -> None:
        self.title = "Change calculator"
        self.root = tk.Tk()
        self.root.title(self.title)

        ttk.Label(self.root, text=self.title, font=Font(size=24, weight="bold")).grid(
            row=0, column=0, columnspan=2, padx=20, pady=(10, 0)
        )

        self.bill_amount = tk.StringVar(value=0)

        ttk.Label(self.root, text="Total bill amount").grid(
            row=1, column=0, columnspan=1, sticky="ew", padx=10
        )

        ttk.Entry(self.root, textvariable=self.bill_amount).grid(
            row=2, column=0, columnspan=1
        )

        self.money_provided = tk.StringVar(value=0)

        ttk.Label(self.root, text="Money provided").grid(
            row=1, column=1, columnspan=2, sticky="ew", padx=10
        )

        ttk.Entry(self.root, textvariable=self.money_provided).grid(
            row=2, column=1, columnspan=1
        )

        ttk.Button(self.root, text="Calculate", command=self.calculate).grid(
            row=3, column=0, padx=10, pady=10
        )
        ttk.Button(self.root, text="Clear", command=self.clear).grid(
            row=3, column=1, padx=10, pady=10
        )

    def clear(self):
        self.bill_amount.set("0")
        self.money_provided.set("0")

    def calculate(self):
        try:
            bill_amount = float(self.bill_amount.get())
            provided = float(self.money_provided.get())
        except Exception:
            messagebox.showerror(
                self.title, "One or more of the inputs is not a number!"
            )
            return

        if bill_amount > provided:
            messagebox.showinfo(self.title, "Customer did not provide enough money.")
            return

        inp = provided - bill_amount

        if inp == 0:
            messagebox.showinfo(self.title, "Total change is 0. (but why?)")
            return

        money_left = inp

        value_per_denomination = {}

        for denom in DENOMINATIONS:
            count = math.floor(money_left / denom)
            value_per_denomination[denom] = count
            money_left = money_left - (count * denom)

        tabulated = "Denominations of money to return to the customer:\n\n"

        # tab_size = len(str(max(value_per_denomination)) + MONEY_UNIT) + 1

        for denom in value_per_denomination:
            count = value_per_denomination[denom]
            if count == 0:
                continue

            part1 = f"{MONEY_UNIT}{denom}\t"  # .expandtabs(tab_size)
            tabulated = tabulated + f"{part1}* {count}\n"

        if money_left:
            tabulated = tabulated + f"\nMoney left after change: {round(money_left, 4)}"

        messagebox.showinfo(self.title, tabulated)

    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
