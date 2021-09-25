def find_fibonacci_number(n):
    if n<2:
        return n
    return find_fibonacci_number(n-1)+find_fibonacci_number(n-2)

print(find_fibonacci_number(int(input())))