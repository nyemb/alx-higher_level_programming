#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    for e in sorted(a_dictionary.keys()):
        print("{}: {}".format(e, a_dictionary[e]))
