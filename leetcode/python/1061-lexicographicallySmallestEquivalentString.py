class Solution:
    def find(self, pa: list[int], u: int) -> int:
        if pa[u] != u:
            pa[u] = self.find(pa, pa[u])
        return pa[u]

    def union(self, pa: list[int], u: int, v: int):
        pa_u = self.find(pa, u)
        pa_v = self.find(pa, v)
        if pa_u == pa_v:
            return
        if pa_u < pa_v:
            pa[pa_v] = pa_u
        else:
            pa[pa_u] = pa_v

    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        pa = [i for i in range(26)]
        for a, b in zip(s1, s2):
            self.union(pa, ord(a) - ord("a"), ord(b) - ord("a"))

        return "".join(
            chr(self.find(pa, ord(char) - ord("a")) + ord("a")) for char in baseStr
        )

def main():
    sol = Solution()
    s1 = "hello"
    s2 = "world"
    baseStr = "hold"
    print(sol.smallestEquivalentString(s1, s2, baseStr))

if __name__ == "__main__":
    main()
    