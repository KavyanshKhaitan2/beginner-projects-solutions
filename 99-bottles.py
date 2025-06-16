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
