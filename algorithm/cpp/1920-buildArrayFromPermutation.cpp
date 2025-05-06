#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> buildArray(vector<int>& nums) 
    {
        vector<int> res;
        int n = nums.size();
        for (int i = 0; i < n; i++)
        {
            res.push_back(nums[nums[i]]);
        }

        return res;
    }
};

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<int> n = {5,0,1,2,3,4};
    
    Solution sol;
    for (int x : sol.buildArray(n)) 
        cout << x << '\t';

    return 0;
}