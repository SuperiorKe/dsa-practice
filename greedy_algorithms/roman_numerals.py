"""
Problem: Roman Numeral Encoder
Difficulty: 6 kyu
Source: Codewars
Link: https://www.codewars.com/kata/51b62bf6a9c58071c600001b

Description:
Convert integers (1-3999) to Roman numerals. Modern Roman numerals are written 
by expressing each digit separately starting with the leftmost digit and skipping 
any digit with a value of zero. Maximum 3 identical symbols in a row.

Examples:
    1 -> "I"
    4 -> "IV"
    1994 -> "MCMXCIV"
    3999 -> "MMMCMXCIX"

Key Concepts:
- Greedy algorithms (always pick the largest value that fits)
- Lookup tables / mappings
- String building patterns

Time Complexity: O(1) - fixed 13 iterations maximum
Space Complexity: O(1) - result string grows to max ~15 characters

My Approach:
1. Create a descending list of (value, symbol) pairs including subtraction cases
   (4=IV, 9=IX, 40=XL, 90=XC, 400=CD, 900=CM)
2. Use greedy approach: pick largest value that fits, append symbol, subtract value
3. Repeat until n becomes 0

Edge Cases Handled:
- Subtraction notation (4, 9, 40, 90, 400, 900)
- Maximum repetition rule (no more than 3 same symbols)
- Numbers with zero digits (e.g., 2008 = MM + VIII, skips hundreds/tens)
"""

def solution(n):
    """
    Convert an integer to Roman numeral representation.
    
    Args:
        n (int): Integer between 1 and 3999 (inclusive)
    
    Returns:
        str: Roman numeral representation
    """
    # Mapping of values to symbols in descending order
    # Includes both base symbols and subtraction cases
    roman_pairs = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    result = ""
    
    # Greedy approach: use largest values first
    for value, symbol in roman_pairs:
        while n >= value:
            result += symbol
            n -= value
    
    return result


# Test cases
if __name__ == "__main__":
    # Basic cases
    assert solution(1) == "I"
    assert solution(5) == "V"
    assert solution(10) == "X"
    
    # Subtraction cases
    assert solution(4) == "IV"
    assert solution(9) == "IX"
    assert solution(40) == "XL"
    assert solution(90) == "XC"
    assert solution(400) == "CD"
    assert solution(900) == "CM"
    
    # Complex cases
    assert solution(1994) == "MCMXCIV"
    assert solution(2008) == "MMVIII"
    assert solution(1666) == "MDCLXVI"
    assert solution(3999) == "MMMCMXCIX"
    
    print("✅ All tests passed!")