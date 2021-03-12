#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    div = 0
    for count in range(list_length):
        try:
            div = my_list_1[count] / my_list_2[count]
        except ZeroDivisionError:
            div = 0
            print("division by 0")
        except TypeError:
            div = 0
            print("wrong type")
        except IndexError:
            div = 0
            print("out of range")
        except:
            div = 0
        finally:
            new_list.append(div)
    return new_list
