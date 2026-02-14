#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int numEquivDominoPairs(vector<vector<int>>& dominoes) {
        for (int i = 0; i < dominoes.size(); i++) 
            if (dominoes[i][0] > dominoes[i][1])
            {
                int temp = dominoes[i][0];
                dominoes[i][0] = dominoes[i][1];
                dominoes[i][1] = temp;
            }
        
        sort(dominoes.begin(), dominoes.end());

        int res = 0;
        
        for (int l = 0, r = 1; r < dominoes.size(); r++)
            if (dominoes[l] == dominoes[r]) res += r - l;
            else l = r;

        return res;
    }

    int _numEquivDominoPairs(vector<vector<int>>& dominoes) 
    {
        int domino[10][10] = {0};
        int res = 0; 

        for (int i = 0; i < dominoes.size(); i++)
        {
            if (dominoes[i][0] == dominoes[i][1])   res += domino[dominoes[i][0]][dominoes[i][1]];
            else res += domino[dominoes[i][0]][dominoes[i][1]] + domino[dominoes[i][1]][dominoes[i][0]];
            
            domino[dominoes[i][0]][dominoes[i][1]]++;
        }

        return res;
    }
};

int main() 
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<vector<int>> dominoes = {{1,2},{1,2},{1,1},{1,2},{2,2}};

    Solution sol;
    cout << sol._numEquivDominoPairs(dominoes);

    return 0;
}