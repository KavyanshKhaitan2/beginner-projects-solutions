# Solution by Kavyansh Khaitan (kavyansh.tech)

#### Mean, Median, and Mode ####
# Create three functions that allow the user to find the mean, median, and mode
# of a list of numbers. If you have access or know of functions that already
# complete these tasks, do not use them.

# Subgoals:
# [-] In the mean function, give the user a way to select how many decimal
#     places they want the answer to be rounded to.
# [-] If there is an even number of numbers in the list, return both numbers
#     that could be considered the median.
# [-] If there are multiple modes, return all of them.


class Messages:
    def clear():
        print("\n" * 50)

    def intro():
        Messages.clear()
        print()
        print()
        print("############################")
        print("#### Mean, Median, Mode ####")
        print("############################")
        print()

    def select_mode(invalid=False):
        """Select from Mean, Median and Mode.

        Args:
            invalid (bool, optional): Choose to print the "invalid" message. Defaults to False.

        Returns:
            (int) 1 = Mean | 2 = Median | 3 = Mode
        """
        Messages.intro()
        print("Input was not valid, please try again!" if invalid else "")
        print("Please select one of the following modes:")
        print("[1] Mean")
        print("[2] Median")
        print("[3] Mode")
        print()
        inp = input("Select an option (1/2/3): ").strip()
        if inp in ["1", "2", "3"]:
            return int(inp)
        Messages.select_mode(invalid=True)

    def get_input(invalid=False, label: None | str = None):
        """Get an input in list form from the user.

        Args:
            invalid (bool, optional): Choose to print the "invalid" message. Defaults to False.

        Returns:
            (int) 1 = Mean | 2 = Median | 3 = Mode
        """
        Messages.intro()
        print(label if label is not None else "")
        print("Input was not valid, please try again!" if invalid else "")
        print("Please input the numbers.")
        print("")
        print(
            "Format: 'a, b, c, d, e, ...' where a, b, c, d, e are integers or decimal numbers"
        )
        print("")
        inp = input(">>> ").strip()

        try:
            nums = inp.split(",")
            out = []
            for num in nums:
                out.append(float(num.strip()))
            return out
        except Exception:
            Messages.get_input(invalid=True, label=label)


def mean(nums: list[float | int]) -> list[float | int]:
    mean_of_nums = sum(nums) / len(nums)
    return [mean_of_nums]


def mode(nums: list[float | int]) -> list[float | int]:
    occurances = {}
    for num in nums:
        occurances[num] = occurances.get(num, 0) + 1

    out = []
    max_occur = 0
    for k in occurances:
        v = occurances[k]
        if v > max_occur:
            max_occur = v
            out = []
        if v == max_occur:
            out.append(k)

    return out

def median(nums: list[float | int]) -> list[float | int]:
    nums.sort()
    len(nums)
    if len(nums) % 2 == 1: # Odd length
        return [nums[len(nums)//2]]
    else: # Even length
        el1 = nums[len(nums)//2 - 1]
        el2 = nums[len(nums)//2]
        return [el1, el2]


def start():
    mmm_mode = Messages.select_mode()
    if mmm_mode == 1:
        label = "Mean"
    if mmm_mode == 2:
        label = "Median"
    if mmm_mode == 3:
        label = "Mode"

    nums = Messages.get_input(label=f"#### {label} ####")

    if mmm_mode == 1: # Mean
        out = mean(nums)
    if mmm_mode == 2: # Median
        out = median(nums)
    if mmm_mode == 3: # Mode
        out = mode(nums)
    
    new_out = []
    for i in out:
        new_out.append(str(i))

    print(f"{label}:", ", ".join(new_out))


if __name__ == "__main__":
    while 1:
        start()
        if "n" in input("Do you want to restart program? [Y/n] :: ").lower():
            print("Bye!")
            break
        else:
            print("Okay, restarting program.")
