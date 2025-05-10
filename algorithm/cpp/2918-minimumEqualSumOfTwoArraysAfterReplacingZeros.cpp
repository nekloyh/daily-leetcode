#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
    public:
        long long minSum(vector<int>& nums1, vector<int>& nums2) 
        {
            int zero1 = 0, zero2 = 0;
            long long sum1 = 0, sum2 = 0;
    
            for (int i = 0; i < nums1.size(); i++) {
                if (nums1[i] == 0) {
                    zero1++;
                }
                sum1 += nums1[i];
            }
    
            for (int i = 0; i < nums2.size(); i++) {
                if (nums2[i] == 0) {
                    zero2++;
                }
                sum2 += nums2[i];
            }
    
            sum1 += zero1;
            sum2 += zero2;
    
            if (zero1 && zero2) {
                return max(sum1, sum2);
            }
            else if (!zero1 && !zero2) {
                return (sum1 == sum2) ? sum1 : -1;
            } 
            else if (zero1) {
                return (sum1 > sum2) ? -1 : max(sum1, sum2);
            }
    
            return (sum2 > sum1) ? -1 : max(sum1, sum2);
        }
    };

int main()
{
    vector<int> nums1, nums2;
    nums1 = {2,0,2,0};
    nums2 = {1, 4};

    Solution sol;
    cout << sol.minSum(nums1, nums2);
    
    return 0;
}