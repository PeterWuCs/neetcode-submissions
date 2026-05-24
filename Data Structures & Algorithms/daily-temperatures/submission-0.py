class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temStack = []
        indexStack = []

        length = len(temperatures)
        result = [0] * length

        for i in range(length):
            if not temStack:
                temStack.append(temperatures[i])
                indexStack.append(i)
            else:
                if temperatures[i] > temStack[-1]:
                    while len(temStack) > 0 and temperatures[i] > temStack[-1]:
                        temStack.pop(-1)
                        index = indexStack.pop(-1)
                        result[index] = i - index

                temStack.append(temperatures[i])
                indexStack.append(i)

        return result
