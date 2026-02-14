#include <iostream>
using namespace std;

class Solution {
public:
    long long M = 1000000000 + 7;

    long long numTilings(int n) {
        long long res[1007];
        res[0] = 0;
        res[1] = 1;
        res[2] = 2;
        res[3] = 5;

        for (int i = 4; i <= n ; i++)
            res[i] = (res[i - 1] * 2 % M + res[i - 3]) % M;

        return res[n];
    }
};


int main()
{
    int n;
    cin >> n;

    Solution sol;
    cout << sol.numTilings(n);

    return 0;
}