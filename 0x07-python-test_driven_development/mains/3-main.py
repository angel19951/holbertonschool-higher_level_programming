#!/usr/bin/python3
say_my_name = __import__('3-say_my_name').say_my_name


try:
    say_my_name("Will", "Williams")
    say_my_name("Will")
    say_my_name("", "Williams")
    say_my_name("", "")
    say_my_name("")
    say_my_name("Will", "1")
    say_my_name("Will", 1)
    say_my_name(1, "williams")
    say_my_name(None, "Williams")
    say_my_name("Will", None)
    say_my_name()
    say_my_name("Will", ["W", "w"])
    say_my_name(["W", "W"], "Williams")
    say_my_name(("W","W"), "Williams")
    say_my_name("Will", ("W", "W"))
except Exception as e:
    print(e)

