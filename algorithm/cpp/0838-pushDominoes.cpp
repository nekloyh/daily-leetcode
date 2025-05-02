#include <iostream>
#include <string>
using namespace std;

class Solution {
public:
    string processString(int start, int end, char left, char right)
    {
        if (start > end) return "";

        int len = end + 1 - start;
        string str = "";

        if (left == 'R')
        {
            if (right == 'L')
            {
                str = string(len/2, 'R');
                if (len % 2) str += '.';
                str = str + string(len/2, 'L');
            }
            else str = string(len, 'R');
        }
        else
        {
            if (left == '.')
            {
                if (right == 'R')
                {
                    str = string(len - 1, '.');
                    str += 'R';
                }
                else str = string(len, right);
            }
            else
            {
                str += 'L';
                str = str + string(len - 1, right);
            }
        }

        return str;
    }

    string pushDominoes(string dominoes)
    {
        string res = "";
        int n = dominoes.length();
        int start = 0, end = 0;

        while (end < n)
        {
            if (dominoes[end] == '.')
                end++;
            else
            {
                if (dominoes[end] == 'R' && end != 0)
                    res = res + processString(start, end - 1, dominoes[start], dominoes[end - 1]);
                if (dominoes[end] == 'L')
                    res = res + processString(start, end, dominoes[start], dominoes[end]);

                start = res.length();
                end++;
            }
        }

        if (res.length() < dominoes.length())
            res = res + processString(start, n - 1, dominoes[start], dominoes[n - 1]);

        return res;
    }
};

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string dominoes = ".R...L.";
    //cin >> dominoes;

    Solution sol;
    cout << sol.pushDominoes(dominoes);

    return 0;
}