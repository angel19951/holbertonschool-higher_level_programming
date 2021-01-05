#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    div = 0
    for count in range(list_length):
        try:
            div = my_list_1[count] / my_list_2[count]
        except ZeroDivisionError:
            ("division by 0")
        except TypeError:
            print("wrong type")
        except IndexError:
            print("out of range")
        except:
            div = 0
        finally:
            new_list.append(div)
    return new_list