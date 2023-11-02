#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    ac = len(sys.argv) - 1

    if ac == 0:
        msg = "{} arguments.".format(ac)
    elif ac == 1:
        msg = "{} argument:".format(ac)
    else:
        msg = "{} arguments:".format(ac)

    print(msg)

    if ac >= 1:
        for i in range(1, ac + 1):
            args = sys.argv[i]
            print("{0}: {1}".format(i, args))
