#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Solution {
    public:
        vector<int> findWordsContaining(vector<string>& words, char x) {
            vector<int> res;
            int idx = 0;

            for (string word: words) {
                for (char c: word) {
                    if (c == x) {
                        res.push_back(idx);
                        break;
                    }
                }
                idx++;
            }

            return res;
        }
    };

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    vector<string> words = {"leet","code"};
    char x = 'e';

    Solution sol;
    vector<int> res = sol.findWordsContaining(words, x);
    for (int i = 0; i < res.size(); i++)
        cout << res[i] << "\t";

    return 0;
}