class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        def comb(a, b):
            return fac[a] * inv[b] % mod * inv[a - b] % mod if 0 <= b <= a else 0
        
        mod = 10**9 + 7
        if k > n - 1:
            return 0
        
        fac = [1] * n
        for i in range(1, n):
            fac[i] = fac[i - 1] * i % mod
        
        inv = [1] * n
        inv[n - 1] = pow(fac[n - 1], mod - 2, mod)
        for i in range(n - 1, 0, -1):
            inv[i - 1] = inv[i] * i % mod
            
        return m * comb(n - 1, k) % mod * pow(m - 1, n - 1 - k, mod) % mod
    
def main():
    n, m, k = 3, 2, 1
    sol = Solution()
    print(sol.countGoodArrays(n, m, k))

if __name__ == "__main__":
    main()
    