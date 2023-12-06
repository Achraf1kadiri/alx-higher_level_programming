#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    
    if not (roman_string and isinstance(roman_string, str)):
        return 0

    value_int = 0
    for i, char in enumerate(roman_string):
        current_value = romans[char]
        next_value = romans[roman_string[i + 1]] if i + 1 < len(roman_string) else 0

        if current_value >= next_value:
            value_int += current_value
        else:
            value_int -= current_value

    return value_int
