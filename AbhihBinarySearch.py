# First make sure that the numbers are sorted
# Find the first and last numbers, then the middle number
# To find middle value we can do (lower + upper)/2
# If our number is greater than the middle then we make the middle number the new lowest and keep the same upper bound.
# If our number is less than the middle then we make the middle number the new upper bound and keep the lower the same.
# Continue this process until the number has been found.

list = [1, 4, 6, 9, 13, 21, 83]
number = int(input("Enter a number you want to find: "))


def binary_search(list, number):
    # Get lower and upper bounds
    lower = 0
    upper = len(list)-1

    while lower <= upper:
        # Find the middle number
        middle = (lower + upper)//2

        # If the middle number is already the number we need, return True.
        if list[middle] == number:

            return True

        else:
            # Algorithm to make the middle number upper or lower then keep iterating until the number is found.
            if list[middle] < number:
                lower = middle + 1
            else:
                upper = middle - 1

    return False


binary_search()
