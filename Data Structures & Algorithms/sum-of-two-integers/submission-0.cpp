class Solution {
public:
    int getSum(int a, int b) {
        while (a)
        {
            unsigned carry = (a & b) << 1;
            b = a^b;
            a = carry;

        }

        return b;
        
    }
};
