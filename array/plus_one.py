'''
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
'''

def plus_one(digits):
    carry = 1
    for i in range(len(digits) - 1, -1, -1):
        if not carry:
            break
        elif digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            carry = 0
    if carry:
        digits.insert(0, 1)
    return digits