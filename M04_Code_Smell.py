def is_num():
    while True:
        try:
            x = int(input("Show me what you got.\n"))
        except ValueError:
            print("Disqualified!")
            continue
        return x

# From here down should not be changed

num = is_num()
print(f"You got {int(num)}.")
