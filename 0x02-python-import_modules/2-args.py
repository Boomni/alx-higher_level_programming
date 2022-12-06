#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    nargs = len(sys.argv)
    count = nargs - 1
    print("{:d} arguments:".format(count))
    for i in range(nargs):
        if (i == 0):
            continue
        print("{:d}: {:s}".format(i, sys.argv[i]))
