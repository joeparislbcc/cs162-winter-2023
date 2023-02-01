def gcd(bigger, smaller):
    """Calculate the greatest common divisor of two positive integers."""
    if not bigger > smaller:  # swap if necessary so bigger > smaller
        bigger, smaller = smaller, bigger

    while smaller != 0:  # 1. if smaller == 0, halt
        remainder = bigger % smaller  # 2. find remainder
        # print(f"calculation, big:{bigger}, small:{smaller}, rem:{remainder}")
        bigger, smaller = smaller, remainder  # 3. reapply
    return bigger


def main():
    print(gcd(10, 5))  # 5
    print(gcd(12, 36))  # 12
    print(gcd(1245, 3196))  # ??
    print(gcd(1245, 3195))  # ??


if __name__ == "__main__":
    main()
