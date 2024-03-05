stack = input("How tall is the pyramid?")
height = int(stack)
if height > 8 or height < 1:
    print("Error: value must be in range from 1 to 8")
else:
    for i in range (1, height + 1):
        print(" " * (height - i) + "*" * i)
