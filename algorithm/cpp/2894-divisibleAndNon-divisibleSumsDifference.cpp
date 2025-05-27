#include <iostream>
using namespace std;

class Solution {
    public:
        int differenceOfSums(int n, int m) {
            int res = 0;
            for (int i = 0; i <= n; i++) {
                if (i % m) {
                    res += i;
                }
                else {
                    res -= i;
                }
            }

            return res;
        }
    };

int main() {
    Solution sol;
    int n = 10, m = 3;
    cout << sol.differenceOfSums(10, 3);
    return 0;
}