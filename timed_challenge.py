# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

"""
Timed Challenge: Remove Duplicates (Keep Order)

Return the values in the order they first appeared, without duplicates.

Example:
Input: ["apple", "banana", "apple", "kiwi", "banana"]
Output: ["apple", "banana", "kiwi"]
"""


def remove_duplicates(values):
    """
    Return values in their original order without duplicates.

    A set is used to quickly check whether a value has already
    appeared, while a list stores the values in their original order.
    """
    seen = set()
    result = []

    for value in values:
        if value not in seen:
            seen.add(value)
            result.append(value)

    return result


# Test cases

# Normal case
print(remove_duplicates(["apple", "banana", "apple", "kiwi", "banana"]))

# No duplicates
print(remove_duplicates([1, 2, 3, 4, 5]))

# All duplicates
print(remove_duplicates([7, 7, 7, 7]))

# Empty list
print(remove_duplicates([]))

# Duplicate values at the beginning and end
print(remove_duplicates(["a", "a", "b", "c", "b", "a"]))


"""
Reflection:

For this challenge, I chose a set combined with a list because the problem
requires two things: quickly checking whether a value has already appeared
and preserving the order of the original values. The set handles membership
checks efficiently, with average O(1) time for checking and adding a value.
The list stores each new value in the order it first appears. Because the
function examines each input value once, the overall time complexity is
O(n), with O(n) additional space in the worst case.

The 30-minute time limit influenced my decision because I wanted to use a
solution that was simple, reliable, and easy to test rather than spending
time creating a more complicated data structure. I considered that using
only a set would remove duplicates, but it would not be the best choice for
preserving the required order. Using only a list would preserve order, but
checking whether each value was already present could take O(n) time for
each item, making the overall solution O(n²).

Under time pressure, I prioritized correctness and readability over trying
to optimize every possible detail. I also added several test cases,
including an empty list, a list with no duplicates, and a list where every
value is duplicated. One trade-off is that the solution uses extra memory
for the set and result list. However, this is a reasonable compromise
because the faster lookup time makes the solution scale better for larger
inputs.
"""
