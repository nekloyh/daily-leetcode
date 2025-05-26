#include <iostream>
#include <vector>
#include <string>
using namespace std;

class Solution {
	private:
		int dfs(int u, string& colors, vector<vector<int>>& adj, vector<vector<int>>& count, vector<int>& visited) {
			if (visited[u] == 0) {
				visited[u] = 1;
				for (int v: adj[u]) {
					if (dfs(v, colors, adj, count, visited) == INT_MAX) {
						return INT_MAX;
					}

					for (int c = 0; c < 26; c++) {
						count[u][c] = max(count[u][c], count[v][c]);
					}
				}

				++count[u][colors[u] - 'a'];
				visited[u] = 2;
			}

			return visited[u] == 2 ? count[u][colors[u] - 'a'] : INT_MAX;
		}

    public:
        int largestPathValue(string colors, vector<vector<int>>& edges) {
            int n = colors.length();

            vector<vector<int>> adj(n);
            vector<vector<int>> count(n, vector<int>(26, 0));
			vector<int> visited(n);

            for (auto& e: edges) {
                adj[e[0]].push_back(e[1]);
			}

			int ans = 0;
			for (int i = 0; ans != INT_MAX && i < n; i++) {
				ans = max(ans, dfs(i, colors, adj, count, visited));
			}

			return ans == INT_MAX ? -1 : ans;
		}
};

int main() {
    Solution sol;
    string colors = "abaca";
    vector<vector<int>> edges = {{0,1},{0,2},{2,3},{3,4}};
    
    cout << sol.largestPathValue(colors, edges) << endl; 
    return 0;
}
