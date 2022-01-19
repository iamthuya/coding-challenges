"""
You are given a list of numbers, and a target number k.
Return whether or not there are two numbers in the list that add up to k.

Example:
Given [4, 7, 1 , -3, 2] and k = 5,
return true since 4 + 1 = 5.

Try to do it in a single pass of the list.
"""

from typing import List


def main():
    num_list = [4, 7, 1, -3, 2]
    target = 5
    result = two_sum(num_list=num_list, target=target)
    print(result)


def two_sum(num_list: List[int], target: int) -> bool:
    for idx, num in enumerate(num_list):
        if target - num in num_list:
            return True
    return False


if __name__ == "__main__":
    main()
