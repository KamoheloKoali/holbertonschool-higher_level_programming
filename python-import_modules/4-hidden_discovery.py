#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as mod

    for prop in mod:
        if prop[:2] != "__":
            print(prop)
