from typing import List

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        res = []
        for path in folder:
            if not res or not path.startswith(res[-1] + "/"):
                res.append(path)
        return res   
            
def main():
    sol = Solution()
    folder = ["/a", "/a/b", "/c/d", "/c/d/e", "/c/f"]
    print(sol.removeSubfolders(folder))
    
if __name__ == "__main__":
    main()
    