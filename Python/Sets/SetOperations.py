def set_union_method(set1, set2):
    return set1.union(set2)

def set_union_operator(set1, set2):
    return set1 | set2

def set_intersection_method(set1, set2):
    return set1.intersection(set2)

def set_intersection_operator(set1, set2):
    return set1 & set2

def set_difference_method(set1, set2):
    return set1.difference(set2)

def set_difference_operator(set1, set2):
    return set1 - set2

def set_symmetric_difference_method(set1, set2):
    return set1.symmetric_difference(set2)

def set_symmetric_difference_operator(set1, set2):
    return set1 ^ set2

def pretty_print_set(msg, set_):
    print(msg + ' : [' + ', '.join(set_) + ']')

def main():
    set1 = set(input().split())
    set2 = set(input().split())
    pretty_print_set('Set 1', set1)
    pretty_print_set('Set 2', set2)

    union = set_union_method(set1, set2)
    pretty_print_set('Set 1 union Set 2 (using method)', union)
    union = set_union_operator(set1, set2)
    pretty_print_set('Set 1 union Set 2 (using operator)', union)

    intersection = set_intersection_method(set1, set2)
    pretty_print_set('Set 1 intersection Set 2 (using method)', intersection)
    intersection = set_intersection_operator(set1, set2)
    pretty_print_set('Set 1 intersection Set 2 (using operator)', intersection)

    difference = set_difference_method(set1, set2)
    pretty_print_set('Set 1 difference Set 2 (using method)', difference)
    difference = set_difference_operator(set1, set2)
    pretty_print_set('Set 1 difference Set 2 (using operator)', difference)

    difference = set_difference_method(set2, set1)
    pretty_print_set('Set 2 difference Set 1 (using method)', difference)
    difference = set_difference_operator(set2, set1)
    pretty_print_set('Set 2 difference Set 1 (using operator)', difference)

    symmetric_difference = set_symmetric_difference_method(set1, set2)
    pretty_print_set('Set 1 symmetric difference Set 2 (using method)', symmetric_difference)
    symmetric_difference = set_symmetric_difference_operator(set1, set2)
    pretty_print_set('Set 1 symmetric difference Set 2 (using operator)', symmetric_difference)


if __name__ == '__main__':
    main()
