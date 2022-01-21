"""
You are given an array of integers in an arbitrary order. Return whether or not it is possible to make
the array non-decreasing by modifying at most 1 element to any value.

We define an array is non-decreasing if array[i] <= array[i + 1] holds for every i (1 <= i < n).

Example:

[13, 4, 7] should return true, since we can modify 13 to any value 4 or less, to make it non-decreasing.

[13, 4, 1] should return false, since there is no way to modify just one element to make the array non-decreasing.

Challenge: Can you find a solution in O(n) time?
"""


def main():
    print(check([13, 4, 7]))
    print(check([13, 4, 1]))


def check(num_list):
    count = 0

    for i in range(len(num_list)-1, 0, -1):
        if num_list[i] < num_list[i-1]:
            count += 1

        if count > 1:
            return False

    return True


if __name__ == "__main__":
    main()
