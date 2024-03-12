def print_graph(n):
    for i in range(-8, 9):
        power = get_power(i, n)
        print("*" * power)

def get_power(i, n):
    return abs(i)**n

print_graph(2)
