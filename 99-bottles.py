line1 = "'x' bottles of beer on the wall, 'x' bottles of beer."
line2 = "Take one down and pass it around, 'x' bottles of beer on the wall."

for i in range(99, -1, -1):
    print()
    if i == 1:
        print(line1.replace("'x'", f"{i}").replace("bottles", "bottle"))
        print(line2.replace("'x'", f"{i-1}").replace("0", "no more"))
        continue

    if i == 0:
        print("No more bottles of beer on the wall, no more bottles of beer.")
        print("Go to the store and buy some more, 99 bottles of beer on the wall.")
        continue

    print(line1.replace("'x'", f"{i}"))
    print(line2.replace("'x'", f"{i-1}"))
