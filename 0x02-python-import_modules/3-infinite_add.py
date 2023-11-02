#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    RES = 0
    for i in range(1, len(sys.argv)):
        RES += int(sys.argv[i])
    print(RES)
