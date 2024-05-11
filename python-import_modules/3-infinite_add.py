#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    numbers = []
    result = 0
    if len(sys.argv) < 2:
        print("0")
    elif len(sys.argv) == 2:
        print(f"{sys.argv[1]}")
    else:
        for num in range(len(sys.argv)):
            if num < len(sys.argv) - 1:
                numbers.append(int(sys.argv[num + 1]))
        for i in numbers:
            result += i
        print(result)
