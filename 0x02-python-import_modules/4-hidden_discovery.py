#!/usr/bin/python3
# Prints defined names in hidden_4.pyc(3.8.x)

if __name__ == "__main__":
    import hidden_4
    names = dir(hidden_4)
    for str in names:
        if str[:2] != "__":
            print(str)
