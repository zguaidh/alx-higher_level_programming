#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ls = []
    for i in range(list_length):
        try:
            elem = my_list_1[i] / my_list_2[i]
            ls.append(elem)
        except ValueError:
            print("wrong type")
            ls.append(0)
        except ZeroDivisionError:
            print("division by 0")
            ls.append(0)
        except IndexError:
            print("out of range")
            ls.append(0)
        except Exception:
            ls.append(0)
        finally:
            print(ls)
    return ls
