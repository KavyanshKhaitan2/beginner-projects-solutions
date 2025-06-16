# Solution by Kavyansh Khaitan (kavyansh.tech)

#### 99 Bottles ####
#
# Create a program that prints out every line to the song "99 bottles of beer
# on the wall."
#
# Tasks:
# [-] Do not use a list for all of the numbers, and do not manually type them
#     all in. Use a built in function instead.
# [-] Besides the phrase "take one down," you may not type in any numbers/names
#     of numbers directly into your song lyrics.
# [-] Remember, when you reach 1 bottle left, the word "bottles" becomes singular.


line = """
'x' bottles of beer on the wall, 'x' bottles of beer.
Take one down and pass it around, 'y' bottles of beer on the wall."""

for i in range(99, -1, -1):
    if i == 1:
        print(
            line.replace("'x'", f"{i}")
            .replace("bottles", "bottle")
            .replace("'y' bottle", "no more bottles")
        )
        continue

    if i == 0:
        print(
            """
No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall."""
        )
        continue

    print(
        line.replace("'x'", f"{i}")
        .replace("'y'", f"{i-1}")
        .replace("1 bottles", "1 bottle")
    )
