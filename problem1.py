"""Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or
5, we get 3, 5, 6 and 9. The sum of these multiples is 23. Find the sum
of all the multiples of 3 or 5 below 1000.
"""
class Solution:

    def multiples(self, bound):
        _sum = 0
        for num in range(bound):
            if num % 3 == 0:
                _sum += num
            elif num % 5 == 0:
                _sum += num
        return _sum

if __name__ == "__main__":
    s = Solution()
    print(s.multiples(10))
    print(s.multiples(1000))
