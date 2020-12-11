#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    arguments = dir(hidden_4)
    for n in arguments:
        if n[:2] != "__":
            print("{}".format(n))
