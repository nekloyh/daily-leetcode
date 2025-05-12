#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> findEvenNumbers(vector<int>& digits) {
        int freq[10] = {0};

        for (int i = 0; i < digits.size(); i++) {
            freq[digits[i]]++;
        }

        vector<int> res;
        int cnt[10] = {0};

        for (int i = 1; i <= 9; i++) 
        {
            if (freq[i] == 0) continue;         
            cnt[i]++;

            for (int j = 0; j <= 9; j++) 
            {
                if (freq[j] == 0 || freq[j] <= cnt[j]) continue;
                cnt[j]++;

                for (int k = 0; k <= 8; k += 2) 
                {
                    if (freq[k] == 0 || freq[k] <= cnt[k]) continue;
                    res.push_back(i * 100 + j * 10 + k);
                }

                cnt[j]--;
            }
            
            cnt[i]--;
        }

        return res;
    }
};


int main()
{
    vector<int> digits;
    digits = {2,1,3,0};

    Solution sol;
    vector<int> res = sol.findEvenNumbers(digits);

    cout << "[";
    for (int i = 0; i < res.size(); i++) {
        cout << res[i];
        if (i != res.size() - 1)
            cout << ",";
    }
    cout << "]" << endl;

    return 0;
}