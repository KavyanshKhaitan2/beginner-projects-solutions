# Solution by Kavyansh Khaitan (kavyansh.tech)

#### Coin Estimator By Weight ####
# When some people receive change after shopping, they put it into a container
# and let it add up over time. Once they fill up the container, they'll roll
# them up in coin wrappers which can then be traded in at a bank for what they
# are worth.

# Tasks:
# [-] Allow the user to input the total weight of each type of coin they have
#     (pennies, nickels, dimes, and quarters).
# [-] Print out how many of each type of coin wrapper they would need, how many
#     coins they have, and the estimated total value of all their money.

# Subgoals:
# [-] Round all numbers printed out to the nearest whole number.
# [-] Allow the user to select whether they want to submit the weight in either
#     grams or pounds.


import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font


class App:
    def __init__(self) -> None:
        self.title = "Coin estimator by weight"
        self.root = tk.Tk()
        self.root.title(self.title)

        ttk.Label(self.root, text=self.title, font=Font(size=24, weight="bold")).grid(
            row=0, column=0, columnspan=9, padx=20, pady=(10, 0)
        )

        ttk.Label(self.root, text="Please input the weight of each type of coin.").grid(
            row=1, column=0, columnspan=9, sticky="ew", padx=10
        )

        self.weight_distribution = {
            "Re 1": (1, 3.09),
            "Rs 2": (2, 4.07),
            "Rs 5": (5, 6.00),
            "Rs 10": (10, 7.74),
            "Rs 20": (20, 8.54),
        }

        self.coinInputs = {}
        for i, coin_label in enumerate(self.weight_distribution):
            self.coinInputs[coin_label] = tk.StringVar(value=0)

            ttk.Label(self.root, text=f"{coin_label} coin:").grid(
                row=2 + i, column=0, sticky="e", padx=(100, 0)
            )

            ttk.Entry(
                self.root,
                textvariable=self.coinInputs[coin_label],
                justify="right",
                width=10,
            ).grid(row=2 + i, column=1, sticky="e")

            ttk.Label(self.root, text="g").grid(row=2 + i, column=2, sticky="w")

        ttk.Button(self.root, text="Calculate", command=self.calculate).grid(
            row=99, column=0, columnspan=3, padx=10, pady=10
        )
        ttk.Button(self.root, text="Clear", command=self.clear).grid(
            row=99, column=1, columnspan=8, padx=10, pady=10
        )

    def clear(self):
        for coin_label in self.coinInputs:
            self.coinInputs[coin_label].set("0")

    def calculate(self):
        inputs = []
        try:
            for coin_label in self.coinInputs:
                weight = float(self.coinInputs[coin_label].get())
                if 0 > weight:
                    messagebox.showerror(
                        self.title, f"Weight for {coin_label} is negative."
                    )
                    return

                number_of_coins = weight / self.weight_distribution[coin_label][1]
                inputs.append(number_of_coins * self.weight_distribution[coin_label][0])
        except Exception:
            messagebox.showerror(
                self.title, "All inputs are not valid numbers. (type required: float)"
            )
            return

        total_money = sum(inputs)
        if total_money == 0:
            messagebox.showinfo(self.title, "Total estimate is 0. (but why?)")
            return
        messagebox.showinfo(self.title, f"Total estimate is Rs. {total_money}.")

    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run()
