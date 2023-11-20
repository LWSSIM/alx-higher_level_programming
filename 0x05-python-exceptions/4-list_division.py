#!/usr/bin/python3
# divide list_1 elements by list_2's
def list_division(my_list1, my_list2, list_lenght):
    my_list = []
    n = 0
    for i in range(list_lenght):
        try:
            n = my_list1[i] / my_list2[i]
        except ZeroDivisionError:
            print("division by 0")
            n = 0
        except TypeError:
            print("wrong type")
            n = 0
        except IndexError:
            print("out of range")
            n = 0
        finally:
            my_list.append(n)
    return my_list