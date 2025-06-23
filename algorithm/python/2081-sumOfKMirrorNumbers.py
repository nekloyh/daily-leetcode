from typing import List


class Solution:
    @staticmethod
    def createPalindrome(num: int, odd: bool) -> int:
        x = num
        if odd:
            x //= 10
        while x > 0:
            num = num * 10 + x % 10
            x //= 10
        return num

    @staticmethod
    def calKbase(num_10base: int, k: int) -> List[int]:
        if num_10base == 0:
            return [0]
        digits = []
        while num_10base > 0:
            digits.append(num_10base % k)
            num_10base //= k
        return digits

    @staticmethod
    def is_palindrome_k(num: List[int]) -> bool:
        return num == num[::-1]

    def kMirror(self, k: int, n: int) -> int:
        total = 0
        length = 1
        while n > 0:
            for i in range(length, length * 10):
                if n <= 0:
                    break
                p = self.createPalindrome(i, True)
                k_base_num = self.calKbase(p, k)
                if self.is_palindrome_k(k_base_num):
                    total += p
                    n -= 1
            for i in range(length, length * 10):
                if n <= 0:
                    break
                p = self.createPalindrome(i, False)
                k_base_num = self.calKbase(p, k)
                if self.is_palindrome_k(k_base_num):
                    total += p
                    n -= 1
            length *= 10
        return total


def main():
    k, n = 2, 8
    sol = Solution()
    print(sol.kMirror(k=k, n=n))


if __name__ == "__main__":
    main()
