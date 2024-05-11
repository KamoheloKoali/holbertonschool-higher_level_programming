#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("0 arguments.")
    else:
        if len(sys.argv) - 1 == 1:
            print("1 argument:")
        else:
            print(f"{len(sys.argv) - 1} arguments:")
        for arg_num in range(len(sys.argv) - 1):
            print(f"{arg_num + 1}: {sys.argv[arg_num + 1]}")
