#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    bool threeConsecutiveOdds(vector<int>& arr) {
        int cnt =  0;
        for (int i = 0; i < arr.size(); i++) 
        {
            if (arr[i] % 2) 
            {
                cnt++;
                if (cnt == 3) 
                {
                    return true;
                }
            }
            else 
            {
                cnt = 0;
            }
        }

        return false;
    }
};


int main()
{
    vector<int> arr = {2,6,4,1};
    
    Solution sol;
    cout << sol.threeConsecutiveOdds(arr);
    return 0;
}