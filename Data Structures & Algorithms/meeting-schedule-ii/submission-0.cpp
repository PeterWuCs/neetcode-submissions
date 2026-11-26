/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    int minMeetingRooms(vector<Interval>& intervals) {

        unordered_map<int, int> count;

        for (Interval &item : intervals)
        {
            if (!count.contains(item.start))
            {
                count[item.start] = 0;
            }
            if (!count.contains(item.end))
            {
                count[item.end] = 0;
            }
            count[item.end] = count[item.end] - 1;
            count[item.start] = count[item.start] + 1;
        }
        
        vector<int> times;
        for (auto a : count)
        {
            times.push_back(a.first);
        }
        
        std::sort(times.begin(), times.end());


        int res = 0;
        int cur = 0;

        for (int time : times)
        {
            cur += count[time];
            res = std::max(res, cur);
        }

        return res;
        
    }
};
