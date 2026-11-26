class Solution {
public:
    vector<int> countBits(int n) {
        vector<int> output;
        output.push_back(0);

        int offset = 1;
        for (int i = 1; i <= n; i++) {
            if (i == offset * 2)
            {
                offset *= 2;
            }
            output.push_back(output[i - offset] + 1);

        }

        return output;
    }
};
