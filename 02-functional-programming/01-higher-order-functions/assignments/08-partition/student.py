def partition(lst, condition):
    first_list = []
    second_list = []

    for object in lst:
        if condition(object):
            first_list.append(object)
        else:
            second_list.append(object)
    return (first_list, second_list)


def is_children(person):
    return person.age < 18
