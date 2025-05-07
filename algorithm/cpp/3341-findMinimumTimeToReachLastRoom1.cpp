#include <iostream>
#include <vector>
#include <queue>
using namespace std;

class Solution {
public:
    int minTimeToReach(vector<vector<int>>& moveTime) {
        int m = moveTime.size(), n = moveTime[0].size();
        vector<vector<int>> dist(m, vector<int>(n, INT_MAX));
        dist[0][0] = 0;
        
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, greater<>> pq;
        pq.push({0, 0, 0});

        vector<vector<int>> dirs = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

        while (!pq.empty())
        {
            auto [time, row, col] = pq.top();
            pq.pop();

            if (row == m - 1 && col == n - 1) {
                return time;
            }

            for (auto& dir: dirs) {
                int r = row + dir[0], c = col + dir[1];

                if (r >= 0 && r < m && c >= 0 && c < n) {
                    int arriveTime = time + 1 + max(0, moveTime[r][c] - time);

                    if (arriveTime < dist[r][c]) {
                        dist[r][c] = arriveTime;
                        pq.push({arriveTime, r, c});
                    }
                }
            }
        }

        return -1;
    }
};

int main()
{
    vector<vector<int>> moveTime;
    moveTime = {{15,58},{67,4}};

    Solution sol;
    cout << sol.minTimeToReach(moveTime);

    return 0;
}