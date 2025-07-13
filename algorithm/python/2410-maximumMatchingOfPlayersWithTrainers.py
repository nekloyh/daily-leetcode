from typing import List

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        count = 0
        i = j = 0

        while i < len(players) and j < len(trainers):
            if players[i] <= trainers[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1

        return count
    
    
def main():
    sol = Solution()
    players = [4, 7, 9]
    trainers = [8, 2, 5, 8]
    print(sol.matchPlayersAndTrainers(players, trainers))
    
if __name__ == "__main__":
    main()
