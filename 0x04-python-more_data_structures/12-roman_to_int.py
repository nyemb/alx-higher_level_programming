#!/usr/bin/python3
def roman_to_int(roman_string):
    roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    i = 0
    result = 0
    if isinstance(roman_string, str):
        for i in range(len(roman_string) - 1):
            if roman[roman_string[i]] >= roman[roman_string[i + 1]]:
                result += roman[roman_string[i]]
            else:
                result -= roman[roman_string[i]]
            i += 1
        result += roman[roman_string[i]]
        return (result)
    return (0)
