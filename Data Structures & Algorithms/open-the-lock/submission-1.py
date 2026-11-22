class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:

        d = set(deadends)
        if "0000" in d:
            return -1
        d.add("0000")


        q = deque()
        q2 = deque()
        q.append("0000")

        step = 0
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node == target:
                    return step

                d.add(node)
                for i in range(4):
                    new_state = list(node)
                    new_state[i] = str((int(node[i]) + 11) % 10)

                    if "".join(new_state) not in d:
                        d.add("".join(new_state))
                        q2.append("".join(new_state))

                    new_state[i] = str((int(node[i]) + 9) % 10)

                    if "".join(new_state) not in d:
                        d.add("".join(new_state))
                        q2.append("".join(new_state))

            step += 1
            q, q2 = q2, q

        return -1

