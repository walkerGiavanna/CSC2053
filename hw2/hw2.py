# Gia Walker
# Cite any sources you used to help with the homework including TAs and classmates
# I looked up some python documentation on strings for some functions

from math import floor


def string3(string):
    """
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
    The string length will be at least 2.
    """
    string_len = len(string)
    end = string_len
    start = string_len - 2
    three_copies = ""
    new_copy = string[start : end]
    for i in range(1,4):
        three_copies = three_copies + new_copy
    new_string = three_copies
    return new_string
    


def has123(nums):
    """
    Given an list of ints, return True if the sequence of numbers
    1, 2, 3 appears in the list somewhere.
    """
    if (1 in nums and 2 in nums and 3 in nums):
        return True
    else:
        return False


# string 2 count_code
def hascode(string):
    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except we'll accept any letter for the 'd', so "cope" and "cooe" count.
    """
    counter = 0
    run_counter = string.count("co")
    for i in range(0, run_counter):
        if "code" in string:
            counter += 1
        elif len(string) >= 4 and "co" in string and "e" in string:
            counter += 1
    return counter


def samecatdog(string):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
   *** This can be simplfied using a Python string method ***
    """
    cat = string.count("cat")
    dog = string.count("dog")
    if cat == dog:
        return True
    else:
        return False


def centered_avg(nums):
    """
    Return the "centered" average of a list of ints, which we'll say is the mean average of the
    values, except ignoring the largest and smallest values in the list. If there are
    multiple copies of the smallest value, use just one copy, and likewise for the largest value.
    Use floor division to produce the final average. You may assume that the list is length 3 or more.
    """
    smallest = nums[0]
    largest = nums[0]
    for i in nums:
        if i < smallest:
            smallest = i
        if i > largest:
            largest = i
    for s in nums:
        if s == smallest:
            nums.remove(s)
            break
    for l in nums:
        if l == largest:
            nums.remove(l)
            break
    sum = 0
    length = len(nums)
    for e in nums:
        sum = sum + e
    average = sum / length
    average = floor(average)
    return average

    


# Test functions
assert string3("Hello") == 'lololo', 'string3(Hello) expected lololo'
print("correct")
assert string3("ab") == 'ababab', 'string3(ab) expected ababab'
print("correct")
assert string3("Hi") == 'HiHiHi', 'string3(Hi) expected HiHiHi'
print("correct")

assert has123([1, 1, 2, 3, 1]) is True, '[1, 1, 2, 3, 1] has 123'
print("correct")
assert has123([1, 1, 2, 4, 1]) is False, '[1, 1, 2, 3, 1] does not have 123'
print("correct")
assert has123([1, 1, 2, 1, 2, 3]) is True, '[1, 1, 2, 1, 2, 3] has 123'
print("correct")

assert hascode("aaacodebbb") == 1, 'aaacodebbb has code'
print("correct")
assert hascode("aaacodebbb") == 1, 'codexxcode has code'
print("correct")
assert hascode("cozexxcope") == 2, 'cozexxcope has code'
print("correct")

assert samecatdog("catdog") is True, 'catdog appear same number of times'
print("correct")
assert samecatdog("catcat") is False, 'catcat does not appear same number of times'
print("correct")
assert samecatdog("1cat1cadodog") is True, '1cat1cadodog appear the same number of times'
print("correct")

assert centered_avg([1, 2, 3, 4, 100]) == 3, 'average [1, 2, 3, 4, 100] is 3'
print("correct")
assert centered_avg([1, 1, 5, 5, 10, 8, 7]) == 5, 'average [1, 1, 5, 5, 10, 8, 7] is 5'
print("correct")
assert centered_avg([-10, -4, -2, -4, -2, 0]) == -3, 'average [-10, -4, -2, -4, -2, 0] is -3'
print("correct")


# Problems found on https://codingbat.com/python