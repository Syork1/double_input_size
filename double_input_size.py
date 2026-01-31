import math

def find_largest_n(f, c, index):
    start = 1
    max_index = 100000

    def ratio(n):
        fn = f(n, index)
        f2n = f(2 * n, index)
        if fn is None or f2n is None or fn == 0:
            return None
        return f2n / fn

    n = start
    best = None

    while n <= max_index:
        r = ratio(n)
        if r is None:
            n += 1
            continue

        if r <= c:
            best = n
            n += 1
            continue

        # current n is too big, so previous n is best
        return best

    # max_index reached
    if n == max_index + 1:
        return None
    return best

# example functions
def f(x, i):
    if x <= 0:
        return None
    if i == 0:
        return x
    elif i == 1:
        return x ** 2
    elif i == 2:
        return 2 ** x
    elif i == 3:
        return math.log(x, 2)
    elif i == 4:
        return x * math.log(x, 2)
    elif i == 5:
        return x * (x ** 0.5)
    else:
        return None

if __name__ == "__main__":
    print("Choose one of the following functions")
    print("0     1     2       3         4            5")
    print("x    x^2   2^x  log_2(x)   x*log_2(x)   x^(3/2)")

    while True:
        try:
            index = int(input("Enter index: "))
            if 0 <= index <= 5:
                break
            else:
                print("Enter a valid index inside the range (0-5)")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    while True:
        try:
            c = float(input("Enter a c value (>0): "))
            if c > 0:
                break
            else:
                print("Enter a valid c value > 0")
        except ValueError:
            print("Invalid input. Please enter a number.")

    n = find_largest_n(f, c, index)
    if n is None:
        print("No valid n found")
    else:
        print(f"The largest integer n is: {n}")