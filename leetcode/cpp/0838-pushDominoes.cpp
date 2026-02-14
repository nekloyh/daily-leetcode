#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string pushDominoes(string dominoes)
    {
        dominoes = 'L' + dominoes + 'R';
        string res = "";
        int n = dominoes.length();
        int start = 0, end = 1;

        while (end < n)
        {
            if (dominoes[end] != '.')
            {
                if (dominoes[start] == dominoes[end])
                    res += string(end - start, dominoes[start]);
                else
                {
                    if (dominoes[start] == 'R' && dominoes[end] == 'L') 
                    {
                        int len = end + 1 - start;
                        res += string(len/2, 'R');
                        if (len%2) res += '.';
                        res += string(len/2 - 1, 'L');
                    }
                    else res += 'L' + string(end - start - 1, '.');
                }

                start = end;
           } 
           end++;
        }

        return res.substr(1, n - 2);
    }
};

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string dominoes = ".L.R...LR..L..";
    //cin >> dominoes;

    Solution sol;
    cout << sol.pushDominoes(dominoes);

    return 0;
}