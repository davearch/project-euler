"""Largest Prime Factor
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143?
"""
import math

class Solution:

    def primeFactors(self, n):

        largest = 0

        while n % 2 == 0:
            largest = 2
            n = n // 2

        for i in range(3, int(math.sqrt(n)) + 1, 2):
            while n % i == 0:
                largest = i
                n = n // i

        if (n > 2):
            return n
        return largest

if __name__ == "__main__":
    s = Solution()
    print(s.primeFactors(600851475143))