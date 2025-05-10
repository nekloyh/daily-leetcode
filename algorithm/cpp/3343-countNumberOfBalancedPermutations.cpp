#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;

class Solution {
private:
    const int MOD = 1e9 + 7;
    vector<vector<long long>> comb;
    int freq[10] = {0};
    map<tuple<int, int, int, int>, int> memo;

    int dfs(int digit, int odd_sum, int odd, int even) {
        if (digit > 9) {
            return ((odd_sum | odd | even) == 0) ? 1 : 0;
        }

        if (odd == 0 && odd_sum > 0) {
            return 0;
        }
        
        auto key = make_tuple(digit, odd_sum, odd, even);
        if (memo.count(key)) return memo[key];

        long long res = 0;

        for (int n_odd = 0; n_odd <= min(freq[digit], odd); n_odd++) {
            int n_even = freq[digit] - n_odd;
    
            if (0 <= n_even && n_even <= even && n_odd * digit <= odd_sum) {
                long long w = comb[odd][n_odd] * comb[even][n_even] % MOD;
                w = w * dfs(digit + 1, odd_sum - n_odd * digit, odd - n_odd, even - n_even) % MOD;
                res = (res + w) % MOD;
            }
        }

        return memo[key] = res;
    }
    // https://cses.fi/problemset/task/1635

public:
    int countBalancedPermutations(string num) {
        long long nsum = 0;
        int n = num.size();

        for (int i = 0; i < n; i++) {
            freq[num[i] - '0']++;
            nsum += num[i] - '0';
        }

        if (nsum % 2) return 0;

        int m = n / 2 + 1;
        comb.assign(m + 1, vector<long long>(m + 1, 0));

        for (int i = 0; i <= m; i++) {
            comb[i][0] = 1;
            for (int j = 1; j <= i; j++) {
                comb[i][j] = (comb[i - 1][j] + comb[i - 1][j - 1]) % MOD;
            }
        }

        return dfs(0, nsum / 2, n / 2, (n + 1) /2);
    }
};

int main()
{
    string num = "123";

    Solution sol;
    cout << sol.countBalancedPermutations(num);

    return 0;
}